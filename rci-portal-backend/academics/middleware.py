import json
from django.utils.deprecation import MiddlewareMixin
from .models import AuditLog

class AuditLogMiddleware(MiddlewareMixin):
    TRACKED_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE']

    EXCLUDED_PATHS = [
        '/api/auth/login/',
        '/api/auth/token/',
        '/api/auth/token/refresh/',
        '/admin/',
        '/static/',
        '/media/',
    ]

    def process_request(self, request):
        """Capture request body for auditing"""
        if request.method in self.TRACKED_METHODS:
            try:
                request._audit_request_body = json.loads(request.body) if request.body else {}
            except Exception:
                request._audit_request_body = {}
        return None

    def process_response(self, request, response):
        if request.method not in self.TRACKED_METHODS:
            return response

        if any(request.path.startswith(path) for path in self.EXCLUDED_PATHS):
            return response

        if not getattr(request, "user", None) or not request.user.is_authenticated:
            return response

        if not (200 <= response.status_code < 300):
            return response

        action = self._get_action(request.method)
        entity = self._extract_entity(request.path)
        details = self._build_details(request, response)

        try:
            AuditLog.objects.create(
                entity=entity,
                action=action,
                user=request.user,
                details=details
            )
        except Exception as e:
            print(f"[AUDIT ERROR] Could not log action: {e}")

        return response

    def _get_action(self, method):
        return {
            'POST': 'create',
            'PUT': 'update',
            'PATCH': 'update',
            'DELETE': 'delete',
        }.get(method, 'unknown')

    def _extract_entity(self, path):
        parts = [p for p in path.split('/') if p and p != 'api']
        if parts:
            entity = parts[0].rstrip('s')  # singularize
            return entity.capitalize()
        return "Unknown"

    def _build_details(self, request, response):
        details = {
            "method": request.method,
            "path": request.path,
            "user_role": getattr(request.user, "role", None),
            "request_data": getattr(request, "_audit_request_body", {}),
        }

        try:
            response_data = json.loads(response.content.decode("utf-8"))
        except Exception:
            response_data = str(response.content[:200])  # fallback for non-JSON

        if request.method == "POST":
            # Add full_name if the object has a user field
            obj = getattr(request, "_obj", None)
            if isinstance(response_data, dict) and obj and hasattr(obj, "user"):
                response_data["full_name"] = obj.user.get_full_name()
            details["created"] = response_data

        elif request.method in ["PUT", "PATCH"]:
            before = getattr(request, "_audit_request_body", {})
            after = response_data if isinstance(response_data, dict) else {}
            obj = getattr(request, "_obj", None)
            if obj and hasattr(obj, "user"):
                after["full_name"] = obj.user.get_full_name()
            changes = {
                k: {"before": before.get(k), "after": after.get(k)}
                for k in set(before.keys()).union(after.keys())
                if before.get(k) != after.get(k)
            }
            details["changes"] = changes

        elif request.method == "DELETE":
            parts = request.path.split("/")
            deleted_id = next((p for p in parts if p.isdigit() or len(p) > 10), None)
            if deleted_id:
                details["deleted_id"] = deleted_id

        return details
