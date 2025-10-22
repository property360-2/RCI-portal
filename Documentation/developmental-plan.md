# 🛠 Developmental Plan – RCI Academic Portal (Django + React)

---

## **Phase 1: Planning & Database Setup** ✅

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

**Status:** ✅ **Completed**

---

## **Phase 2: Backend Foundations (Django + DRF)** ✅

**Goal:** Create the API layer and secure it.

### Backend – **Kirt**

* [x] Initialize Django project & core apps.
* [x] Install & configure **Django REST Framework (DRF)**.
* [x] Implement JWT authentication.
* [x] Setup role-based permissions (middleware).
* [x] Add AuditLog middleware (auto-record CRUD).

### API Testing – **Yasmien**

* [x] Test endpoints in Postman (CRUD + auth).

**Status:** ✅ **Completed**

---

## **Phase 3: Frontend Foundations (React + Tailwind)** ✅

**Goal:** Setup UI skeleton and connect to API.

### Frontend – **Joshua**

* [x] Initialize React project (Vite).
* [x] Setup Tailwind + shadcn/ui components.
* [x] Build login page + role-based dashboard routing.
* [x] Create protected routes.

### API Integration – **Edjohn**

* [x] Install dependencies (`axios`, `zustand`, etc.).
* [x] Implement global auth state (JWT store in Zustand).
* [x] Connect login/register with backend API.

### Component Design & Reusables – **Joshua and Edjohn**

* [x] Build reusable UI components: buttons, cards, inputs, modals.
* [x] Ensure design consistency across all modules.
* [x] Setup responsive breakpoints for mobile/tablet/desktop.
* [x] Implement wireframes for dashboard and module layouts.
* [x] Document component usage for other frontend members.

### Optimization – **Aira**

* [x] Organize folder structure.
* [x] Support component integration & small reusable tweaks.

**Status:** ✅ **Completed**

---

## **Phase 4 (REVISED): Enrollment Logic & INC Resolution Workflow** 🚨

**Goal:** Implement intelligent enrollment with prerequisite validation, INC blocking, and approval chain visibility.

**Deadline:** **October 27, 2025** 

⚠️ **CRITICAL NOTES:**
- **Enrollment UI must be inside the Admission module** (accessible after Admission officer logs in)
- **Use the Documents table to store user credentials/requirements** (not a separate table)
- **Always refer to the documentation** (concept-plan.md, schema.md, pages-to-implement.md, use-cases.md) for accuracy

---

### **4.1 Admission Module – Smart Enrollment UI with Auto Account Creation**

**Owner:** Mary Ann (Frontend) + Kirt (Backend)

#### **⚠️ IMPORTANT IMPLEMENTATION NOTES:**

- **The enrollment functionality is part of the Admission module UI**, not a separate module
- Admission officers will handle the enrollment process for students
- Use the **Documents table** to store uploaded requirements/credentials (see schema.md)
- Refer to **pages-to-implement.md Section 3.2** for the expected UI structure

#### **Tasks:**

* [ ] **Student Account Auto-Generation**
  - System automatically creates user account upon enrollment:
    - **Username format:** First letter of first name + Full surname (e.g., "jdelacruz" for Juan Dela Cruz)
    - **Password:** Auto-generated student number (e.g., "2025-0001")
  - Store in Users table with role="student"
  - Student receives credentials (displayed in confirmation screen, can be printed/emailed)
  - Backend API:
    - `POST /api/students/create-account/` → auto-generates username and student number

* [ ] **Two-Step Enrollment Confirmation Process**
  
  **Step 1: Fill Enrollment Form**
  - Form fields:
    - Student personal information (name, email, birthdate, etc.)
    - Program selection (dropdown)
    - Year level (dropdown: 1st, 2nd, 3rd, 4th)
    - Semester (dropdown: 1st, 2nd, Summer)
    <!-- - Upload requirements (Documents table: Birth Certificate, Form 137, ID Photo, etc.) wala pa to, maybe soon -->
    - refer to the document sent by sir in the ojt gc
  - Button: **"Continue"** → proceeds to Step 2

  **Step 2: Confirmation & Final Submission**
  - Display summary of all entered data:
    - Student information review
    - Selected program and year level
    - List of enrolled subjects (auto-generated based on year/sem)
    - Uploaded documents list
  - **⚠️ Warning/Danger Alert Box:**
    ```
    ⚠️ WARNING: Please verify all information carefully.
    
    Are you sure the data you're about to submit to the system is accurate?
    Once submitted, this will create a permanent student record.
    
    Auto-generated credentials/ student can edit it if they want custom username and password:
    Username: [jdelacruz]
    Password: [2025-0001] (Student Number)
    
    [✓] I confirm that all information is accurate and correct.
    ```
  - Checkbox: Must check before final submission
  - Buttons: **"Go Back"** (edit form) | **"Confirm & Submit"** (finalize enrollment)

