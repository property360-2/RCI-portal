# 📘 Data Dictionary – RCI Academic Portal

---

### **1. Users Table**

| Field         | Type          | Description                                             |
| ------------- | ------------- | ------------------------------------------------------- |
| user_id (PK)  | UUID / Serial | Unique identifier for each user                         |
| username      | VARCHAR       | Login username                                          |
| password_hash | VARCHAR       | Encrypted password                                      |
| email         | VARCHAR       | User’s email address                                    |
| role          | ENUM          | {student, registrar, admission, head, professor, admin} |
| date_joined   | TIMESTAMP     | Account creation date                                   |
| is_active     | BOOLEAN       | Active/inactive flag                                    |

---

### **2. Programs Table**

| Field           | Type          | Description                         |
| --------------- | ------------- | ----------------------------------- |
| program_id (PK) | UUID / Serial | Unique program ID                   |
| program_code    | VARCHAR       | Short code (e.g., BSIS)             |
| program_name    | VARCHAR       | Full name of program                |
| department      | VARCHAR       | Department offering the program     |
| sector          | VARCHAR       | category of what sector is it under |

---

### **3. Curriculum Table**

| Field              | Type          | Description             |
| ------------------ | ------------- | ----------------------- |
| curriculum_id (PK) | UUID / Serial | Unique curriculum ID    |
| program_id (FK)    | UUID          | References Programs     |
| year_level         | INT           | Year level (1, 2, 3, 4) |
| semester           | ENUM          | {1st, 2nd, Summer}      |

---

### **4. Subjects Table**

| Field              | Type           | Description                               |
| ------------------ | -------------- | ----------------------------------------- |
| subject_id (PK)    | UUID / Serial  | Unique subject ID                         |
| code               | VARCHAR        | Subject code (e.g., IT101)                |
| title              | VARCHAR        | Subject name                              |
| units              | INT            | Number of units                           |
| prerequisites      | JSON / FK list | List of prerequisite subject_ids          |
| syllabus_pdf       | VARCHAR        | Path/URL to syllabus                      |
| curriculum_id (FK) | UUID           | References Curriculum                     |
| summary            | TEXT           | Short description ()                      |

---

### **5. Sections Table**

| Field            | Type          | Description                          |
| ---------------- | ------------- | ------------------------------------ |
| section_id (PK)  | UUID / Serial | Unique section ID                    |
| subject_id (FK)  | UUID          | References Subjects                  |
| term             | VARCHAR       | Academic term (e.g., 2024-2025-1st)  |
| schedule         | VARCHAR       | Schedule details (e.g., MWF 8-10 AM) |
| room             | VARCHAR       | Room assignment                      |
| professor_id(FK) | UUID          | References Users (role=professor)    |

---

### **6. Students Table**

| Field           | Type          | Description                         |
| --------------- | ------------- | ----------------------------------- |
| student_id (PK) | UUID / Serial | Unique student ID                   |
| user_id (FK)    | UUID          | References Users                    |
| student_number  | VARCHAR       | School student number               |
| status          | ENUM          | {enrolled, graduated, dropped, LOA} |
| program_id (FK) | UUID          | References Programs                 |
| year_level      | INT           | Current year level                  |

---

### **7. Enrollments Table**

| Field              | Type          | Description                  |
| ------------------ | ------------- | ---------------------------- |
| enrollment_id (PK) | UUID / Serial | Unique enrollment record     |
| student_id (FK)    | UUID          | References Students          |
| section_id (FK)    | UUID          | References Sections          |
| term               | VARCHAR       | Academic term                |
| status             | ENUM          | {pending, enrolled, dropped} |
| timestamp          | TIMESTAMP     | Enrollment date/time         |

---

### **8. Grades Table**

| Field           | Type          | Description                                          |
| --------------- | ------------- | ---------------------------------------------------- |
| grade_id (PK)   | UUID / Serial | Unique grade record                                  |
| student_id (FK) | UUID          | References Students                                  |
| subject_id (FK) | UUID          | References Subjects                                  |
| section_id (FK) | UUID          | References Sections                                  |
| grade           | DECIMAL(3,2)  | Grade (e.g., 1.75, 2.0)                              |
| status          | ENUM          | {Passed, Failed, INC}                                |
| encoded_by (FK) | UUID          | Professor (Users)                                    |
| signatories     | JSON          | Stores approvals per role (Registrar, Head, teacher) |

---

### **9. Applications Table**

| Field                 | Type           | Description                   |
| --------------------- | -------------- | ----------------------------- |
| application_id (PK)   | UUID / Serial  | Unique application record     |
| applicant_name        | VARCHAR        | Name of applicant             |
| email                 | VARCHAR        | Applicant email               |
| program_id (FK)       | UUID           | Desired program               |
| uploaded_requirements | JSON / FK list | References Documents          |
| status                | ENUM           | {Pending, Accepted, Rejected} |

---

### **10. Documents Table**

| Field            | Type          | Description               |
| ---------------- | ------------- | ------------------------- |
| document_id (PK) | UUID / Serial | Unique document ID        |
| student_id (FK)  | UUID          | References Students       |
| doc_type         | ENUM          | {TOR, COR, Diploma, etc.} |
| file_path        | VARCHAR       | Path/URL to stored file   |
| uploaded_by (FK) | UUID          | References Users          |
| timestamp        | TIMESTAMP     | Upload time               |

---

### **11. AuditLog Table**

| Field        | Type          | Description                         |
| ------------ | ------------- | ----------------------------------- |
| log_id (PK)  | UUID / Serial | Unique log entry                    |
| entity       | VARCHAR       | Affected entity/table               |
| action       | VARCHAR       | {CREATE, UPDATE, DELETE}            |
| user_id (FK) | UUID          | User who performed action           |
| details      | JSON          | Extra details (before/after values) |
| timestamp    | TIMESTAMP     | Action date/time                    |

---
