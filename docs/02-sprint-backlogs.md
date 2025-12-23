# Sprint Plans
**Clinic Management System - Agile Maintenance Project**

**Team:** Zakaria Eltawill (Team Lead), Mohamed Bseikri, Ali Ramadan, Ali Boujuari

---

## Project Management Tool

**ClickUp** was used as the primary project management tool to organize and track all work throughout the project:

- **Workspace Structure:** Organized by EPICs (8 folders) and Sprints (4 lists per EPIC)
- **Task Management:** All 47 tasks created with detailed descriptions, acceptance criteria, and subtasks
- **Team Collaboration:** Tasks assigned to team members with clear ownership
- **Sprint Tracking:** Each sprint had its own board view showing task progress
- **Custom Fields:** Story Points, Priority, PBI Number, Maintenance Type, Estimated Hours, Deliverables
- **Progress Monitoring:** Dashboard views showing sprint progress, team workload, and story point distribution
- **Evidence:** Complete task history, assignments, and sprint organization documented in ClickUp

This tool enabled effective Scrum Master leadership, clear task distribution, and transparent progress tracking across all 4 sprints.

---

## Sprint Overview

| Sprint | Duration | Focus Area | Story Points |
|--------|----------|------------|--------------|
| Sprint 1 | Week 1 | Analysis & Planning | 10 |
| Sprint 2 | Week 2 | Refactoring & Code Quality | 25 |
| Sprint 3 | Week 3 | Features & Testing | 25 |
| Sprint 4 | Week 4 | Polish & Documentation | 20 |

---

## Sprint 1: Code Exploration & Issue Identification
**Duration:** Week 1  
**Sprint Goal:** Understand codebase, identify issues, create backlog, set up development environment

### Sprint Backlog

#### Zakaria Eltawill (Team Lead)
- **Task 1.1:** Codebase analysis and documentation
  - Analyze all files
  - Document architecture
  - Identify coupling/cohesion issues
  - **Deliverable:** `analysis.md`
  - **Estimate:** 4 hours

- **Task 1.2:** Create product backlog
  - Organize all identified issues
  - Prioritize items
  - Estimate story points
  - **Deliverable:** `PRODUCT_BACKLOG.md`
  - **Estimate:** 3 hours

- **Task 1.3:** Set up Git repository
  - Initialize repository
  - Create branch structure
  - Set up .gitignore
  - **Deliverable:** Git repo with branches
  - **Estimate:** 1 hour

#### Mohamed Bseikri
- **Task 1.4:** Metrics calculation
  - Count LOC
  - Calculate complexity
  - Function point estimation
  - COCOMO estimation
  - **Deliverable:** Metrics in `analysis.md`
  - **Estimate:** 4 hours

- **Task 1.5:** Set up development environment
  - Verify Python/Flask setup
  - Create requirements.txt
  - Test application runs
  - **Deliverable:** Working dev environment
  - **Estimate:** 2 hours

#### Ali Ramadan
- **Task 1.6:** Code duplication analysis
  - Identify all duplicates
  - Document impact
  - Propose consolidation strategy
  - **Deliverable:** Duplication report
  - **Estimate:** 3 hours

- **Task 1.7:** Testing strategy planning
  - Research pytest
  - Plan test structure
  - Identify test cases
  - **Deliverable:** Testing plan
  - **Estimate:** 3 hours

#### Ali Boujuari
- **Task 1.8:** UI/UX analysis
  - Review all templates
  - Identify UI issues
  - Research CSS frameworks
  - **Deliverable:** UI improvement plan
  - **Estimate:** 3 hours

- **Task 1.9:** Create sprint planning document
  - Plan all 4 sprints
  - Assign tasks to team members
  - Create timeline
  - **Deliverable:** `SPRINT_PLANS.md`
  - **Estimate:** 2 hours

### Sprint 1 Deliverables
- ✅ `analysis.md` - Complete codebase analysis
- ✅ `PRODUCT_BACKLOG.md` - Prioritized backlog
- ✅ `SPRINT_PLANS.md` - All sprint plans
- ✅ Git repository initialized
- ✅ Development environment ready

### Sprint 1 Retrospective
*(To be completed after sprint)*

---

## Sprint 2: Refactoring & Code Quality Improvement
**Duration:** Week 2  
**Sprint Goal:** Remove duplication, implement repository pattern, improve code structure, add validation

### Sprint Backlog

#### Zakaria Eltawill (Team Lead)
- **Task 2.1:** Implement repository pattern
  - Create `repositories.py`
  - Implement `PatientRepository` class
  - Implement `AppointmentRepository` class
  - Replace global state
  - **Story Points:** 5
  - **Estimate:** 6 hours

