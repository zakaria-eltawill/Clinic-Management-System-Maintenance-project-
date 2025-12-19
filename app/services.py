"""
Business logic layer for the Clinic Management System.
Contains service functions that handle business rules and validation.
"""

from typing import Tuple, Optional, List, Dict, Any
from app.repositories import patient_repository, appointment_repository
from app.models import Patient, Appointment
import re


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_patient_name(name: str) -> Tuple[bool, str]:
    """
    Validate patient name.
    
    Args:
        name: Name to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Patient name is required"
    if len(name.strip()) < 2:
        return False, "Patient name must be at least 2 characters"
    if len(name.strip()) > 100:
        return False, "Patient name must be less than 100 characters"
    return True, ""


def validate_age(age: str) -> Tuple[bool, str]:
    """
    Validate patient age.
    
    Args:
        age: Age to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not age or not age.strip():
        return False, "Age is required"
    
    try:
        age_int = int(age.strip())
        if age_int < 0:
            return False, "Age cannot be negative"
        if age_int > 150:
            return False, "Age must be less than 150"
        return True, ""
    except ValueError:
        return False, "Age must be a valid number"


def validate_phone(phone: str) -> Tuple[bool, str]:
    """
    Validate phone number.
    
    Args:
        phone: Phone number to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not phone or not phone.strip():
        return False, "Phone number is required"
    
    # Allow various phone formats
    phone_clean = re.sub(r'[\s\-\(\)]', '', phone.strip())
    if not phone_clean:
        return False, "Phone number is required"
    
    if len(phone_clean) < 7:
        return False, "Phone number is too short"
    if len(phone_clean) > 15:
        return False, "Phone number is too long"
    
    if not phone_clean.isdigit():
        return False, "Phone number must contain only digits"
    
    return True, ""


def validate_date(date_str: str) -> Tuple[bool, str]:
    """
    Validate date format (YYYY-MM-DD).
    
    Args:
        date_str: Date string to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not date_str or not date_str.strip():
        return False, "Date is required"
    
    # Check format YYYY-MM-DD
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(date_pattern, date_str.strip()):
        return False, "Date must be in YYYY-MM-DD format"
    
    # Try to parse the date
    try:
        from datetime import datetime
        datetime.strptime(date_str.strip(), '%Y-%m-%d')
        return True, ""
    except ValueError:
        return False, "Invalid date"


def validate_appointment_description(description: str) -> Tuple[bool, str]:
    """
    Validate appointment description.
    
    Args:
        description: Description to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not description or not description.strip():
        return False, "Description is required"
    if len(description.strip()) < 3:
        return False, "Description must be at least 3 characters"
    if len(description.strip()) > 500:
        return False, "Description must be less than 500 characters"
    return True, ""


def create_patient(name: str, age: str, phone: str, notes: str = '') -> Tuple[Optional[Patient], Optional[str]]:
    """
    Create a new patient with validation.
    
    Args:
        name: Patient name
        age: Patient age
        phone: Patient phone
        notes: Optional notes
        
    Returns:
        Tuple of (Patient object or None, error_message or None)
    """
    # Validate inputs
    valid, error = validate_patient_name(name)
    if not valid:
        return None, error
    
    valid, error = validate_age(age)
    if not valid:
        return None, error
    
    valid, error = validate_phone(phone)
    if not valid:
        return None, error
    
    # Create patient
    patient = patient_repository.create(name.strip(), age.strip(), phone.strip(), notes.strip())
    return patient, None


def update_patient(patient_id: int, name: Optional[str] = None,
                   age: Optional[str] = None, phone: Optional[str] = None,
                   notes: Optional[str] = None) -> Tuple[Optional[Patient], Optional[str]]:
    """
    Update a patient with validation.
    
    Args:
        patient_id: ID of patient to update
        name: New name (optional)
        age: New age (optional)
        phone: New phone (optional)
        notes: New notes (optional)
        
    Returns:
        Tuple of (Patient object or None, error_message or None)
    """
    # Check if patient exists
    patient = patient_repository.find_by_id(patient_id)
    if not patient:
        return None, "Patient not found"
    
    # Validate inputs if provided
    if name is not None:
        valid, error = validate_patient_name(name)
        if not valid:
            return None, error
        name = name.strip()
    
    if age is not None:
        valid, error = validate_age(age)
        if not valid:
            return None, error
        age = age.strip()
    
    if phone is not None:
        valid, error = validate_phone(phone)
        if not valid:
            return None, error
        phone = phone.strip()
    
    # Update patient
    updated_patient = patient_repository.update(patient_id, name, age, phone, notes)
    return updated_patient, None


def delete_patient(patient_id: int) -> Tuple[bool, Optional[str]]:
    """
    Delete a patient and all associated appointments.
    
    Args:
        patient_id: ID of patient to delete
        
    Returns:
        Tuple of (success, error_message or None)
    """
    # Check if patient exists
    patient = patient_repository.find_by_id(patient_id)
    if not patient:
        return False, "Patient not found"
    
    # Delete associated appointments
    appointment_repository.delete_by_patient_id(patient_id)
    
    # Delete patient
    success = patient_repository.delete(patient_id)
    return success, None


def create_appointment(patient_id: int, date: str, description: str) -> Tuple[Optional[Appointment], Optional[str]]:
    """
    Create a new appointment with validation.
    
    Args:
        patient_id: ID of the patient
        date: Appointment date
        description: Appointment description
        
    Returns:
        Tuple of (Appointment object or None, error_message or None)
    """
    # Validate patient exists
    patient = patient_repository.find_by_id(patient_id)
    if not patient:
        return None, "Patient not found"
    
    # Validate inputs
    valid, error = validate_date(date)
    if not valid:
        return None, error
    
    valid, error = validate_appointment_description(description)
    if not valid:
        return None, error
    
    # Create appointment
    appointment = appointment_repository.create(patient_id, date.strip(), description.strip())
    return appointment, None


def get_appointments_with_patients() -> List[Dict[str, Any]]:
    """
    Get all appointments with patient information included.
    
    Returns:
        List of appointment dictionaries with patient data
    """
    appointments = appointment_repository.get_all()
    result = []
    
    for appointment in appointments:
        patient = patient_repository.find_by_id(appointment.patient_id)
        result.append(appointment.to_dict(patient))
    
    return result


def search_appointments(query: Optional[str] = None,
                       patient_id: Optional[int] = None,
                       date: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Search appointments with patient information.
    
    Args:
        query: Search term for description
        patient_id: Filter by patient ID
        date: Filter by date
        
    Returns:
        List of appointment dictionaries with patient data
    """
    appointments = appointment_repository.search(query, patient_id, date)
    result = []
    
    for appointment in appointments:
        patient = patient_repository.find_by_id(appointment.patient_id)
        result.append(appointment.to_dict(patient))
    
    return result

