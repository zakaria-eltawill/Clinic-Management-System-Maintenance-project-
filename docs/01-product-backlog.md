# Product Backlog
**Clinic Management System - Maintenance & Evolution Project**

**Team:** Zakaria Eltawill (Team Lead), Mohamed Bseikri, Ali Ramadan, Ali Boujuari

---

## Backlog Overview

This document contains all identified issues, improvements, and feature requests organized by priority and category.

---

## EPIC 1: Code Quality & Refactoring

### PBI-001: Remove Code Duplication
**Priority:** High  
**Story Points:** 3  
**Description:**  
Remove duplicate functions:
- Consolidate `add_patient_record()` and `create_patient()` into single function
- Consolidate `find_patient()` and `get_patient_by_id()` into single function

**Acceptance Criteria:**
- Only one function exists for each operation
- All existing functionality preserved
- Code coverage maintained

**Assigned to:** Ali Ramadan

---

### PBI-002: Implement Repository Pattern
**Priority:** High  
**Story Points:** 5  
**Description:**  
Replace global state with repository classes:
- Create `PatientRepository` class
- Create `AppointmentRepository` class
- Encapsulate data access logic

**Acceptance Criteria:**
- No global variables for data storage
- Repository classes handle all data operations
- Unit tests pass

**Assigned to:** Mohamed Bseikri

---

### PBI-003: Separate Concerns (MVC Pattern)
**Priority:** Medium  
**Story Points:** 5  
**Description:**  
Restructure code into separate modules:
- `models.py` - Data models
- `repositories.py` - Data access layer
- `services.py` - Business logic
- `routes.py` - Route handlers
- `app.py` - Application initialization

**Acceptance Criteria:**
- Clear separation of concerns
- Each module has single responsibility
- Application still functions correctly

**Assigned to:** Zakaria Eltawill

---

### PBI-004: Remove Dead Code
**Priority:** Low  
**Story Points:** 1  
**Description:**  
Remove unused code:
- Delete `messy_maintenance_function()`
- Remove unused `datetime` import

**Acceptance Criteria:**
- No unused functions or imports
- Code still functions

**Assigned to:** Ali Boujuari

---

## EPIC 2: Input Validation & Error Handling

### PBI-005: Add Input Validation
**Priority:** High  
**Story Points:** 5  
**Description:**  
Add validation for all form inputs:
- Validate patient name (required, min length)
- Validate age (numeric, range 0-150)
- Validate phone (format validation)
- Validate appointment date (format, future dates)
- Validate appointment description (required)

**Acceptance Criteria:**
- All forms validate input
- Error messages displayed to users
- Invalid data rejected

**Assigned to:** Ali Ramadan

---

### PBI-006: Improve Error Handling
**Priority:** High  
**Story Points:** 3  
**Description:**  
Add comprehensive error handling:
- Try-catch blocks for all operations
- User-friendly error messages
- Error logging

**Acceptance Criteria:**
- No unhandled exceptions
- Users see helpful error messages
- Errors logged for debugging

**Assigned to:** Mohamed Bseikri

---

### PBI-007: Add Flash Messages
**Priority:** Medium  
**Story Points:** 2  
**Description:**  
Implement Flask flash messages for user feedback:
- Success messages for create/update/delete
- Error messages for validation failures
- Info messages for operations

**Acceptance Criteria:**
- Users see feedback for all operations
- Messages are styled appropriately
- Messages clear after display

**Assigned to:** Ali Boujuari

---

## EPIC 3: Architecture Improvements

### PBI-008: Decouple Appointments from Patients
**Priority:** High  
**Story Points:** 5  
**Description:**  
Change appointments to store patient_id instead of patient object:
- Update appointment structure
- Modify appointment creation logic
- Update appointment display logic
- Fix deletion cascading

**Acceptance Criteria:**
- Appointments reference patient_id only
- Patient lookup done when needed
- Deletion works correctly