- **Task 2.2:** Separate concerns (MVC structure)
  - Create `models.py`
  - Create `services.py`
  - Create `routes.py`
  - Refactor `app.py`
  - **Story Points:** 5
  - **Estimate:** 6 hours

- **Task 2.3:** Decouple appointments from patients
  - Change to patient_id references
  - Update all logic
  - Fix deletion cascading
  - **Story Points:** 5
  - **Estimate:** 4 hours

#### Mohamed Bseikri
- **Task 2.4:** Remove code duplication
  - Consolidate patient functions
  - Update all references
  - Test functionality
  - **Story Points:** 3
  - **Estimate:** 3 hours

- **Task 2.5:** Add input validation
  - Validate patient forms
  - Validate appointment forms
  - Add error messages
  - **Story Points:** 5
  - **Estimate:** 6 hours

- **Task 2.6:** Improve error handling
  - Add try-catch blocks
  - User-friendly messages
  - Error logging setup
  - **Story Points:** 3
  - **Estimate:** 4 hours

#### Ali Ramadan
- **Task 2.7:** Remove dead code
  - Delete unused functions
  - Remove unused imports
  - Clean up code
  - **Story Points:** 1
  - **Estimate:** 1 hour

- **Task 2.8:** Add type hints
  - Add to all functions
  - Type check code
  - **Story Points:** 2
  - **Estimate:** 3 hours

- **Task 2.9:** Consistent naming
  - Standardize parameters
  - Update all references
  - **Story Points:** 1
  - **Estimate:** 2 hours

- **Task 2.10:** Add flash messages
  - Implement Flask flash
  - Style messages
  - Add to all operations
  - **Story Points:** 2
  - **Estimate:** 3 hours

#### Ali Boujuari
- **Task 2.11:** Modern UI design (Phase 1)
  - Add Bootstrap CSS
  - Create base template
  - Style dashboard
  - **Story Points:** 5
  - **Estimate:** 6 hours

- **Task 2.12:** Improve form design
  - Style all forms
  - Add validation feedback
  - Better UX
  - **Story Points:** 3
  - **Estimate:** 4 hours

### Sprint 2 Deliverables
- ✅ Refactored code structure
- ✅ Repository pattern implemented
- ✅ Input validation added
- ✅ Error handling improved
- ✅ Modern UI foundation
- ✅ All tests passing

### Sprint 2 Retrospective
*(To be completed after sprint)*

---

## Sprint 3: Features, Testing & Bug Fixing
**Duration:** Week 3  
**Sprint Goal:** Add unit tests, implement features, fix bugs, complete UI improvements

### Sprint Backlog

#### Zakaria Eltawill (Team Lead)
- **Task 3.1:** Set up testing infrastructure
  - Install pytest
  - Create test structure
  - Add fixtures
  - **Story Points:** 3
  - **Estimate:** 3 hours

- **Task 3.2:** Unit tests for appointments
  - Test creation
  - Test retrieval
  - Test edge cases
  - **Story Points:** 5
  - **Estimate:** 6 hours

- **Task 3.3:** Integration tests
  - Test workflows
  - Test API endpoints
  - **Story Points:** 3
  - **Estimate:** 4 hours

- **Task 3.4:** Code documentation
  - Add docstrings
  - Document modules
  - **Story Points:** 3
  - **Estimate:** 4 hours

#### Mohamed Bseikri
- **Task 3.5:** Unit tests for patients
  - Test all operations
  - Test edge cases
  - Achieve 80%+ coverage
  - **Story Points:** 5
  - **Estimate:** 6 hours

- **Task 3.6:** Add logging
  - Configure logging
  - Log operations
  - Log errors
  - **Story Points:** 3
  - **Estimate:** 4 hours

- **Task 3.7:** Appointment search feature
  - Implement search
  - Add filters
  - Update UI
  - **Story Points:** 5
  - **Estimate:** 6 hours

#### Ali Ramadan
- **Task 3.8:** Improve table design
  - Style patient table
  - Style appointment table
  - Responsive design
  - **Story Points:** 2
  - **Estimate:** 3 hours

- **Task 3.9:** Appointment date validation
  - Validate format
  - Add date picker
  - Better UX
  - **Story Points:** 2
  - **Estimate:** 3 hours

- **Task 3.10:** CSRF protection
  - Install Flask-WTF
  - Add tokens
  - Validate
  - **Story Points:** 3
  - **Estimate:** 4 hours

#### Ali Boujuari
- **Task 3.11:** Complete UI design
  - Finish all pages
  - Add navigation
  - Responsive design
  - **Story Points:** 3
  - **Estimate:** 5 hours

