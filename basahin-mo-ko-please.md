# Team Notes — RCI Academic Portal

**Last updated:** September 27, 2025

---

## Purpose

This document contains the team roster, responsibilities, Git workflow, and simple onboarding notes for the RCI Academic Portal project. Keep this file as the single source of truth for team assignments and basic rules.


## Team Roster (Updated)

| Name     | Email                                                                   | GitHub                | Role / Primary Responsibility                                                                          | Notes                                          |
| -------- | ----------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| Joshua   | [delaralloydjoshua4@gmail.com](mailto:delaralloydjoshua4@gmail.com)     | Invited on GitHub     | Frontend Lead — HTML/CSS/JS, set up React Vite + Tailwind, base UI & layout                            | Guide other frontend members                   |
| Aira     | [lucasairakelly@gmail.com](mailto:lucasairakelly@gmail.com)             | No GitHub account yet | Frontend — Student UI (Enrollment, Profile, Grades)                                                    | Learn React/Tailwind; work with Joshua         |
| Yasmien  | [yasmientapang202418@gmail.com](mailto:yasmientapang202418@gmail.com)   | No GitHub account yet | QA / Testing — API & UI test plans, Postman collections, manual test reports                           | Report bugs to Jun and assignees               |
| Mary Ann | [maryannlachicalumjod@gmail.com](mailto:maryannlachicalumjod@gmail.com) | No GitHub account yet | Frontend preferred (HTML/CSS, Kotlin experience), can help backend if needed — Registrar UI, Documents | Can help gym membership mini-feature if needed |
| Kirt     | [kmaghinang57@gmail.com](mailto:kmaghinang57@gmail.com)                 | No GitHub account yet | Backend Lead — Django + DRF, models, auth (JWT), file uploads, core APIs                               | Set up Django apps & DB seed data              |
| Edjohn   | Edjohngamaay28@gmailcom                                                 | No GitHub account yet | Frontend — Professor UI (grade encoding, section view)                                                 | Coordinate with Kirt for API contracts         |
| Marjorie | (TBD)                                                                   | No GitHub account yet | **UI/UX Lead** — wireframes, responsive layouts, component design, improve frontend usability          | Supports all frontend members                  |
| Jun      | [junalvior21@gmail.com](mailto:junalvior21@gmail.com)                   | Repository owner      | Project Manager — PR reviews, documentation owner, progress checks                                     | Approves PRs into `main`                       |

---

> **Note:** GitHub invites have been sent to Joshua and the repository is owned by Jun. Everyone without a GitHub account should create one and share their username so they can be invited.

---

## Responsibilities (short)

* **Jun (PM):** approve PRs, maintain docs, run weekly progress check-ins.
* **Joshua:** initialize frontend project, create base components and shared layout.
* **Kirt:** initialize Django project, create core apps (`users`, `students`, `enrollment`, `grades`, `documents`, `analytics`).
* **Frontend members (Aira, Mary Ann, Edjohn, Marjorie):** implement assigned UIs, follow Tailwind + shadcn pattern.
* **Yasmien:** prepare Postman collections, run tests, log issues in GitHub Issues.

---

## Team Workflow (Git)

1. Create your feature branch locally:

```bash
git checkout -b feature/<your-name>



