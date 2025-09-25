# 📌 Use Cases (Final Updated with Analytics)

### 1. **Student**

* Enroll in a semester/school year (checks prerequisites).
* View subjects enrolled.

  * Can view the subjects and syllabus (PDF).
* View summary of grades.

  * Can view grades, including INC.
  * If INC is resolved, system shows updated grade and who signed off (Head/Professor/Registrar).
* View announcements / notifications.

---

### 2. **Registrar**

* Manage student records (CRUD).
* Upload/store student documents (linked to student profile).
* Generate and archive official documents (PDF, certificates).
* Verify enrollment status.
* View analytics (enrollment data, grade distributions).

---

### 3. **Admission**

* Accept/deny applications.
* Verify requirements.
* Manage applicant records.
* View analytics (applications vs. accepted/rejected).

---

### 4. **Head (Dean / Department Head)**

* CRUD professors.
* Assign professors to sections.
* CRUD subjects.
* Update syllabus.
* View analytics (faculty loads, pass/fail rates in department).

---

### 5. **Professor / Teacher**

* View syllabus.
* Encode/change final grades.
* View students in their section.
* View analytics (grade distribution for their classes only).

---

### 6. **Admin**

* Manage curriculum under each sector.
* Manage programs, sections, and system-wide settings.
* Manage user roles and permissions.
* Full access to analytics dashboard (enrollment, grades, admission, faculty).

---

### 7. **Analytics (Global Use Case)**

* Generate dashboards & reports (graphs, charts).
* Enrollment Analytics, Grades Analytics, Admission Analytics, Faculty Analytics.
* Filter data by semester, program, course, section.
* Export analytics (CSV, PDF).
* Access depends on role:

  * Admin = all data.
  * Head = department only.
  * Registrar = enrollment/grades only.
  * Professor = their own classes.

---
