# 🛠 Developmental Plan – RCI Academic Portal (Django + React)

---

## **Phase 1: Planning & Database Setup**

**Goal:** Lay the foundation with requirements, ERD, and DB schema.

**Tasks:**

- [ ] Finalize system requirements & user roles (Student, Registrar, Admission, Head, Professor, Admin).
- [ ] Create ERD with full relationships (Users, Programs, Curriculum, Subjects, Sections, Students, Enrollments, Grades, Applications, Documents, AuditLog).
- [ ] Initialize PostgreSQL database.
- [ ] Implement schema in Django models (`models.py`).
- [ ] Run migrations (`makemigrations`, `migrate`).
- [ ] Seed sample data (programs, test users, dummy enrollments).
- [ ] Setup version control (GitHub repo).

**Status:** 🚧 Not Started

---

## **Phase 2: Backend Foundations (Django + DRF)**

**Goal:** Create the API layer and secure it.

**Tasks:**

- [ ] Initialize Django project & core apps/modules.
- [ ] Install & configure **Django REST Framework (DRF)**.
- [ ] Implement JWT authentication (djangorestframework-simplejwt).
- [ ] Setup role-based permissions (middleware).
- [ ] Create serializers & views for **Users, Programs, Subjects, Curriculum**.
- [ ] Add AuditLog middleware (auto-record CRUD).
- [ ] Test endpoints in Postman (CRUD + auth).

**Status:** 🚧 Not Started

---

## **Phase 3: Frontend Foundations (React + Tailwind)**

**Goal:** Setup UI skeleton and connect to API.

**Tasks:**

- [ ] Initialize React project (Vite).
- [ ] Install dependencies:

  - `react-router-dom` (routing)
  - `axios` (API calls)
  - `zustand` (state management)
  - `tailwindcss` (styling)
  - `react-hot-toast` (notifications)
  - `recharts` (analytics charts)
  - _(add more as needed, document where they’re used)_

- [ ] Setup Tailwind + shadcn/ui components.
- [ ] Implement global auth state (JWT store in Zustand).
- [ ] Build login page + role-based dashboard routing.
- [ ] Create protected routes (student, professor, admin, etc.).

**Status:** 🚧 Not Started

---

## **Phase 4: Core Academic Modules**

**Goal:** Implement base features for enrollment and academic records.

**Tasks:**

- [ ] **Student Module**

  - View profile, program, year level.
  - Enroll (prereq validation).
  - View enrolled subjects & syllabus.

- [ ] **Admission Module**

  - Applicant registration (forms + requirements upload).
  - Accept / reject applications.
  - Application status tracking.

- [ ] **Head Module**

  - CRUD subjects.
  - CRUD professors + assign to sections.
  - Update syllabus.

**Deliverable:** Enrollment demo + sample student data.

**Status:** 🚧 Not Started

---

## **Phase 5: Grades & Registrar**

**Goal:** Build grading + registrar functionality.

**Tasks:**

- [ ] **Professor Module**

  - View section list.
  - Encode / update student final grades.
  - View analytics (grade distribution per class).

- [ ] **Registrar Module**

  - Manage student records (CRUD).
  - Process documents (upload PDFs linked to student).
  - Generate reports (enrollment verification, transcript drafts).

- [ ] **Grades System**

  - Handle INC workflow.
  - Signatory flow (encoded_by professor, signed_by head/registrar).

**Deliverable:** Grade entry + registrar document demo.

**Status:** 🚧 Not Started

---

## **Phase 6: Analytics & Reporting**

**Goal:** Provide insights & dashboards.

**Tasks:**

- [ ] Create analytics endpoints in Django (aggregate queries).
- [ ] Role-based access:

  - Admin → full system analytics.
  - Head → department analytics.
  - Registrar → enrollment + grade summaries.
  - Professor → own class grade distribution.

- [ ] Build dashboards in React with Recharts.
- [ ] Export features (CSV, PDF).

**Deliverable:** Analytics dashboard MVP.

**Status:** 🚧 Not Started

---

## **Phase 7: UI/UX Optimization (Frontend Efficiency)**

**Goal:** Polish usability and performance before QA.

**Tasks:**

- [ ] Optimize API calls & caching with **TanStack Query** (stale-while-revalidate(loading), background updates).
- [ ] Memoize only UI-heavy components (tables, charts) with `React.memo` if needed.
- [ ] Improve responsiveness (mobile-first adjustments with Tailwind).
- [ ] Add accessibility support (labels, ARIA roles, keyboard navigation).
- [ ] Polish dashboards & forms (animations with Framer Motion, shadcn/ui refinements).
- [ ] Enhance error handling + toasts for better UX.

**Status:** 🚧 Not Started

---

## **Phase 8: Testing & QA**

**Goal:** Ensure system stability and correctness.

**Tasks:**

- [ ] Unit tests (Django + Pytest).
- [ ] API tests (Postman collections).
- [ ] React component & integration tests (Jest + React Testing Library).
- [ ] End-to-end tests (Cypress).
- [ ] Security tests (RBAC enforcement, SQL injection prevention).
- [ ] Load testing (simulate multiple students enrolling).

**Status:** 🚧 Not Started

---

## **Phase 9: Deployment (LAN Hosting)**

**Goal:** Host the system for local WiFi access.

**Tasks:**

- [ ] Setup Django to run on LAN (`0.0.0.0:8000`).
- [ ] Serve React frontend build via Django or Nginx.
- [ ] Ensure all team members can access system over WiFi.
- [ ] Setup daily DB backups (cron or pg_dump).
- [ ] Prepare presentation + demo dataset.

**Deliverable:** MVP hosted on LAN + ready for final defense.

**Status:** 🚧 Not Started

---
