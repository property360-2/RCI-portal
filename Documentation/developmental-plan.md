# 🛠 Developmental Plan – RCI Academic Portal (Django + React)

---

## **Phase 1: Planning & Database Setup**

**Goal:** Lay the foundation with requirements, ERD, and DB schema.

### Project Management – **Jun**

* [x] Finalize system requirements & user roles.
* [x] Setup GitHub repository & workflow.
* [x] Create ERD with full relationships (see schema.md).

### Backend – **Kirt**

* [x] Initialize sqlite database. (soon postgresql)
* [x] Implement schema in Django models (`models.py`).
* [x] Run migrations (`makemigrations`, `migrate`).
* [x] Seed sample data (programs, test users, dummy enrollments).

**Status:** 🚧 Not Started

---

## **Phase 2: Backend Foundations (Django + DRF)**

**Goal:** Create the API layer and secure it.

### Backend – **Kirt**

* [x] Initialize Django project & core apps.
* [x] Install & configure **Django REST Framework (DRF)**.
* [x] Implement JWT authentication.
* [x] Setup role-based permissions (middleware).
* [x] Add AuditLog middleware (auto-record CRUD).

### API Testing – **Yasmien**

* [ ] Test endpoints in Postman (CRUD + auth).

**Status:** 🚧 Not Started

---

## **Phase 3: Frontend Foundations (React + Tailwind)**

**Goal:** Setup UI skeleton and connect to API.

### Frontend – **Joshua**

* [ ] Initialize React project (Vite).
* [ ] Setup Tailwind + shadcn/ui components.
* [ ] Build login page + role-based dashboard routing.
* [ ] Create protected routes.

### API Integration – **Edjohn**

* [ ] Install dependencies (`axios`, `zustand`, etc.).
* [ ] Implement global auth state (JWT store in Zustand).
* [ ] Connect login/register with backend API.

### Component Design & Reusables – **Marjorie**

* [ ] Build reusable UI components: buttons, cards, inputs, modals.
* [ ] Ensure design consistency across all modules.
* [ ] Setup responsive breakpoints for mobile/tablet/desktop.
* [ ] Implement wireframes for dashboard and module layouts.
* [ ] Document component usage for other frontend members.

### Optimization – **Aira**

* [ ] Organize folder structure.
* [ ] Support component integration & small reusable tweaks.

**Status:** 🚧 Not Started

---

## **Phase 4: Core Academic Modules**

**Goal:** Implement base features for enrollment and academic records.

### Student Module – **Joshua**

* [ ] Profile & program view.
* [ ] Enroll (prereq validation).
* [ ] View enrolled subjects & syllabus.

### Admission & Head Modules – **Mary Ann**

* [ ] Applicant registration (forms + requirements upload).
* [ ] Accept / reject applications.
* [ ] Application status tracking.
* [ ] CRUD subjects & assign professors (previously Marjorie’s tasks).

### Backend APIs – **Kirt**

* [ ] Support endpoints for Student, Admission, Head modules.

### Testing – **Yasmien**

* [ ] Verify enrollment and admin flows.

**Deliverable:** Enrollment & admission demo + sample data.

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

### UI/UX Lead – **Marjorie**

* [ ] Review and improve all frontend layouts & forms.
* [ ] Ensure mobile-first responsiveness & accessibility (ARIA, keyboard nav).
* [ ] Add Framer Motion animations to dashboards & components.
* [ ] Polish overall user experience: colors, spacing, consistency.
* [ ] Collaborate with Aira for TanStack Query optimization & component reuse.

### Optimization – **Aira**

* [ ] Optimize API calls & caching.
* [ ] Memoize heavy components.

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
