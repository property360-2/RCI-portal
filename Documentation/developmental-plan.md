# 🛠 Developmental Plan – RCI Academic Portal (Django + React)

---

## **Phase 1: Planning & Database Setup**

**Goal:** Lay the foundation with requirements, ERD, and DB schema.

### Project Management – **Jun**

* [X] Finalize system requirements & user roles.
* [X] Setup GitHub repository & workflow.
* [X] Create ERD with full relationships. nasa schema.md

### Backend – **Kirt**

* [ ] Initialize PostgreSQL database.
* [ ] Implement schema in Django models (`models.py`).
* [ ] Run migrations (`makemigrations`, `migrate`).
* [ ] Seed sample data (programs, test users, dummy enrollments).

**Status:** 🚧 Not Started

---

## **Phase 2: Backend Foundations (Django + DRF)**

**Goal:** Create the API layer and secure it.

### Backend – **Kirt**

* [ ] Initialize Django project & core apps.
* [ ] Install & configure **Django REST Framework (DRF)**.
* [ ] Implement JWT authentication.
* [ ] Setup role-based permissions (middleware).
* [ ] Add AuditLog middleware (auto-record CRUD).

### API Testing – **Yasmien**

* [ ] Test endpoints in Postman (CRUD + auth).

**Status:** 🚧 Not Started

---

## **Phase 3: Frontend Foundations (React + Tailwind)**

**Goal:** Setup UI skeleton and connect to API.

### Frontend – **Joshua & Marjorie**

* [ ] Initialize React project (Vite).
* [ ] Setup Tailwind + shadcn/ui components.
* [ ] Build login page + role-based dashboard routing.
* [ ] Create protected routes.

### API Integration – **Edjohn**

* [ ] Install dependencies (`axios`, `zustand`, etc.).
* [ ] Implement global auth state (JWT store in Zustand).
* [ ] Connect login/register with backend API.

### Optimization – **Aira**

* [ ] Organize folder structure.
* [ ] Setup reusable components (buttons, inputs, cards).

**Status:** 🚧 Not Started

---

## **Phase 4: Core Academic Modules**

**Goal:** Implement base features for enrollment and academic records.

### Student Module – **Joshua**

* [ ] Profile & program view.
* [ ] Enroll (prereq validation).
* [ ] View enrolled subjects & syllabus.

### Admission Module – **Mary Ann**

* [ ] Applicant registration (forms + requirements upload).
* [ ] Accept / reject applications.
* [ ] Application status tracking.

### Head Module – **Marjorie**

* [ ] CRUD subjects.
* [ ] CRUD professors + assign to sections.
* [ ] Update syllabus.

### Backend APIs – **Kirt**

* [ ] Support endpoints for Student, Admission, Head modules.

### Testing – **Yasmien**

* [ ] Verify enrollment flow works.

**Deliverable:** Enrollment demo + sample student data.
**Status:** 🚧 Not Started

---

## **Phase 5: Grades & Registrar**

**Goal:** Build grading + registrar functionality.

### Professor Module – **Edjohn**

* [ ] View section list.
* [ ] Encode / update student final grades.
* [ ] View analytics (per class).

### Registrar Module – **Aira**

* [ ] Manage student records (CRUD).
* [ ] Upload PDFs linked to student.
* [ ] Generate enrollment verification reports.

### Grades System – **Mary Ann**

* [ ] Handle INC workflow.
* [ ] Implement signatory flow (professor → head → registrar).

### Backend APIs – **Kirt**

* [ ] Endpoints for grade encoding & registrar workflows.

### Testing – **Yasmien**

* [ ] Test grade entry and registrar processes.

**Deliverable:** Grade entry + registrar demo.
**Status:** 🚧 Not Started

---

## **Phase 6: Analytics & Reporting**

**Goal:** Provide insights & dashboards.

### Backend – **Kirt**

* [ ] Create analytics endpoints with aggregates.

### Analytics Dashboards – **Mary Ann**

* [ ] Admin → full system analytics.
* [ ] Head → department analytics.
* [ ] Registrar → enrollment + grades.
* [ ] Professor → class distribution.

### Frontend Visualization – **Joshua**

* [ ] Build dashboards in React with Recharts.
* [ ] Export features (CSV, PDF).

### Testing – **Yasmien**

* [ ] Validate correctness of analytics data.

**Deliverable:** Analytics dashboard MVP.
**Status:** 🚧 Not Started

---

## **Phase 7: UI/UX Optimization**

**Goal:** Polish usability and performance.

### Optimization – **Aira**

* [ ] Optimize API calls & caching with TanStack Query.
* [ ] Memoize heavy components (tables, charts).
* [ ] Improve responsiveness (mobile-first).
* [ ] Add accessibility support.
* [ ] Polish dashboards & forms (Framer Motion, shadcn/ui).
* [ ] Error handling + toasts.

### Project Management – **Jun**

* [ ] Review all UI/UX improvements before merge.

**Status:** 🚧 Not Started

---

## **Phase 8: Testing & QA**

**Goal:** Ensure stability & correctness.

### QA – **Yasmien**

* [ ] Unit tests (Django + Pytest).
* [ ] API tests (Postman).
* [ ] React component & integration tests.
* [ ] End-to-end tests (Cypress).
* [ ] Security tests (RBAC, SQL injection).
* [ ] Load testing.

### Support – **Jun**

* [ ] Oversee bug fixing workflow.

**Status:** 🚧 Not Started

---

## **Phase 9: Deployment (LAN Hosting)**

**Goal:** Host the system for local WiFi access.

### Backend Deployment – **Kirt**

* [ ] Setup Django to run on LAN (`0.0.0.0:8000`).
* [ ] Configure Nginx/Django serving.
* [ ] Setup daily DB backups.

### Frontend Build – **Marjorie**

* [ ] Serve React build on LAN.

### Presentation Prep – **Jun**

* [ ] Demo dataset preparation.
* [ ] Final presentation deck.

**Deliverable:** MVP hosted on LAN + ready for defense.
**Status:** 🚧 Not Started

---