* [ ] **Block Enrollment for 1st Year, 1st Semester**
  - Auto-enroll students in pre-assigned block sections (no validation).
  - UI: Simple confirmation screen with enrolled subjects list.
  - **Location:** Inside Admission dashboard → "Enroll Student" section
  
* [ ] **Smart Enrollment (2nd Semester onwards)**
  - Generate recommended subjects based on:
    - Completed prerequisites
    - Current curriculum (year level + program)
  - Block subjects if:
    - ❌ Prerequisite not completed (failed or not taken)
    - ❌ Student has unresolved INC in any previous subject
  - UI Components (inside Admission module):
    - **✅ Recommended Subjects Card** (eligible to enroll)
    - **🔒 Blocked Subjects Card** (with tooltip explaining reason: "Prerequisite [CODE] not completed" or "Resolve INC in [SUBJECT] first")
    - **Manual Add Subject Option** (with validation)

* [ ] **Student Credentials/Requirements Storage**
  - Use **Documents table** to store uploaded requirements
  - Fields to populate:
    - `student_id` (FK to Students)
    - `doc_type` (e.g., "Birth Certificate", "Form 137", "ID Photo", "enrollment form")
    - `file_path` (local server storage path)
    - `uploaded_by` (admission officer's user_id)
  - UI: File upload component with document type dropdown

* [ ] **Enrollment Approval Chain Visibility (Student Side)**
  - Show enrollment status: ⏳ Pending / ✅ Approved / ❌ Rejected
  - Student can view this in their own dashboard (Joshua's task)

#### **Backend API (Kirt):**
* [ ] `POST /api/students/create-account/` → auto-generates username (first letter + surname) and student number
* [ ] `GET /api/enrollment/recommended/{student_id}/` → returns eligible subjects
* [ ] `POST /api/enrollment/validate/` → validates prerequisites + INC status
* [ ] `POST /api/enrollment/submit/` → submits enrollment with two-step confirmation
* [ ] `POST /api/documents/` → stores uploaded requirements (use Documents table from schema.md)

**📚 Reference:** 
- **schema.md** → Documents Table structure, Users Table, Students Table
- **pages-to-implement.md** → Section 3.2 (Student Account Creation / Enrollment Form)
- **use-cases.md** → Section 3 (Admission use cases)

---

### **4.2 Professor Module – Grade Encoding with Restricted Values & INC Resolution**

**Owner:** Edjohn (Frontend) + Kirt (Backend)

#### **⚠️ GRADE INPUT RESTRICTIONS:**
- Professors **CANNOT** manually type grades (no free-text input like 1.052, 1.36)
- Grades must be selected from **predefined dropdown values only:**
  - **Passing:** 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0
  - **Failing:** 5.0
  - **Incomplete:** INC

#### **Tasks:**

* [ ] **Grade Encoding with Dropdown Selection**
  - **Dropdown:** Pre-populated with valid grade values (1.0, 1.25, 1.5, ... 3.0, 5.0, INC)
  - **No manual text input allowed** (dropdown only)
  - If **INC** selected → modal with fields:
    - Reason (textarea)
    - Recommended action (textarea)
  - Store INC metadata in `Grades.signatories` JSON (as per schema.md):
    ```json
    {
      "status": "INC",
      "reason": "Missing final exam",
      "recommendation": "Complete exam by [date]",
      "professor_signed": "2025-10-22T14:30:00Z",
      "head_signed": null,
      "registrar_signed": null,
      "inc_created_date": "2025-10-22",
      "retake_deadline": "2026-04-22" // auto-calculated based on subject type
    }
    ```

* [ ] **INC Resolution Workflow**
  - Professor can resolve INC by selecting final grade from dropdown (same valid values)
  - After resolution:
    - Mark `professor_signed` timestamp
    - Status → **"Pending Registar Signature/Update"**
  - UI: 
    - **INC Badge** (🔴 orange ⏳)
    - **Resolve Button** → modal to select final grade (dropdown)
    - Show "Awaiting Head Approval" after submission

* [ ] **INC Auto-Retake Logic (Backend handles this):**
  - If INC not resolved within deadline:
    - **Major Subject:** 6 months after semester end
    - **Minor Subject:** 1 year after semester end
  - System auto-marks as "Retake Required"

#### **Backend API (Kirt):**
* [ ] `POST /api/grades/` → create grade (dropdown values only, with INC option)
* [ ] `PATCH /api/grades/{id}/resolve/` → resolve INC, update signatory chain (validate grade values)
* [ ] Add backend validation: reject any grade value not in approved list

**📚 Reference:** 
- **schema.md** → Grades Table (signatories field)
- **pages-to-implement.md** → Section 5.3 (Grades encoding)
- **use-cases.md** → Section 5 (Professor use cases)

---

### **4.3 Head Module – Subject Management (CRUD with Subject Type)**

**Owner:** Mary Ann (Frontend - for head UI) + Kirt (Backend)

#### **⚠️ ROLE RESTRICTION:**
- **ONLY Head/Dean** can perform subject management (CRUD)
- Head module does NOT have subject CRUD (only view)

#### **📝 UPDATED SCHEMA REQUIREMENT:**
**Add `subject_type` field to Subjects table:**
```sql
subject_type ENUM {'Major', 'Minor'} -- determines INC retake deadline
```

#### **Tasks:**

* [ ] **Subject Management (CRUD) - Head**
  - Create, Read, Update, Delete subjects
  - Fields:
    - Code (e.g., IT101)
    - Title (e.g., Introduction to Computing)
    - Units (e.g., 3)
    - **Subject Type (NEW!):** Dropdown - `Major` or `Minor`
    - Prerequisites (multi-select dropdown of existing subjects)
    - Syllabus PDF upload
    - Summary (textarea)
  - UI: Subjects table with filters (program, year level, subject type) + Add/Edit modal
  - **Prerequisite Multi-Select:** Dropdown showing existing subjects, can select multiple
  - **Subject Type Logic:**
    - If `Major` → INC retake deadline = 6 months
    - If `Minor` → INC retake deadline = 1 year

* [ ] **Year Standing/Level Integration**
  - Link subjects to curriculum (curriculum_id FK)
  - Display which year level the subject belongs to
  - Used in enrollment validation

#### **Backend API (Kirt):**
* [ ] Update Subjects model: Add `subject_type` field (ENUM: Major/Minor)
* [ ] `POST /api/subjects/` → create subject (head only - check role permission)
* [ ] `PATCH /api/subjects/{id}/` → update subject (including prerequisites array, subject_type)
* [ ] `DELETE /api/subjects/{id}/` → soft delete subject (head)
* [ ] Add role-based permission middleware: only `role=admin` can access these endpoints

**📚 Reference:** 
- **schema.md** → Subjects Table (UPDATE to add subject_type field)
- **pages-to-implement.md** → Section 6.2 (head Curriculum Management)
- **use-cases.md** → Section 6 (head use cases)

---

### **4.4 Head Module – INC Approval (No Subject CRUD)**

**Owner:** Mary Ann (Frontend) + Kirt (Backend)

#### **⚠️ ROLE CLARIFICATION:**
- Head **CANNOT** create/edit/delete subjects (head only)
- Head can only **view subjects** and **approve INC resolutions**

#### **Tasks:**

* [ ] **View Subjects (Read Only)**
  - Display subjects list for their department
  - Can view syllabus and subject details
  - **No CRUD buttons** (view only)

* [ ] **INC Approval Queue**
  - View INC grades resolved by professors (pending head approval)
  - Table columns:
    | Student Name | Subject Code | Subject Type | Professor | Resolved Grade | Date Resolved | Retake Deadline | Actions |
  - Show retake deadline (calculated from subject type)
  - Actions: ✅ Approve / ❌ Reject (with reason modal if rejecting)
  - After approval:
    - Mark `head_signed` timestamp
    - Status → **"Pending Registrar Approval"**

#### **Backend API (Kirt):**
* [ ] `GET /api/subjects/` → read-only for Head role (no POST/PATCH/DELETE access)
* [ ] `GET /api/grades/inc-pending-head/` → INC grades needing head approval
* [ ] `PATCH /api/grades/{id}/approve-head/` → head approves INC resolution

**📚 Reference:** 
- **pages-to-implement.md** → Section 4 (Head module - adjusted for view-only subjects)
- **use-cases.md** → Section 4 (Head use cases)

---

### **4.5 Registrar Module – Final INC Approval**

**Owner:** Aira (Frontend) + Kirt (Backend)

#### **Tasks:**

* [ ] **INC Final Approval**
  - View INC grades approved by Head (pending registrar finalization)
  - Table columns:
    | Student Name | Student No. | Subject Code | Subject Type | Grade | Professor | Head | Date | Retake Deadline | Actions |
  - Show checkmarks (✅) for professor and head signatures
  - Show retake deadline (auto-calculated)
  - Actions: ✅ Finalize / ❌ Reject (with reason)
  - After finalization:
    - Mark `registrar_signed` timestamp
    - Grade status: **INC** → **Passed/Failed** (based on grade value)

#### **Backend API (Kirt):**
* [ ] `GET /api/grades/inc-pending-registrar/` → INC grades needing registrar approval
* [ ] `PATCH /api/grades/{id}/finalize/` → registrar finalizes INC resolution

**📚 Reference:** 
- **schema.md** → Grades Table (status enum, signatories JSON)
- **pages-to-implement.md** → Section 2 (Registrar functions)
- **use-cases.md** → Section 2 (Registrar use cases)

---

### **4.6 Student Module – Profile Management, INC Visibility & Enrollment Blocker**

**Owner:** Joshua (Frontend) + Kirt (Backend)

#### **Tasks:**

* [ ] **Profile Settings - Change Username & Password**
  - Add "Profile Settings" page in student sidebar
  - Form fields:
    - Current Username (display only)
    - New Username (text input with validation)
    - Current Password (password input for verification)
    - New Password (password input)
    - Confirm New Password (password input)
  - Validation:
    - Username must be unique
    - Password must match confirmation
    - Must enter current password to change credentials
  - Button: **"Update Profile"** → success toast notification
  - Backend API:
    - `PATCH /api/users/{id}/update-credentials/` → update username/password with current password verification

* [ ] **Grades Page Enhancement**
  - Show INC approval chain with timeline:
    - ✅ Professor (Resolved on [date])
    - ⏳ Head (Pending Approval) OR ✅ Head (Approved on [date])
    - ⏳ Registrar (Pending Approval) OR ✅ Registrar (Approved on [date])
  - Display **Retake Deadline** for unresolved INC:
    - **Major Subject:** "⚠️ Retake required by [date] (6 months from INC creation)"
    - **Minor Subject:** "⚠️ Retake required by [date] (1 year from INC creation)"
  - Once fully resolved:
    - Grade updates to final numerical value
    - Badge: 🔴 INC → ✅ Passed (if 1.00-3.00) / ❌ Failed (if 5.00)
  - Show "View INC Details" button → opens modal with:
    - Reason for INC
    - Recommended action from professor
    - Approval timeline
    - Retake deadline (if applicable)

* [ ] **Enrollment Blocker Warning**
  - If student has unresolved INC:
    - Show prominent banner on dashboard:
      > ⚠️ **You cannot enroll in new subjects until INC in [Subject Code - Subject Name] is resolved.**
      > 
      > Retake Deadline: [Date]
    - Banner color: Red/Orange with alert icon
    - Link to "View INC Details" modal

* [ ] **View Auto-Generated Credentials (First Login Prompt)**
  - On first login (flag: `is_first_login` in Students table):
    - Show modal:
      ```
      Welcome to RCI Academic Portal!
      
      Your account has been created with these credentials:
      Username: [jdelacruz]
      Initial Password: [2025-0001] (Your Student Number)
      
      For security, please change your password in Profile Settings.
      
      [Go to Profile Settings] [Continue to Dashboard]
      ```

#### **Backend API (Kirt):**
* [ ] `PATCH /api/users/{id}/update-credentials/` → update username/password with verification
* [ ] Add `is_first_login` boolean field to Students table

**📚 Reference:** 
- **pages-to-implement.md** → Section 1.2 (Grades page with INC behavior), Section 1.1 (Dashboard)
- **use-cases.md** → Section 1 (Student use cases)

---

### **4.7 Testing & Bug Fixes**

**Owner:** Yasmien (QA Lead) + Marjorie (Documentation QA)

#### **Test Cases:**

* [ ] **Enrollment Logic**
  - Test two-step confirmation process (form fill → summary → warning → submit)
  - Test auto-account generation (username format, student number as password)
  - Test 1st year, 1st sem enrollment (block section, no validation)
  - Test 2nd sem onwards enrollment (prerequisite check works)
  - Test INC blocking (student with unresolved INC cannot enroll)
  - Test recommended subjects accuracy (matches curriculum + completed prereqs)
  - Test manual subject addition with validation
  - Test Documents table storage for uploaded requirements

* [ ] **Grade Input Restrictions**
  - Test that professors cannot manually type grades (dropdown only)
  - Test all valid grade values (1.0, 1.25, ... 3.0, 5.0)
  - Test INC selection and metadata storage
  - Test grade resolution with dropdown selection

* [ ] **INC Workflow with Retake Deadlines**
  - Professor creates INC → verify signatories JSON field + retake_deadline in database
  - Professor resolves INC → verify "Pending Head" status shows in UI
  - Head approves → verify "Pending Registrar" status updates
  - Registrar finalizes → verify grade value updates and status changes to Passed/Failed
  - Test retake deadline calculation:
    - Major subject INC → 6 months from creation
    - Minor subject INC → 1 year from creation
  - Test rejection flow (head/registrar rejects) → verify reason is stored

* [ ] **Subject Management (head Only)**
  - Test that only head can create/edit/delete subjects
  - Test Head cannot access subject CRUD (view only)
  - Head creates subject with prerequisites → should be blocked
  - head creates subject with subject_type (Major/Minor) → verify in DB
  - Verify prerequisite validation works in enrollment (blocked if prereq not met)
  - Verify syllabus upload/download functionality
  - Test subject summary display in student UI

* [ ] **Student Profile Management**
  - Test username change (must be unique)
  - Test password change (requires current password)
  - Test validation (password confirmation must match)
  - Test first login modal display
  - Test "Go to Profile Settings" redirect

* [ ] **Cross-Role Integration**
  - Admission enrolls student → auto-generates account → Student can login with credentials
  - Student logs in first time → sees welcome modal with credentials
  - Student changes password → can login with new password
  - Professor marks INC with subject_type → retake deadline auto-calculated
  - Head sees INC in approval queue with correct deadline
  - Registrar finalizes → Student sees updated grade with resolution timeline

**📚 Reference:** All documentation files for expected behavior validation

---

### **4.8 Documentation Alignment & Final Review**

**Owner:** Jun (Project Manager)

#### **Tasks:**

* [ ] **Pre-Testing Review (Oct 23-24)**
  - Ensure all team members have read relevant sections of documentation
  - Verify UI mockups match pages-to-implement.md descriptions
  - Confirm API endpoints match must-have-api.md specifications
  - **Update schema.md:** Add `subject_type` field to Subjects table
  - **Update schema.md:** Add `is_first_login` field to Students table

* [ ] **Testing Coordination (Oct 26)**
  - Coordinate with Yasmien and Marjorie for systematic testing
  - Prioritize critical path: Enrollment with 2-step confirmation → Auto account creation → INC Creation with retake logic → Approval Chain

* [ ] **Final Documentation Update (Oct 27)**
  - Update schema.md with new fields (subject_type, is_first_login)
  - Document two-step enrollment confirmation process
  - Document auto-account generation logic (username format, password)
  - Document grade input restrictions (dropdown only)
  - Document INC retake deadline calculation rules
  - Document role restrictions (head-only subject CRUD)
  - Document student profile management feature
  - Prepare demo script with sample data flow
  - Create quick reference guide for instructors

**📚 All Documentation Files Must Be Consulted Throughout Development**

---

## **Timeline Breakdown (Oct 22-27)**

| Date       | Focus Area                                           | Owners                  | Documentation Reference              |
|------------|------------------------------------------------------|-------------------------|--------------------------------------|
| **Oct 23** | Backend: Auto-account generation + Enrollment APIs   | Kirt                    | schema.md, must-have-api.md          |
| **Oct 23** | Backend: Update Subjects model (subject_type field)  | Kirt                    | schema.md                            |
| **Oct 23** | Frontend: Start 2-step Enrollment UI                 | Mary Ann                | pages-to-implement.md (Section 3)    |
| **Oct 24** | Frontend: Complete Enrollment UI + Grade dropdown    | Mary Ann + Edjohn       | pages-to-implement.md (Sections 3,5) |
| **Oct 25** | Frontend: head Subject CRUD + Head INC approval     | Mary Ann                | pages-to-implement.md (Sections 4,6) |
| **Oct 25** | Frontend: Registrar INC finalization                 | Aira                    | pages-to-implement.md (Section 2)    |
| **Oct 25** | Frontend: Student profile + INC visibility           | Joshua                  | pages-to-implement.md (Section 1)    |
| **Oct 26** | Integration testing + bug fixes                      | Yasmien + Marjorie      | All documentation files              |
| **Oct 27** | Final testing + documentation alignment + demo prep  | Jun + All               | All documentation files              |

---

## **Critical Success Factors**

1. **📚 ALWAYS REFER TO DOCUMENTATION:**
   - **concept-plan.md** → Overall system design
   - **schema.md** → Database structure (UPDATE with new fields!)
   - **pages-to-implement.md** → Exact UI requirements
   - **use-cases.md** → User workflows
   - **must-have-api.md** → API specifications

2. **Kirt (Backend):** Prioritize APIs in this order:
   - Auto-account generation (username format, student number password)
   - Two-step enrollment submission
   - Grade value validation (dropdown only)
   - Subject_type field implementation
   - INC retake deadline calculation
   - Documents table CRUD (for credentials storage)
   - Student profile update (username/password change)

3. **Frontend Team:** Work in parallel:
   - **Mary Ann:** 2-step enrollment UI (with confirmation & warning) + head subject CRUD
   - **Edjohn:** Professor grade dropdown (no manual input)
   - **Aira:** Registrar INC finalization
   - **Joshua:** Student profile settings + INC visibility + enrollment blocker

4. **Daily Check-ins:** 
   - Morning: Jun reviews progress against documentation
   - Evening: Quick sync to unblock issues

5. **Testing Strategy:**
   - **Yasmien:** Functional testing with sample data (Oct 26)
   - **Marjorie:** Documentation alignment testing (Oct 26-27)
   - Create test accounts:
     - head (for subject CRUD testing)
     - Admission officer (for enrollment testing)
     - Multiple students (various scenarios):
       - 1st year, 1st sem (block enrollment)
       - 2nd year with completed prereqs
       - Student with unresolved INC (major subject)
       - Student with unresolved INC (minor subject)
       - Student missing prerequisites

---

## **⚠️ KEY REMINDERS**

### **For Mary Ann (Admission UI + head UI):**
- Implement **TWO-STEP** enrollment: Form fill → Summary with WARNING → Submit
- Warning must include checkbox confirmation before allowing submission
- Display auto-generated credentials in confirmation screen
- **head subject CRUD:** Add subject_type dropdown (Major/Minor)
- Head module: subjects are **view-only** (no CRUD buttons)

### **For Edjohn (Professor UI):**
- Grade input MUST be **dropdown only** (no text input)
- Valid values: 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 5.0, INC
- Reject any manual typed values on frontend validation

### **For Joshua (Student UI):**
- Add "Profile Settings" page with username/password change
- Show first-login modal with auto-generated credentials
- Display INC retake deadlines based on subject type
- Enrollment blocker must show retake deadline

### **For Kirt (Backend):**
- **Username generation:** First letter + surname (e.g., "jdelacruz")
- **Password:** Student number (auto-generated)
- Update Subjects table: Add `subject_type` ENUM('Major', 'Minor')
- Update Students table: Add `is_first_login` BOOLEAN
- Grade validation: Only accept predefined values (reject others)
- INC retake deadline calculation:
  - Major: `inc_created_date + 6 months`
  - Minor: `inc_created_date + 1 year`
- Role-based permissions: Only head can POST/PATCH/DELETE subjects

### **For Everyone:**
- Read your assigned sections in documentation **BEFORE** coding
- When in doubt, check documentation first, then ask Jun
- Test against documentation specifications, not assumptions
- Update schema.md with new fields (Jun will coordinate)

---

## **📋 Schema Updates Required (Kirt + Jun)**

**Subjects Table - ADD:**
```sql
subject_type ENUM('Major', 'Minor') NOT NULL
```

**Students Table - ADD:**
```sql
is_first_login BOOLEAN DEFAULT TRUE
```

**Grades Table - UPDATE signatories JSON to include:**
```json
{
  "status": "INC",
  "reason": "...",
  "recommendation": "...",
  "professor_signed": "timestamp",
  "head_signed": null,
  "registrar_signed": null,
  "inc_created_date": "YYYY-MM-DD",
  "retake_deadline": "YYYY-MM-DD",  // auto-calculated
  "subject_type": "Major" or "Minor"
}
```

---

## **Post-October 27 (Future Phases)**

### **Phase 5: Analytics & Reporting**
### **Phase 6: UI/UX Optimization**
### **Phase 7: Final Testing & QA**
### **Phase 8: Deployment (LAN Hosting)**

---

**Let's build this with precision! 📚✨ Every detail matters! 🚀**