**Assigned to:** Zakaria Eltawill

---

### PBI-009: Add Type Hints
**Priority:** Low  
**Story Points:** 2  
**Description:**  
Add Python type hints to all functions:
- Function parameters
- Return types
- Variable types where helpful

**Acceptance Criteria:**
- All functions have type hints
- Code passes type checking
- IDE autocomplete improved

**Assigned to:** Ali Ramadan

---

### PBI-010: Consistent Naming Convention
**Priority:** Low  
**Story Points:** 1  
**Description:**  
Standardize naming:
- Use consistent parameter names (pid vs p_id)
- Follow Python naming conventions
- Update all references

**Acceptance Criteria:**
- Consistent naming throughout
- No naming conflicts

**Assigned to:** Ali Boujuari

---

## EPIC 4: Testing

### PBI-011: Set Up Testing Infrastructure
**Priority:** High  
**Story Points:** 3  
**Description:**  
Set up pytest and testing structure:
- Install pytest and dependencies
- Create `tests/` directory
- Create test configuration
- Add test fixtures

**Acceptance Criteria:**
- pytest installed and configured
- Test structure in place
- Can run tests with `pytest`

**Assigned to:** Mohamed Bseikri

---

### PBI-012: Unit Tests for Patient Operations
**Priority:** High  
**Story Points:** 5  
**Description:**  
Write unit tests for:
- Patient creation
- Patient retrieval
- Patient update
- Patient deletion
- Edge cases

**Acceptance Criteria:**
- 80%+ code coverage for patient operations
- All tests pass
- Edge cases covered

**Assigned to:** Ali Ramadan

---

### PBI-013: Unit Tests for Appointment Operations
**Priority:** High  
**Story Points:** 5  
**Description:**  
Write unit tests for:
- Appointment creation
- Appointment retrieval
- Appointment listing
- Edge cases

**Acceptance Criteria:**
- 80%+ code coverage for appointment operations
- All tests pass
- Edge cases covered

**Assigned to:** Zakaria Eltawill

---

### PBI-014: Integration Tests
**Priority:** Medium  
**Story Points:** 3  
**Description:**  
Write integration tests for:
- Full patient workflow
- Full appointment workflow
- API endpoints

**Acceptance Criteria:**
- Integration tests pass
- Workflows tested end-to-end

**Assigned to:** Mohamed Bseikri

---

## EPIC 5: User Interface Enhancement

### PBI-015: Modern UI Design
**Priority:** High  
**Story Points:** 8  
**Description:**  
Redesign UI with modern framework:
- Add Bootstrap or Tailwind CSS
- Responsive design
- Professional styling
- Consistent color scheme
- Improved typography

**Acceptance Criteria:**
- Modern, professional appearance
- Responsive on mobile/tablet/desktop
- Consistent styling throughout
- Improved user experience

**Assigned to:** Ali Boujuari

---

### PBI-016: Improve Form Design
**Priority:** Medium  
**Story Points:** 3  
**Description:**  
Enhance form layouts:
- Better form styling
- Clear labels and placeholders
- Inline validation feedback
- Better button styling

**Acceptance Criteria:**
- Forms are visually appealing
- Clear user guidance
- Validation feedback visible

**Assigned to:** Ali Boujuari

---

### PBI-017: Improve Table Design
**Priority:** Medium  
**Story Points:** 2  
**Description:**  
Enhance patient and appointment tables:
- Better table styling
- Hover effects
- Responsive tables
- Better action buttons

**Acceptance Criteria:**
- Tables are readable and styled
- Responsive on mobile
- Actions are clear

**Assigned to:** Ali Ramadan

---

### PBI-018: Add Navigation Bar
**Priority:** Low  
**Story Points:** 2  
**Description:**  
Add consistent navigation:
- Header with navigation links
- Active page indication
- Brand/logo area

**Acceptance Criteria:**
- Navigation on all pages
- Easy to move between sections
- Professional appearance