- **Task 3.12:** Input sanitization
  - Escape HTML
  - Sanitize inputs
  - Prevent XSS
  - **Story Points:** 2
  - **Estimate:** 3 hours

- **Task 3.13:** Patient notes export (CSV)
  - Implement export
  - Add download
  - Test functionality
  - **Story Points:** 3
  - **Estimate:** 4 hours

### Sprint 3 Deliverables
- ✅ Comprehensive test suite (80%+ coverage)
- ✅ Appointment search feature
- ✅ CSV export feature
- ✅ Complete modern UI
- ✅ Security improvements
- ✅ All bugs fixed

### Sprint 3 Retrospective
*(To be completed after sprint)*

---

## Sprint 4: Metrics, Documentation & Presentation
**Duration:** Week 4  
**Sprint Goal:** Finalize documentation, calculate metrics, prepare presentation, create final report

### Sprint Backlog

#### Zakaria Eltawill (Team Lead)
- **Task 4.1:** Final code review
  - Review all changes
  - Ensure quality
  - Fix any issues
  - **Estimate:** 4 hours

- **Task 4.2:** Create refactor log
  - Document all changes
  - Before/after comparisons
  - **Deliverable:** `REFACTOR_LOG.md`
  - **Estimate:** 6 hours

- **Task 4.3:** Final comprehensive report
  - Compile all work
  - Document team contributions
  - Create final report
  - **Deliverable:** `FINAL_REPORT.md`
  - **Estimate:** 8 hours

- **Task 4.4:** Prepare presentation
  - Create slides
  - Prepare demo
  - Practice presentation
  - **Estimate:** 4 hours

#### Mohamed Bseikri
- **Task 4.5:** Calculate final metrics
  - LOC after refactoring
  - Complexity metrics
  - Coverage metrics
  - **Deliverable:** `METRICS_REPORT.md`
  - **Estimate:** 4 hours

- **Task 4.6:** Create README
  - Installation guide
  - Usage instructions
  - Development setup
  - **Deliverable:** `README.md`
  - **Estimate:** 3 hours

- **Task 4.7:** API documentation
  - Document endpoints
  - Add examples
  - **Deliverable:** API docs
  - **Estimate:** 3 hours

#### Ali Ramadan
- **Task 4.8:** Evaluation report
  - Compare before/after
  - Document improvements
  - Include screenshots
  - **Deliverable:** `EVALUATION.md`
  - **Estimate:** 5 hours

- **Task 4.9:** Test documentation
  - Document test suite
  - How to run tests
  - Coverage report
  - **Estimate:** 2 hours

- **Task 4.10:** Final UI polish
  - Last UI improvements
  - Bug fixes
  - **Estimate:** 3 hours

#### Ali Boujuari
- **Task 4.11:** User manual
  - Create user guide
  - Screenshots
  - Step-by-step instructions
  - **Deliverable:** `USER_MANUAL.md`
  - **Estimate:** 4 hours

- **Task 4.12:** Presentation visuals
  - Create diagrams
  - Prepare screenshots
  - Design slides
  - **Estimate:** 4 hours

- **Task 4.13:** Final testing
  - End-to-end testing
  - User acceptance testing
  - Bug fixes
  - **Estimate:** 4 hours

### Sprint 4 Deliverables
- ✅ Complete documentation
- ✅ Metrics report (before/after)
- ✅ Refactor log
- ✅ Final report
- ✅ User manual
- ✅ README
- ✅ Presentation ready
- ✅ All deliverables complete

### Sprint 4 Retrospective
*(To be completed after sprint)*

---

## Team Responsibilities Summary

### Zakaria Eltawill (Team Lead)
- Overall project coordination
- Architecture decisions
- Repository pattern implementation
- Code structure refactoring
- Final documentation
- Presentation

### Mohamed Bseikri
- Metrics and analysis
- Testing infrastructure
- Patient operations testing
- Logging implementation
- Search features
- API documentation

### Ali Ramadan
- Code duplication removal
- Input validation
- Type hints
- Table improvements
- Date validation
- CSRF protection
- Evaluation report

### Ali Boujuari
- UI/UX design and implementation
- Form improvements
- Navigation
- CSV export
- User manual
- Presentation visuals

---

## Definition of Done

For each task to be considered complete:
1. ✅ Code implemented and tested
2. ✅ Unit tests written and passing (where applicable)
3. ✅ Code reviewed by at least one team member
4. ✅ Documentation updated
5. ✅ Committed to Git with meaningful commit message
6. ✅ No new bugs introduced
7. ✅ Meets acceptance criteria

---

**Last Updated:** Sprint Planning Phase  
**Maintained by:** Zakaria Eltawill (Team Lead)

