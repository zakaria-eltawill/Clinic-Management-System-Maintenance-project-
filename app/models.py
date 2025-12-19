"""
Data models for the Clinic Management System.
"""

from typing import Optional, Dict, Any


class Patient:
    """Represents a patient in the clinic system."""
    
    def __init__(self, patient_id: int, name: str, age: str, phone: str, notes: str = ''):
        """
        Initialize a Patient object.
        
        Args:
            patient_id: Unique identifier for the patient
            name: Patient's full name
            age: Patient's age (as string for flexibility)
            phone: Patient's phone number
            notes: Optional notes about the patient
        """
        self.id = patient_id
        self.name = name
        self.age = age
        self.phone = phone
        self.notes = notes
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert patient to dictionary format."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'notes': self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Patient':
        """Create Patient from dictionary."""
        return cls(
            patient_id=data['id'],
            name=data['name'],
            age=data['age'],
            phone=data['phone'],
            notes=data.get('notes', '')
        )


class Appointment:
    """Represents an appointment in the clinic system."""
    
    def __init__(self, appointment_id: int, patient_id: int, date: str, description: str):
        """
        Initialize an Appointment object.
        
        Args:
            appointment_id: Unique identifier for the appointment
            patient_id: ID of the patient (not full object to reduce coupling)
            date: Appointment date (YYYY-MM-DD format)
            description: Description of the appointment
        """
        self.id = appointment_id
        self.patient_id = patient_id
        self.date = date
        self.description = description
    
    def to_dict(self, patient: Optional[Patient] = None) -> Dict[str, Any]:
        """
        Convert appointment to dictionary format.
        
        Args:
            patient: Optional Patient object to include in response
        """
        result = {
            'id': self.id,
            'patient_id': self.patient_id,
            'date': self.date,
            'description': self.description
        }
        if patient:
            result['patient'] = patient.to_dict()
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Appointment':
        """Create Appointment from dictionary."""
        return cls(
            appointment_id=data['id'],
            patient_id=data.get('patient_id', data.get('patient', {}).get('id')),
            date=data['date'],
            description=data['description']
        )

