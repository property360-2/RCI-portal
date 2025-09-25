
# RCI Academic Portal — Full Concept Plan

## 1) Project Summary (elevator pitch)

RCI Academic Portal is a centralized Student Information & Academic Management System that handles enrollment, curriculum, grading, document management, and analytics for RCI. It ensures valid enrollment (prerequisite checks), official record keeping, document generation, and data-driven dashboards for admins, heads, registrars, and professors.

---

## 2) Main Goals

* Provide reliable enrollment workflow with prerequisite enforcement.
* Maintain accurate academic records (grades, transcripts, INC handling).
* Digitally store & generate official documents (PDFs).
* Give role-based access & permission-controlled functions.
* Provide actionable analytics & exportable reports.
<!-- * Be easy to deploy and maintain within 4 months MVP timeline.  i dont know the time for the scope as of now-->

---

## 3) Core Modules (what to build)

1. **Authentication & Authorization**

   * Role-based accounts (Student, Professor, Head, Registrar, Admission, Admin).
   * Session management and password reset.
2. **Student Profile & Registry**

   * Personal data, academic history, uploaded documents.
3. **Curriculum & Subjects**

   * Programs, curriculum templates (by year/term), subjects, prerequisites.
4. **Enrollment Module**

   * Enrollment workflow (apply, validate prereqs, section assignment).
   * Enrollment status history, overrides (admin/head).
5. **Gradebook & Academic Records**

   * Professors submit/modify grades, INC workflow, signatory tracking.
   * Registrar official records, transcript generation.
6. **Admission Module**

   * Applicant intake, requirements upload/verification, acceptance flow.
7. **Document Management**

   * Upload, link, archive PDFs; generate certificates, enrollment verifications.
8. **Academic Management**

   * CRUD: Professors, Subjects, Syllabus (upload PDF), Sections.
9. **Analytics & Reporting**

   * Enrollment trends, grade distributions, admission stats, faculty load.
   * Filtering and export (CSV/PDF).
10. **Notifications & Announcements**

    * System-wide notices, student/professional notifications.
11. **Audit Log & Activity Trail**

    * Track who changed grades, who approved INC, who issued docs.

---

## 4) Key Use Cases (short)

* Student: enroll, view syllabus & grades, see INC and signer info, view announcements.
* Registrar: manage records, upload/store docs, generate/archive PDFs, view limited analytics.
* Admission: manage applicants, verify docs, update status, view admission analytics.
* Head: manage faculty/subjects/syllabus, approve overrides, view departmental analytics.
* Professor: view syllabus, manage grades, view their class analytics.
* Admin: manage curriculum, roles, full analytics, system settings.

---

## 5) Data Model (entities overview)

* **Users** (id, name, role, email, passwordHash, profile)
* **Programs / Sectors** (e.g., BSIS)
* **Curriculum** (program_id, year_level, semester, subject entries)
* **Subjects** (code, title, units, prerequisites, syllabus_pdf, summary) ✅ tooltip/info for UI hover
* **Sections** (subject_id, term, schedule, room, professor_id)
* **Students** (user_id, student_number, status, program_id, year_level)
* **Enrollments** (student_id, section_id, term, status, timestamp)
* **Grades** (student_id, subject_id, section_id, grade, status, encoded_by, signed_by)
* **Applications** (applicant info, uploaded_requirements, status)
* **Documents** (student_id, doc_type, pdf_path, uploaded_by, timestamp)
* **AuditLog** (entity, action, user_id, details, timestamp)


---

## 6) Important Workflows

### Enrollment (student)

1. Student selects term & subjects.
2. System checks prerequisites and holds invalid subjects.
3. Student confirms and submits enrollment.
4. Registrar/Auto processes enrollment -> assigns section.
5. Enrollment status saved and visible in student profile.

### Grade/Incompletes

1. Professor encodes final grade.
2. If INC -> grade marked INC with resolution steps.
3. When resolved, head/prof/registrar signs off; system records who changed and when.
4. Registrar finalizes record.

### Document generation

* Registrar fills form → system generates PDF (enrollment cert, transcript stub) → store in Documents linked to student → downloadable / printable.

### Analytics

* ETL/aggregate nightly (or real-time queries for small data).
* Dashboards: filters by term, program, section, professor.
* Export options and scheduleable reports.

---

## 7) Roles & Permissions (high-level)

* Admin: full access, manage roles, system config.
* Head: manage dept data, approve overrides, department analytics.
* Registrar: student records, docs, verify enrollment, partial analytics.
* Admission: applicant flows, applicant analytics.
* Professor: manage grades for assigned sections, view class analytics.
* Student: enroll, view grades/syllabus/docs.

---

## 8) Non-functional Requirements

* Security: HTTPS, password hashing, input validation, RBAC.
* Performance: responsive dashboard, reasonable query times (<2s for main views).
* Scalability: modular design, DB indexes for queries.
* Backup: daily DB backups + file storage snapshots.
* Accessibility: basic WCAG-friendly UI (forms readable).
* Auditability: full change logs for academic records.

---


## 9) Tech Stack (Finalized)

* **Frontend:** React vite tsx.
* **UI:** Tailwind CSS (clean styling), ShadCN components.
* **Backend:** Django (Python) with Django REST Framework (DRF) for APIs.
* **Database:** PostgreSQL (recommended) or MySQL(depends parin sa school), sqlite muna for better good.
* **File Storage:** Local server storage (since WiFi hosting), with option to switch to S3/MinIO later.
* **Auth:** Django’s built-in auth + JWT for React frontend integration.
* **Reporting/Analytics:** SQL queries + Django ORM aggregations, visualized with Recharts/Chart.js in React.
* **Hosting:** Local server on LAN/WiFi (using Django’s runserver or Apache/Nginx + WSGI).

  * Students/faculty connect via the same WiFi network.
  <!-- * (Optional later) Cloud/VPS deployment for remote access. pero malabo HAHAHA  -->
* **DevOps:** GitHub for version control, GitHub Actions.

---


## 10) MVP Scope

**Must-have (MVP):**

* Auth & role management.
* Student profile & student enrollments (prereq checks).
* Curriculum + subject + section CRUD.
* Professor grade entry + INC handling with signature tracking.
* Registrar record management + PDF generation for 1-2 doc types.
* Basic analytics: enrollment counts, grade distribution (per subject).
* Audit logs.
* Simple, usable UI and documentation for demo.

**Stretch (if time):**

* Admission module complete.
* Advanced analytics with export & filters.
* Notifications & scheduler.
* Multi-term historical reports.
* Mobile-friendly polish.

---

## 12) QA & Testing

* Unit tests for critical backend logic (prereq check, grade calc).
* Integration tests for enrollment & grade workflows.
* Manual acceptance tests for each role.
* UAT session with sample users (classmates) one week before demo.

