"""
Unit tests for service layer.
"""

import pytest
from app.services import (
    validate_patient_name, validate_age, validate_phone, validate_date,
    validate_appointment_description, create_patient, update_patient,
    delete_patient, create_appointment
)
from app.repositories import patient_repository, appointment_repository


class TestValidation:
    """Test cases for validation functions."""
    
    def test_validate_patient_name_valid(self):
        """Test validating a valid patient name."""
        valid, error = validate_patient_name("John Doe")
        assert valid is True
        assert error == ""
    
    def test_validate_patient_name_empty(self):
        """Test validating an empty name."""
        valid, error = validate_patient_name("")
        assert valid is False
        assert "required" in error.lower()
    
    def test_validate_patient_name_too_short(self):
        """Test validating a name that's too short."""
        valid, error = validate_patient_name("A")
        assert valid is False
        assert "2 characters" in error
    
    def test_validate_age_valid(self):
        """Test validating a valid age."""
        valid, error = validate_age("30")
        assert valid is True
        assert error == ""
    
    def test_validate_age_invalid(self):
        """Test validating an invalid age."""
        valid, error = validate_age("abc")
        assert valid is False
        assert "number" in error.lower()
    
    def test_validate_age_negative(self):
        """Test validating a negative age."""
        valid, error = validate_age("-5")
        assert valid is False
        assert "negative" in error.lower()
    
    def test_validate_phone_valid(self):
        """Test validating a valid phone number."""
        valid, error = validate_phone("1234567890")
        assert valid is True
        assert error == ""
    
    def test_validate_phone_invalid(self):
        """Test validating an invalid phone number."""
        valid, error = validate_phone("abc")
        assert valid is False
        assert "digits" in error.lower()
    
    def test_validate_date_valid(self):
        """Test validating a valid date."""
        valid, error = validate_date("2025-12-25")
        assert valid is True
        assert error == ""
    
    def test_validate_date_invalid_format(self):
        """Test validating an invalid date format."""
        valid, error = validate_date("12/25/2025")
        assert valid is False
        assert "format" in error.lower()
    
    def test_validate_appointment_description_valid(self):
        """Test validating a valid description."""
        valid, error = validate_appointment_description("General Checkup")
        assert valid is True
        assert error == ""
    
    def test_validate_appointment_description_too_short(self):
        """Test validating a description that's too short."""
        valid, error = validate_appointment_description("AB")
        assert valid is False
        assert "3 characters" in error


class TestPatientServices:
    """Test cases for patient service functions."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Clear repositories
        patient_repository._patients.clear()
        patient_repository._next_id = 1
        appointment_repository._appointments.clear()
    
    def test_create_patient_success(self):
        """Test successfully creating a patient."""
        patient, error = create_patient("John Doe", "30", "1234567890")
        assert patient is not None
        assert error is None
        assert patient.name == "John Doe"
    
    def test_create_patient_invalid_name(self):
        """Test creating a patient with invalid name."""
        patient, error = create_patient("", "30", "1234567890")
        assert patient is None
        assert error is not None
        assert "required" in error.lower()
    
    def test_update_patient_success(self):
        """Test successfully updating a patient."""
        patient, _ = create_patient("John Doe", "30", "1234567890")
        updated, error = update_patient(patient.id, name="John Updated")
        assert updated is not None
        assert error is None
        assert updated.name == "John Updated"
    
    def test_update_patient_not_found(self):
        """Test updating a non-existent patient."""
        updated, error = update_patient(999, name="Test")
        assert updated is None
        assert error is not None
        assert "not found" in error.lower()
    
    def test_delete_patient_success(self):
        """Test successfully deleting a patient."""
        patient, _ = create_patient("John Doe", "30", "1234567890")
        success, error = delete_patient(patient.id)
        assert success is True
        assert error is None
    
    def test_delete_patient_not_found(self):
        """Test deleting a non-existent patient."""
        success, error = delete_patient(999)
        assert success is False
        assert error is not None


class TestAppointmentServices:
    """Test cases for appointment service functions."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Clear repositories
        patient_repository._patients.clear()
        patient_repository._next_id = 1
        appointment_repository._appointments.clear()
    
    def test_create_appointment_success(self):
        """Test successfully creating an appointment."""
        patient, _ = create_patient("John Doe", "30", "1234567890")
        appointment, error = create_appointment(patient.id, "2025-12-25", "Checkup")
        assert appointment is not None
        assert error is None
        assert appointment.patient_id == patient.id
    
    def test_create_appointment_invalid_patient(self):
        """Test creating an appointment with invalid patient ID."""
        appointment, error = create_appointment(999, "2025-12-25", "Checkup")
        assert appointment is None
        assert error is not None
        assert "not found" in error.lower()
    
    def test_create_appointment_invalid_date(self):
        """Test creating an appointment with invalid date."""
        patient, _ = create_patient("John Doe", "30", "1234567890")
        appointment, error = create_appointment(patient.id, "invalid-date", "Checkup")
        assert appointment is None
        assert error is not None

