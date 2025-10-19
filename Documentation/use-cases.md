# 📘 **RCI Academic Portal – Final Use Case Summary (with Analytics)**

---

## **1. Student**

### **Core Use Cases**

* Enroll in a semester/school year (system validates prerequisites).
* View enrolled subjects and their details.

  * Can view syllabus (PDF download).
  * Can view subject summary or overview.
* View summary of grades:

  * Displays current and previous grades.
  * Includes *Incomplete (INC)* status if applicable.
  * Once INC is resolved, shows updated grade and signatories (Head / Professor / Registrar).
* View announcements and notifications from departments or registrar.

---

## **2. Registrar**

### **Core Use Cases**

* Manage student records (**Create, Read, Update, Delete**).
* Upload and store official student documents (linked to each student’s profile).
* Generate, verify, and archive official school documents (PDF certificates, COR, TOR, etc.).
* Verify and update student enrollment statuses (enrolled, LOA, dropped, graduated).
* View **Registrar Analytics**, including:

  * Enrollment data per program or term.
  * Grade distributions and trends.
  * Student performance summaries.

---

## **3. Admission**

### **Core Use Cases**

* Accept or deny student applications.
* Verify applicant requirements and uploaded documents.
* Manage applicant records (CRUD and queue management).
* View **Admission Analytics**, including:

  * Total applications vs. accepted/rejected counts.
  * Application trends over time.
  * Conversion rate (applicants → enrolled students).

---

## **4. Head (Dean / Department Head)**

### **Core Use Cases**

* Manage professors (CRUD functions).
* Assign professors to specific sections.
* Manage subjects (CRUD) and update syllabi.
* Add or modify subject summaries and learning outcomes.
* View **Department Analytics**, including:

  * Faculty loads (teaching assignments).
  * Pass/fail rates within the department.
  * Subject or course performance metrics.

---

## **5. Professor / Teacher**

### **Core Use Cases**

* View assigned subjects and related syllabi.
* Encode and update final grades of enrolled students.
* View list of students in their sections.
* View **Professor Analytics**, including:

  * Grade distribution per subject/section.
  * Class performance overview.
  * Pass–Fail rate visualization for personal classes.

---

## **6. Admin**

### **Core Use Cases**

* Manage academic programs, sections, and system-wide settings.
* Manage curriculum under each department or sector.
* Assign or modify user roles and permissions across the system.
* Configure academic year and semester settings.
* View **Full Analytics Dashboard** covering:

  * Enrollment, grades, admission, and faculty data.
  * System logs and usage reports.
  * Organization-wide performance metrics.

---

## **7. Analytics (Global Use Case)**

### **Core Use Cases**

* Generate **dashboards and visual reports** (graphs, charts, data tables).
* Access specialized analytics modules:

  * Enrollment Analytics
  * Grades Analytics
  * Admission Analytics
  * Faculty Analytics
* Filter results by **semester, academic year, program, course, or section**.
* Export reports as **CSV or PDF** files.
* Role-based access control:

  * **Admin:** Full access to all analytics data.
  * **Head:** Access limited to their department analytics.
  * **Registrar:** Access to enrollment and grades data.
  * **Professor:** Access to analytics for their assigned classes only.

---
