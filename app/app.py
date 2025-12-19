"""
Clinic Management System - Main Application
Refactored version with improved architecture and maintainability.
"""

from flask import Flask
import logging
from app.routes import register_routes
from app.repositories import patient_repository, appointment_repository
from app.models import Patient, Appointment

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask application
app = Flask(__name__)
app.secret_key = 'clinic-management-system-secret-key-change-in-production'

# Register all routes
register_routes(app)


def initialize_sample_data():
    """Initialize the application with sample data for demonstration."""
    try:
        # Check if data already exists
        if patient_repository.count() > 0:
            logger.info("Sample data already exists, skipping initialization")
            return
        
        # Create sample patients
        patient1 = patient_repository.create('Ahmed Ali', '30', '091-111-222', 'Regular patient')
        patient2 = patient_repository.create('Sara Omar', '25', '092-222-333', 'New patient')
        
        # Create sample appointment
        appointment_repository.create(
            patient_id=patient1.id,
            date='2025-10-22',
            description='General Checkup'
        )
        
        logger.info("Sample data initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing sample data: {e}", exc_info=True)


if __name__ == '__main__':
    # Initialize sample data
    initialize_sample_data()
    
    # Run the application
    logger.info("Starting Clinic Management System...")
    app.run(debug=True, host='127.0.0.1', port=5001)
