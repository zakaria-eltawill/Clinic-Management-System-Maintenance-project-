"""
Integration tests for route handlers.
"""

import pytest
from app import app
from app.repositories import patient_repository, appointment_repository


@pytest.fixture
def client():
    """Create a test client."""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    with app.test_client() as client:
        yield client


@pytest.fixture
def setup_data():
    """Set up test data."""
    # Clear repositories
    patient_repository._patients.clear()
    patient_repository._next_id = 1
    appointment_repository._appointments.clear()
    
    # Create test patient
    patient = patient_repository.create("Test Patient", "30", "1234567890")
    return patient


class TestIndexRoute:
    """Test cases for index route."""
    
    def test_index_route(self, client):
        """Test accessing the index page."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Dashboard' in response.data


class TestPatientRoutes:
    """Test cases for patient routes."""
    
    def test_list_patients(self, client, setup_data):
        """Test listing patients."""
        response = client.get('/patients')
        assert response.status_code == 200
        assert b'Patients' in response.data
    
    def test_add_patient_get(self, client):
        """Test getting the add patient form."""
        response = client.get('/patients/add')
        assert response.status_code == 200
        assert b'Add' in response.data
    
    def test_add_patient_post_success(self, client):
        """Test successfully adding a patient."""
        response = client.post('/patients/add', data={
            'name': 'New Patient',
            'age': '25',
            'phone': '1234567890'
        }, follow_redirects=True)
        assert response.status_code == 200
    
    def test_add_patient_post_invalid(self, client):
        """Test adding a patient with invalid data."""
        response = client.post('/patients/add', data={
            'name': '',
            'age': '25',
            'phone': '1234567890'
        })
        assert response.status_code == 200
        assert b'required' in response.data.lower()
    
    def test_edit_patient_get(self, client, setup_data):
        """Test getting the edit patient form."""
        response = client.get(f'/patients/{setup_data.id}/edit')
        assert response.status_code == 200
        assert b'Edit' in response.data
    
    def test_edit_patient_post(self, client, setup_data):
        """Test updating a patient."""
        response = client.post(f'/patients/{setup_data.id}/edit', data={
            'name': 'Updated Patient',
            'age': '31',
            'phone': '0987654321'
        }, follow_redirects=True)
        assert response.status_code == 200


class TestAppointmentRoutes:
    """Test cases for appointment routes."""
    
    def test_list_appointments(self, client):
        """Test listing appointments."""
        response = client.get('/appointments')
        assert response.status_code == 200
        assert b'Appointments' in response.data
    
    def test_create_appointment_get(self, client, setup_data):
        """Test getting the create appointment form."""
        response = client.get('/appointments/create')
        assert response.status_code == 200
        assert b'Create' in response.data
    
    def test_create_appointment_post_success(self, client, setup_data):
        """Test successfully creating an appointment."""
        response = client.post('/appointments/create', data={
            'patient_id': str(setup_data.id),
            'date': '2025-12-25',
            'description': 'Test Appointment'
        }, follow_redirects=True)
        assert response.status_code == 200


class TestAPIRoutes:
    """Test cases for API routes."""
    
    def test_api_get_patients(self, client, setup_data):
        """Test API endpoint for getting patients."""
        response = client.get('/api/patients')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) > 0
    
    def test_api_get_appointments(self, client):
        """Test API endpoint for getting appointments."""
        response = client.get('/api/appointments')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)

