# Clinic Management System

A modern Flask-based web application for managing patients and appointments in a clinic setting. This project demonstrates software maintenance and evolution practices, including refactoring, testing, and documentation.

## 🏥 Project Overview

The Clinic Management System is a web application that allows healthcare providers to:
- Manage patient records (CRUD operations)
- Schedule and manage appointments
- Search and filter appointments
- Export patient data to CSV
- Access RESTful API endpoints

## 👥 Team

- **Zakaria Eltawill** - Team Lead
- **Mohamed Bseikri** - Developer
- **Ali Ramadan** - Developer
- **Ali Boujuari** - Developer

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project:**
   ```bash
   cd clinic_legacy_project
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask development server:**
   ```bash
   python run.py
   ```
   
   Or alternatively:
   ```bash
   python -m app
   ```

2. **Access the application:**
   - Open your web browser and navigate to: `http://127.0.0.1:5001`
   - The application will be running with sample data pre-loaded

### Running Tests

To run the test suite:

```bash
pytest
```

To run tests with coverage report:

```bash
pytest --cov=. --cov-report=html
```

The coverage report will be generated in `htmlcov/index.html`.

## 📁 Project Structure

```
clinic-management-system/
├── app/                    # Application package
│   ├── __init__.py        # Application initialization
│   ├── app.py             # Main application file
│   ├── models.py          # Data models (Patient, Appointment)
│   ├── repositories.py   # Data access layer (Repository pattern)
│   ├── services.py       # Business logic layer (Validation, services)
│   ├── routes.py         # Route handlers
│   └── templates/        # HTML templates
│       ├── base.html      # Base template with navigation
│       ├── index.html     # Dashboard
│       ├── patients.html  # Patient list
│       ├── patient_add.html
│       ├── patient_edit.html
│       ├── appointments.html
│       └── appointment_create.html
├── tests/                 # Test suite
│   ├── test_models.py
│   ├── test_repositories.py
│   ├── test_services.py
│   └── test_routes.py
├── docs/                  # Documentation
│   ├── 00-analysis.md
│   ├── 01-product-backlog.md
│   ├── 02-sprint-backlogs.md
│   ├── 03-refactor-log.md
│   ├── 04-metrics-report.md
│   ├── 05-final-documentation.md
│   ├── 06-user-manual.md
│   └── 07-project-summary.md
├── presentation/          # Presentation materials
│   └── presentation-outline.md
├── app_old.py            # Original legacy code (for reference)
├── run.py                # Application entry point
├── requirements.txt      # Python dependencies
├── pytest.ini           # Pytest configuration
└── README.md            # This file
```

## 🎯 Features

### Patient Management
- ✅ Add new patients with validation
- ✅ View all patients in a table
- ✅ Edit patient information
- ✅ Delete patients (with cascade deletion of appointments)
- ✅ Export patients to CSV

### Appointment Management
- ✅ Create appointments linked to patients
- ✅ View all appointments
- ✅ Search appointments by description
- ✅ Filter appointments by date
- ✅ Automatic patient information display

### User Interface
- ✅ Modern, responsive design using Bootstrap 5
- ✅ Flash messages for user feedback
- ✅ Form validation with helpful error messages
- ✅ Professional color scheme and styling
- ✅ Mobile-friendly navigation

### API Endpoints
- ✅ `GET /api/patients` - Get all patients as JSON
- ✅ `GET /api/appointments` - Get all appointments as JSON

## 🏗️ Architecture

The application follows a layered architecture:

1. **Models Layer** (`models.py`)
   - Data models: `Patient`, `Appointment`
   - Data transfer objects

2. **Repository Layer** (`repositories.py`)
   - Data access abstraction
   - `PatientRepository` - Patient data operations
   - `AppointmentRepository` - Appointment data operations

3. **Service Layer** (`services.py`)
   - Business logic
   - Input validation
   - Error handling

4. **Routes Layer** (`routes.py`)
   - HTTP request handling
   - Template rendering
   - Flash messages

5. **Templates Layer** (`templates/`)
   - HTML templates with Jinja2
   - Bootstrap 5 for styling

## 🧪 Testing

The project includes comprehensive unit and integration tests:

- **Model Tests** - Test data models
- **Repository Tests** - Test data access layer
- **Service Tests** - Test business logic and validation
- **Route Tests** - Test HTTP endpoints

Run tests with:
```bash
pytest
```

## 📊 Code Quality

- **Type Hints** - All functions include type annotations
- **Documentation** - Comprehensive docstrings
- **Error Handling** - Try-catch blocks with logging
- **Input Validation** - All user inputs validated
- **Code Structure** - Separation of concerns (MVC pattern)

## 🔒 Security Features

- Input sanitization
- Form validation
- Error handling
- Secure session management

## 📝 Documentation

All documentation is available in the `docs/` folder:

- **01-product-backlog.md** - All identified issues and features
- **02-sprint-backlogs.md** - 4-sprint Agile plan
- **03-refactor-log.md** - Documentation of all changes
- **04-metrics-report.md** - Before/after metrics comparison
- **05-final-documentation.md** - Comprehensive final report
- **06-user-manual.md** - Complete user guide

Presentation materials are in the `presentation/` folder.

## 🛠️ Development

### Adding New Features

1. Create feature branch
2. Implement feature with tests
3. Run test suite
4. Update documentation
5. Submit for code review

### Code Style

- Follow PEP 8 Python style guide
- Use type hints for all functions
- Write docstrings for all functions
- Keep functions small and focused

## 📈 Metrics

### Before Refactoring
- **LOC:** 102 lines
- **Code Duplication:** ~15%
- **Test Coverage:** 0%
- **Functions:** 10
- **Global Variables:** 3

### After Refactoring
- **LOC:** ~600 lines (well-structured)
- **Code Duplication:** 0%
- **Test Coverage:** 80%+
- **Functions:** 30+ (organized in modules)
- **Global Variables:** 0 (repository pattern)

## 🐛 Known Issues

- Data is stored in memory (not persistent)
- No database integration (future enhancement)
- No user authentication (future enhancement)

## 🔮 Future Enhancements

- [ ] Database persistence (SQLite/PostgreSQL)
- [ ] User authentication and authorization
- [ ] Email notifications for appointments
- [ ] Appointment reminders
- [ ] Patient medical history
- [ ] Reports and analytics
- [ ] Multi-language support

## 📄 License

This project is part of a Software Maintenance & Evolution course assignment.

## 🙏 Acknowledgments

- Flask framework
- Bootstrap 5 for UI components
- Bootstrap Icons
- Pytest for testing framework

## 📧 Contact

For questions or issues, please contact the development team.

---

**Last Updated:** December 2025  
**Version:** 2.0 (Refactored)

