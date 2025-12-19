"""
Unit tests for data models.
"""

import pytest
from app.models import Patient, Appointment


class TestPatient:
    """Test cases for Patient model."""
    
    def test_patient_creation(self):
        """Test creating a patient."""
        patient = Patient(1, "John Doe", "30", "123-456-7890", "Test notes")
        assert patient.id == 1
        assert patient.name == "John Doe"
        assert patient.age == "30"
        assert patient.phone == "123-456-7890"
        assert patient.notes == "Test notes"
    
    def test_patient_to_dict(self):
        """Test converting patient to dictionary."""
        patient = Patient(1, "John Doe", "30", "123-456-7890", "Test notes")
        patient_dict = patient.to_dict()
        assert patient_dict['id'] == 1
        assert patient_dict['name'] == "John Doe"
        assert patient_dict['age'] == "30"
        assert patient_dict['phone'] == "123-456-7890"
        assert patient_dict['notes'] == "Test notes"
    
    def test_patient_from_dict(self):
        """Test creating patient from dictionary."""
        data = {
            'id': 1,
            'name': 'John Doe',
            'age': '30',
            'phone': '123-456-7890',
            'notes': 'Test notes'
        }
        patient = Patient.from_dict(data)
        assert patient.id == 1
        assert patient.name == "John Doe"
        assert patient.age == "30"
        assert patient.phone == "123-456-7890"
        assert patient.notes == "Test notes"


class TestAppointment:
    """Test cases for Appointment model."""
    
    def test_appointment_creation(self):
        """Test creating an appointment."""
        appointment = Appointment(1, 1, "2025-12-25", "Checkup")
        assert appointment.id == 1
        assert appointment.patient_id == 1
        assert appointment.date == "2025-12-25"
        assert appointment.description == "Checkup"
    
    def test_appointment_to_dict(self):
        """Test converting appointment to dictionary."""
        appointment = Appointment(1, 1, "2025-12-25", "Checkup")
        appointment_dict = appointment.to_dict()
        assert appointment_dict['id'] == 1
        assert appointment_dict['patient_id'] == 1
        assert appointment_dict['date'] == "2025-12-25"
        assert appointment_dict['description'] == "Checkup"
    
    def test_appointment_to_dict_with_patient(self):
        """Test converting appointment to dictionary with patient."""
        from models import Patient
        appointment = Appointment(1, 1, "2025-12-25", "Checkup")
        patient = Patient(1, "John Doe", "30", "123-456-7890")
        appointment_dict = appointment.to_dict(patient)
        assert appointment_dict['id'] == 1
        assert appointment_dict['patient_id'] == 1
        assert 'patient' in appointment_dict
        assert appointment_dict['patient']['name'] == "John Doe"

