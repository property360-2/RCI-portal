# 📡 RCI Academic Portal – API Endpoints

---

## **1. Authentication**

| Method | Endpoint             | Request Body             | Response Summary           |
| ------ | -------------------- | ------------------------ | -------------------------- |
| POST   | `/api/auth/login/`   | `{ username, password }` | `{ token, refresh, user }` |
| POST   | `/api/auth/refresh/` | `{ refresh }`            | `{ token }`                |
| POST   | `/api/auth/logout/`  | `{}`                     | `{ success: true }`        |

---

## **2. Users**

| Method | Endpoint           | Request Body                          | Response Summary    |
| ------ | ------------------ | ------------------------------------- | ------------------- |
| GET    | `/api/users/`      | -                                     | List of all users   |
| GET    | `/api/users/{id}/` | -                                     | User details by ID  |
| POST   | `/api/users/`      | `{ username, email, password, role }` | Newly created user  |
| PATCH  | `/api/users/{id}/` | `{ email?, role?, is_active? }`       | Updated user        |
| DELETE | `/api/users/{id}/` | -                                     | `{ success: true }` |

---

## **3. Programs**

| Method | Endpoint              | Request Body                                 | Response Summary    |
| ------ | --------------------- | -------------------------------------------- | ------------------- |
| GET    | `/api/programs/`      | -                                            | List of programs    |
| GET    | `/api/programs/{id}/` | -                                            | Program details     |
| POST   | `/api/programs/`      | `{ program_code, program_name, department }` | Created program     |
| PATCH  | `/api/programs/{id}/` | `{ program_name?, department? }`             | Updated program     |
| DELETE | `/api/programs/{id}/` | -                                            | `{ success: true }` |

---

## **4. Curriculum**

| Method | Endpoint                | Request Body                                       | Response Summary    |
| ------ | ----------------------- | -------------------------------------------------- | ------------------- |
| GET    | `/api/curriculum/`      | -                                                  | List of curricula   |
| GET    | `/api/curriculum/{id}/` | -                                                  | Curriculum details  |
| POST   | `/api/curriculum/`      | `{ program_id, year_level, semester, subjects[] }` | New curriculum      |
| PATCH  | `/api/curriculum/{id}/` | `{ subjects? }`                                    | Updated curriculum  |
| DELETE | `/api/curriculum/{id}/` | -                                                  | `{ success: true }` |

---

## **5. Subjects**

| Method | Endpoint              | Request Body                                                                    | Response Summary    |
| ------ | --------------------- | ------------------------------------------------------------------------------- | ------------------- |
| GET    | `/api/subjects/`      | -                                                                               | List of subjects    |
| GET    | `/api/subjects/{id}/` | -                                                                               | Subject details     |
| POST   | `/api/subjects/`      | `{ code, title, units, prerequisites[], syllabus_pdf, curriculum_id, summary }` | Created subject     |
| PATCH  | `/api/subjects/{id}/` | `{ title?, units?, prerequisites?, syllabus_pdf?, summary? }`                   | Updated subject     |
| DELETE | `/api/subjects/{id}/` | -                                                                               | `{ success: true }` |

---

## **6. Sections**

| Method | Endpoint              | Request Body                                         | Response Summary    |
| ------ | --------------------- | ---------------------------------------------------- | ------------------- |
| GET    | `/api/sections/`      | -                                                    | List of sections    |
| GET    | `/api/sections/{id}/` | -                                                    | Section details     |
| POST   | `/api/sections/`      | `{ subject_id, term, schedule, room, professor_id }` | New section         |
| PATCH  | `/api/sections/{id}/` | `{ term?, schedule?, room?, professor_id? }`         | Updated section     |
| DELETE | `/api/sections/{id}/` | -                                                    | `{ success: true }` |

---

## **7. Students**

| Method | Endpoint              | Request Body                                                  | Response Summary    |
| ------ | --------------------- | ------------------------------------------------------------- | ------------------- |
| GET    | `/api/students/`      | -                                                             | List of students    |
| GET    | `/api/students/{id}/` | -                                                             | Student details     |
| POST   | `/api/students/`      | `{ user_id, student_number, status, program_id, year_level }` | New student record  |
| PATCH  | `/api/students/{id}/` | `{ status?, year_level? }`                                    | Updated student     |
| DELETE | `/api/students/{id}/` | -                                                             | `{ success: true }` |

---

## **8. Enrollments**

| Method | Endpoint                 | Request Body                               | Response Summary    |
| ------ | ------------------------ | ------------------------------------------ | ------------------- |
| GET    | `/api/enrollments/`      | -                                          | List of enrollments |
| GET    | `/api/enrollments/{id}/` | -                                          | Enrollment details  |
| POST   | `/api/enrollments/`      | `{ student_id, section_id, term, status }` | New enrollment      |
| PATCH  | `/api/enrollments/{id}/` | `{ status? }`                              | Updated enrollment  |
| DELETE | `/api/enrollments/{id}/` | -                                          | `{ success: true }` |

---

## **9. Grades**

| Method | Endpoint            | Request Body                                                                       | Response Summary    |
| ------ | ------------------- | ---------------------------------------------------------------------------------- | ------------------- |
| GET    | `/api/grades/`      | -                                                                                  | List of grades      |
| GET    | `/api/grades/{id}/` | -                                                                                  | Grade details       |
| POST   | `/api/grades/`      | `{ student_id, subject_id, section_id, grade, status, encoded_by, signatories{} }` | New grade           |
| PATCH  | `/api/grades/{id}/` | `{ grade?, status?, signatories? }`                                                | Updated grade       |
| DELETE | `/api/grades/{id}/` | -                                                                                  | `{ success: true }` |

---

## **10. Applications**

| Method | Endpoint                  | Request Body                                                             | Response Summary     |
| ------ | ------------------------- | ------------------------------------------------------------------------ | -------------------- |
| GET    | `/api/applications/`      | -                                                                        | List of applications |
| GET    | `/api/applications/{id}/` | -                                                                        | Application details  |
| POST   | `/api/applications/`      | `{ applicant_name, email, program_id, uploaded_requirements[], status }` | New application      |
| PATCH  | `/api/applications/{id}/` | `{ status? }`                                                            | Updated application  |
| DELETE | `/api/applications/{id}/` | -                                                                        | `{ success: true }`  |

---

## **11. Documents**

| Method | Endpoint               | Request Body                                       | Response Summary    |
| ------ | ---------------------- | -------------------------------------------------- | ------------------- |
| GET    | `/api/documents/`      | -                                                  | List of documents   |
| GET    | `/api/documents/{id}/` | -                                                  | Document details    |
| POST   | `/api/documents/`      | `{ student_id, doc_type, file_path, uploaded_by }` | New document        |
| PATCH  | `/api/documents/{id}/` | `{ doc_type?, file_path? }`                        | Updated document    |
| DELETE | `/api/documents/{id}/` | -                                                  | `{ success: true }` |

---

## **12. AuditLog**

| Method | Endpoint              | Request Body                             | Response Summary    |
| ------ | --------------------- | ---------------------------------------- | ------------------- |
| GET    | `/api/auditlog/`      | -                                        | List of log entries |
| GET    | `/api/auditlog/{id}/` | -                                        | Log details         |
| POST   | `/api/auditlog/`      | `{ entity, action, user_id, details{} }` | New log entry       |
| DELETE | `/api/auditlog/{id}/` | -                                        | `{ success: true }` |

---