**Assigned to:** Ali Boujuari

---

## EPIC 6: Documentation & Logging

### PBI-019: Add Logging
**Priority:** Medium  
**Story Points:** 3  
**Description:**  
Implement logging:
- Configure Python logging
- Log all operations
- Log errors with stack traces
- Log user actions

**Acceptance Criteria:**
- Logging configured
- All operations logged
- Logs useful for debugging

**Assigned to:** Mohamed Bseikri

---

### PBI-020: Code Documentation
**Priority:** Medium  
**Story Points:** 3  
**Description:**  
Add documentation:
- Docstrings for all functions
- Module-level documentation
- Inline comments for complex logic

**Acceptance Criteria:**
- All functions documented
- Documentation is clear and helpful
- Follows Python docstring conventions

**Assigned to:** Zakaria Eltawill

---

### PBI-021: README File
**Priority:** Medium  
**Story Points:** 2  
**Description:**  
Create comprehensive README:
- Project overview
- Installation instructions
- Usage guide
- Development setup
- Contributing guidelines

**Acceptance Criteria:**
- README is complete
- Clear instructions
- Easy to follow

**Assigned to:** Ali Ramadan

---

### PBI-022: API Documentation
**Priority:** Low  
**Story Points:** 2  
**Description:**  
Document API endpoints:
- Endpoint descriptions
- Request/response formats
- Example requests

**Acceptance Criteria:**
- API documented
- Examples provided
- Easy to understand

**Assigned to:** Mohamed Bseikri

---

## EPIC 7: Security & Best Practices

### PBI-023: Add CSRF Protection
**Priority:** Medium  
**Story Points:** 3  
**Description:**  
Implement CSRF protection:
- Install Flask-WTF
- Add CSRF tokens to forms
- Validate tokens on submission

**Acceptance Criteria:**
- All forms have CSRF protection
- Tokens validated
- Security improved

**Assigned to:** Zakaria Eltawill

---

### PBI-024: Input Sanitization
**Priority:** Medium  
**Story Points:** 2  
**Description:**  
Sanitize user input:
- Escape HTML in templates
- Validate and sanitize all inputs
- Prevent XSS attacks

**Acceptance Criteria:**
- Input sanitized
- XSS vulnerabilities addressed
- Safe template rendering

**Assigned to:** Ali Ramadan

---

## EPIC 8: Feature Enhancements

### PBI-025: Appointment Search/Filter
**Priority:** Medium  
**Story Points:** 5  
**Description:**  
Add search functionality:
- Search appointments by patient name
- Filter by date range
- Search by description

**Acceptance Criteria:**
- Search works correctly
- Results displayed clearly
- Performance acceptable

**Assigned to:** Mohamed Bseikri

---

### PBI-026: Patient Notes Export (CSV)
**Priority:** Low  
**Story Points:** 3  
**Description:**  
Add export functionality:
- Export patient list to CSV
- Export appointments to CSV
- Download functionality

**Acceptance Criteria:**
- CSV export works
- Data formatted correctly
- Download successful

**Assigned to:** Ali Boujuari

---

### PBI-027: Appointment Date Validation
**Priority:** Medium  
**Story Points:** 2  
**Description:**  
Improve date handling:
- Validate date format
- Prevent past dates (optional)
- Better date picker UI

**Acceptance Criteria:**
- Dates validated
- User-friendly date input
- Clear error messages

**Assigned to:** Ali Ramadan

---

## Backlog Summary

**Total Story Points:** 95  
**High Priority:** 8 items (42 points)  
**Medium Priority:** 12 items (43 points)  
**Low Priority:** 4 items (10 points)

**Estimated Sprint Capacity:** ~20-25 points per sprint  
**Total Sprints Needed:** 4 sprints

---

**Last Updated:** Sprint Planning Phase  
**Maintained by:** Zakaria Eltawill (Team Lead)

