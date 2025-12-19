"""
Route handlers for the Clinic Management System.
Contains all Flask route definitions.
"""

from flask import render_template, request, redirect, url_for, flash, jsonify
from app.services import (
    create_patient, update_patient, delete_patient,
    create_appointment, get_appointments_with_patients, search_appointments
)
from app.repositories import patient_repository, appointment_repository
import logging

logger = logging.getLogger(__name__)


def register_routes(app):
    """
    Register all routes with the Flask application.
    
    Args:
        app: Flask application instance
    """
    
    @app.route('/')
    def index():
        """Display the main dashboard."""
        try:
            patients = patient_repository.get_all()
            appointments = get_appointments_with_patients()
            return render_template('index.html', patients=patients, appointments=appointments)
        except Exception as e:
            logger.error(f"Error loading dashboard: {e}", exc_info=True)
            flash("An error occurred while loading the dashboard.", "error")
            return render_template('index.html', patients=[], appointments=[])
    
    @app.route('/patients')
    def list_patients():
        """Display list of all patients."""
        try:
            patients = patient_repository.get_all()
            return render_template('patients.html', patients=patients)
        except Exception as e:
            logger.error(f"Error loading patients: {e}", exc_info=True)
            flash("An error occurred while loading patients.", "error")
            return render_template('patients.html', patients=[])
    
    @app.route('/patients/add', methods=['GET', 'POST'])
    def patient_add():
        """Add a new patient."""
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            age = request.form.get('age', '').strip()
            phone = request.form.get('phone', '').strip()
            notes = request.form.get('notes', '').strip()
            
            patient, error = create_patient(name, age, phone, notes)
            
            if error:
                flash(error, "error")
                return render_template('patient_add.html', 
                                     name=name, age=age, phone=phone, notes=notes)
            
            flash(f"Patient '{patient.name}' added successfully!", "success")
            logger.info(f"Patient created: ID={patient.id}, Name={patient.name}")
            return redirect(url_for('list_patients'))
        
        return render_template('patient_add.html')
    
    @app.route('/patients/<int:patient_id>/edit', methods=['GET', 'POST'])
    def patient_edit(patient_id):
        """Edit an existing patient."""
        patient = patient_repository.find_by_id(patient_id)
        
        if not patient:
            flash("Patient not found.", "error")
            return redirect(url_for('list_patients'))
        
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            age = request.form.get('age', '').strip()
            phone = request.form.get('phone', '').strip()
            notes = request.form.get('notes', '').strip()
            
            updated_patient, error = update_patient(patient_id, name, age, phone, notes)
            
            if error:
                flash(error, "error")
                return render_template('patient_edit.html', patient=patient)
            
            flash(f"Patient '{updated_patient.name}' updated successfully!", "success")
            logger.info(f"Patient updated: ID={patient_id}")
            return redirect(url_for('list_patients'))
        
        return render_template('patient_edit.html', patient=patient)
    
    @app.route('/patients/<int:patient_id>/delete', methods=['POST'])
    def patient_delete(patient_id):
        """Delete a patient."""
        patient = patient_repository.find_by_id(patient_id)
        
        if not patient:
            flash("Patient not found.", "error")
            return redirect(url_for('list_patients'))
        
        success, error = delete_patient(patient_id)
        
        if error:
            flash(error, "error")
        else:
            flash(f"Patient '{patient.name}' and all associated appointments deleted successfully!", "success")
            logger.info(f"Patient deleted: ID={patient_id}")
        
        return redirect(url_for('list_patients'))
    
    @app.route('/appointments')
    def list_appointments():
        """Display list of all appointments with optional search."""
        try:
            query = request.args.get('search', '').strip()
            date_filter = request.args.get('date', '').strip()
            
            if query or date_filter:
                appointments = search_appointments(query=query if query else None,
                                                 date=date_filter if date_filter else None)
            else:
                appointments = get_appointments_with_patients()
            
            return render_template('appointments.html', appointments=appointments, 
                                search_query=query, date_filter=date_filter)
        except Exception as e:
            logger.error(f"Error loading appointments: {e}", exc_info=True)
            flash("An error occurred while loading appointments.", "error")
            return render_template('appointments.html', appointments=[])
    
    @app.route('/appointments/create', methods=['GET', 'POST'])
    def appointment_create():
        """Create a new appointment."""
        patients = patient_repository.get_all()
        
        if request.method == 'POST':
            try:
                patient_id = int(request.form.get('patient_id', 0))
            except (ValueError, TypeError):
                flash("Invalid patient selected.", "error")
                return render_template('appointment_create.html', patients=patients)
            
            date = request.form.get('date', '').strip()
            description = request.form.get('description', '').strip()
            
            appointment, error = create_appointment(patient_id, date, description)
            
            if error:
                flash(error, "error")
                return render_template('appointment_create.html', patients=patients,
                                    patient_id=patient_id, date=date, description=description)
            
            flash(f"Appointment created successfully!", "success")
            logger.info(f"Appointment created: ID={appointment.id}, Patient ID={patient_id}")
            return redirect(url_for('list_appointments'))
        
        return render_template('appointment_create.html', patients=patients)
    
    @app.route('/api/patients', methods=['GET'])
    def api_get_patients():
        """API endpoint to get all patients."""
        try:
            patients = patient_repository.get_all()
            return jsonify([p.to_dict() for p in patients])
        except Exception as e:
            logger.error(f"API error getting patients: {e}", exc_info=True)
            return jsonify({'error': 'Internal server error'}), 500
    
    @app.route('/api/appointments', methods=['GET'])
    def api_get_appointments():
        """API endpoint to get all appointments."""
        try:
            appointments = get_appointments_with_patients()
            return jsonify(appointments)
        except Exception as e:
            logger.error(f"API error getting appointments: {e}", exc_info=True)
            return jsonify({'error': 'Internal server error'}), 500
    
    @app.route('/patients/export', methods=['GET'])
    def export_patients():
        """Export patients to CSV."""
        try:
            import csv
            from io import StringIO
            from flask import Response
            
            patients = patient_repository.get_all()
            
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(['ID', 'Name', 'Age', 'Phone', 'Notes'])
            
            for patient in patients:
                writer.writerow([patient.id, patient.name, patient.age, patient.phone, patient.notes])
            
            output.seek(0)
            
            return Response(
                output.getvalue(),
                mimetype='text/csv',
                headers={'Content-Disposition': 'attachment; filename=patients.csv'}
            )
        except Exception as e:
            logger.error(f"Error exporting patients: {e}", exc_info=True)
            flash("An error occurred while exporting patients.", "error")
            return redirect(url_for('list_patients'))

