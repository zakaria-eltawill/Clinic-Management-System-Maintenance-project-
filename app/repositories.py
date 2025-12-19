"""
Repository pattern implementation for data access.
Encapsulates all data storage and retrieval logic.
"""

from typing import List, Optional, Dict, Any
from app.models import Patient, Appointment


class PatientRepository:
    """Repository for patient data operations."""
    
    def __init__(self):
        """Initialize the repository with empty storage."""
        self._patients: List[Patient] = []
        self._next_id: int = 1
    
    def create(self, name: str, age: str, phone: str, notes: str = '') -> Patient:
        """
        Create a new patient record.
        
        Args:
            name: Patient's name
            age: Patient's age
            phone: Patient's phone number
            notes: Optional notes
            
        Returns:
            Created Patient object
        """
        patient = Patient(
            patient_id=self._next_id,
            name=name,
            age=age,
            phone=phone,
            notes=notes
        )
        self._patients.append(patient)
        self._next_id += 1
        return patient
    
    def find_by_id(self, patient_id: int) -> Optional[Patient]:
        """
        Find a patient by ID.
        
        Args:
            patient_id: Patient ID to search for
            
        Returns:
            Patient object if found, None otherwise
        """
        for patient in self._patients:
            if patient.id == patient_id:
                return patient
        return None
    
    def get_all(self) -> List[Patient]:
        """
        Get all patients.
        
        Returns:
            List of all Patient objects
        """
        return self._patients.copy()
    
    def update(self, patient_id: int, name: Optional[str] = None, 
               age: Optional[str] = None, phone: Optional[str] = None,
               notes: Optional[str] = None) -> Optional[Patient]:
        """
        Update a patient's information.
        
        Args:
            patient_id: ID of patient to update
            name: New name (optional)
            age: New age (optional)
            phone: New phone (optional)
            notes: New notes (optional)
            
        Returns:
            Updated Patient object if found, None otherwise
        """
        patient = self.find_by_id(patient_id)
        if not patient:
            return None
        
        if name is not None:
            patient.name = name
        if age is not None:
            patient.age = age
        if phone is not None:
            patient.phone = phone
        if notes is not None:
            patient.notes = notes
        
        return patient
    
    def delete(self, patient_id: int) -> bool:
        """
        Delete a patient by ID.
        
        Args:
            patient_id: ID of patient to delete
            
        Returns:
            True if patient was deleted, False if not found
        """
        patient = self.find_by_id(patient_id)
        if patient:
            self._patients.remove(patient)
            return True
        return False
    
    def count(self) -> int:
        """Get total number of patients."""
        return len(self._patients)


class AppointmentRepository:
    """Repository for appointment data operations."""
    
    def __init__(self):
        """Initialize the repository with empty storage."""
        self._appointments: List[Appointment] = []
    
    def create(self, patient_id: int, date: str, description: str) -> Appointment:
        """
        Create a new appointment.
        
        Args:
            patient_id: ID of the patient
            date: Appointment date
            description: Appointment description
            
        Returns:
            Created Appointment object
        """
        appointment_id = len(self._appointments) + 1
        appointment = Appointment(
            appointment_id=appointment_id,
            patient_id=patient_id,
            date=date,
            description=description
        )
        self._appointments.append(appointment)
        return appointment
    
    def find_by_id(self, appointment_id: int) -> Optional[Appointment]:
        """
        Find an appointment by ID.
        
        Args:
            appointment_id: Appointment ID to search for
            
        Returns:
            Appointment object if found, None otherwise
        """
        for appointment in self._appointments:
            if appointment.id == appointment_id:
                return appointment
        return None
    
    def get_all(self) -> List[Appointment]:
        """
        Get all appointments.
        
        Returns:
            List of all Appointment objects
        """
        return self._appointments.copy()
    
    def find_by_patient_id(self, patient_id: int) -> List[Appointment]:
        """
        Find all appointments for a specific patient.
        
        Args:
            patient_id: Patient ID to search for
            
        Returns:
            List of Appointment objects for the patient
        """
        return [apt for apt in self._appointments if apt.patient_id == patient_id]
    
    def delete_by_patient_id(self, patient_id: int) -> int:
        """
        Delete all appointments for a specific patient.
        
        Args:
            patient_id: Patient ID whose appointments should be deleted
            
        Returns:
            Number of appointments deleted
        """
        initial_count = len(self._appointments)
        self._appointments = [apt for apt in self._appointments if apt.patient_id != patient_id]
        return initial_count - len(self._appointments)
    
    def search(self, query: Optional[str] = None, 
               patient_id: Optional[int] = None,
               date: Optional[str] = None) -> List[Appointment]:
        """
        Search appointments by various criteria.
        
        Args:
            query: Search term for description
            patient_id: Filter by patient ID
            date: Filter by date
            
        Returns:
            List of matching Appointment objects
        """
        results = self._appointments.copy()
        
        if patient_id is not None:
            results = [apt for apt in results if apt.patient_id == patient_id]
        
        if date:
            results = [apt for apt in results if apt.date == date]
        
        if query:
            query_lower = query.lower()
            results = [apt for apt in results if query_lower in apt.description.lower()]
        
        return results
    
    def count(self) -> int:
        """Get total number of appointments."""
        return len(self._appointments)


# Global repository instances (will be replaced with dependency injection in future)
patient_repository = PatientRepository()
appointment_repository = AppointmentRepository()

