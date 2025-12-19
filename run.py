"""
Run script for Clinic Management System.
"""

from app import app, initialize_sample_data

if __name__ == '__main__':
    # Initialize sample data
    initialize_sample_data()
    
    # Run the application
    app.run(debug=True, host='127.0.0.1', port=5001)

