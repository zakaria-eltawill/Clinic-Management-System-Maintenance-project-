"""
Unit tests for repository classes.
"""

import pytest
from app.repositories import PatientRepository, AppointmentRepository
from app.models import Patient, Appointment


class TestPatientRepository:
    """Test cases for PatientRepository."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.repo = PatientRepository()
    
    def test_create_patient(self):
        """Test creating a patient."""
        patient = self.repo.create("John Doe", "30", "123-456-7890")
        assert patient.name == "John Doe"
        assert patient.age == "30"
        assert patient.phone == "123-456-7890"
        assert patient.id == 1
    
    def test_find_by_id_existing(self):
        """Test finding an existing patient."""
        patient = self.repo.create("John Doe", "30", "123-456-7890")
        found = self.repo.find_by_id(patient.id)
        assert found is not None
        assert found.name == "John Doe"
    
    def test_find_by_id_nonexistent(self):
        """Test finding a non-existent patient."""
        found = self.repo.find_by_id(999)
        assert found is None
    
    def test_get_all(self):
        """Test getting all patients."""
        self.repo.create("John Doe", "30", "123-456-7890")
        self.repo.create("Jane Smith", "25", "098-765-4321")
        patients = self.repo.get_all()
        assert len(patients) == 2
    
    def test_update_patient(self):
        """Test updating a patient."""
        patient = self.repo.create("John Doe", "30", "123-456-7890")
        updated = self.repo.update(patient.id, name="John Updated")
        assert updated.name == "John Updated"
        assert updated.age == "30"  # Unchanged
    
    def test_delete_patient(self):
        """Test deleting a patient."""
        patient = self.repo.create("John Doe", "30", "123-456-7890")
        success = self.repo.delete(patient.id)
        assert success is True
        assert self.repo.find_by_id(patient.id) is None
    
    def test_count(self):
        """Test counting patients."""
        assert self.repo.count() == 0
        self.repo.create("John Doe", "30", "123-456-7890")
        assert self.repo.count() == 1


class TestAppointmentRepository:
    """Test cases for AppointmentRepository."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.repo = AppointmentRepository()
    
    def test_create_appointment(self):
        """Test creating an appointment."""
        appointment = self.repo.create(1, "2025-12-25", "Checkup")
        assert appointment.patient_id == 1
        assert appointment.date == "2025-12-25"
        assert appointment.description == "Checkup"
        assert appointment.id == 1
    
    def test_find_by_id_existing(self):
        """Test finding an existing appointment."""
        appointment = self.repo.create(1, "2025-12-25", "Checkup")
        found = self.repo.find_by_id(appointment.id)
        assert found is not None
        assert found.description == "Checkup"
    
    def test_find_by_patient_id(self):
        """Test finding appointments by patient ID."""
        self.repo.create(1, "2025-12-25", "Checkup")
        self.repo.create(1, "2025-12-26", "Follow-up")
        self.repo.create(2, "2025-12-27", "Other")
        appointments = self.repo.find_by_patient_id(1)
        assert len(appointments) == 2
    
    def test_delete_by_patient_id(self):
        """Test deleting appointments by patient ID."""
        self.repo.create(1, "2025-12-25", "Checkup")
        self.repo.create(1, "2025-12-26", "Follow-up")
        self.repo.create(2, "2025-12-27", "Other")
        deleted_count = self.repo.delete_by_patient_id(1)
        assert deleted_count == 2
        assert self.repo.count() == 1
    
    def test_search_by_description(self):
        """Test searching appointments by description."""
        self.repo.create(1, "2025-12-25", "General Checkup")
        self.repo.create(1, "2025-12-26", "Follow-up Visit")
        results = self.repo.search(query="Checkup")
        assert len(results) == 1
        assert results[0].description == "General Checkup"
    
    def test_search_by_date(self):
        """Test searching appointments by date."""
        self.repo.create(1, "2025-12-25", "Checkup")
        self.repo.create(1, "2025-12-26", "Follow-up")
        results = self.repo.search(date="2025-12-25")
        assert len(results) == 1
        assert results[0].date == "2025-12-25"

