# User Manual
**Clinic Management System**

**Version:** 2.0  
**Date:** December 2025

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Patient Management](#patient-management)
4. [Appointment Management](#appointment-management)
5. [Features Guide](#features-guide)
6. [Troubleshooting](#troubleshooting)

---

## Introduction

The Clinic Management System is a web-based application designed to help healthcare providers manage patient records and appointments efficiently. This manual will guide you through all features and functionalities.

---

## Getting Started

### Accessing the Application

1. **Start the Application**
   - The application runs on `http://127.0.0.1:5001`
   - Open your web browser and navigate to this address

2. **Dashboard Overview**
   - The dashboard displays:
     - Total number of patients
     - Total number of appointments
     - Recent patients list
     - Upcoming appointments
     - Quick action buttons

---

## Patient Management

### Adding a New Patient

1. **Navigate to Patients**
   - Click on "Patients" in the navigation bar
   - Or click "Add Patient" from the dashboard

2. **Fill Patient Information**
   - **Name:** Enter patient's full name (required, minimum 2 characters)
   - **Age:** Enter patient's age (required, must be a number between 0-150)
   - **Phone:** Enter phone number (required, 7-15 digits)
   - **Notes:** Optional notes about the patient

3. **Submit**
   - Click "Add Patient" button
   - You'll see a success message if the patient is added successfully
   - You'll see an error message if validation fails

### Viewing Patients

1. **Patient List**
   - Click "Patients" in the navigation bar
   - View all patients in a table format
   - Information displayed:
     - Patient ID
     - Name
     - Age
     - Phone number
     - Notes (truncated if long)

2. **Export Patients**
   - Click "Export CSV" button on the patients page
   - Download a CSV file with all patient data

### Editing a Patient

1. **Access Edit Form**
   - Go to the Patients list
   - Click "Edit" button next to the patient you want to edit

2. **Update Information**
   - Modify any field (name, age, phone, notes)
   - All fields are validated the same way as adding

3. **Save Changes**
   - Click "Save Changes" button
   - You'll be redirected to the patients list with a success message

### Deleting a Patient

1. **Delete Action**
   - Go to the Patients list
   - Click "Delete" button next to the patient
   - Confirm the deletion in the popup dialog

2. **Important Note**
   - Deleting a patient will also delete all associated appointments
   - This action cannot be undone

---

## Appointment Management

### Creating an Appointment

1. **Navigate to Create Appointment**
   - Click "Appointments" in the navigation bar
   - Click "Create Appointment" button
   - Or use the quick action from the dashboard

2. **Fill Appointment Details**
   - **Patient:** Select a patient from the dropdown (required)
   - **Date:** Select appointment date (required, YYYY-MM-DD format)
   - **Description:** Enter appointment description (required, 3-500 characters)

3. **Submit**
   - Click "Create Appointment" button
   - You'll see a success message if created successfully
   - You'll see an error message if validation fails

### Viewing Appointments

1. **Appointment List**
   - Click "Appointments" in the navigation bar
   - View all appointments in a table format
   - Information displayed:
     - Appointment ID
     - Patient name and details
     - Appointment date
     - Description

### Searching Appointments

1. **Search Functionality**
   - On the Appointments page, use the search form:
     - **Search Description:** Enter keywords to search in appointment descriptions
     - **Filter by Date:** Select a specific date to filter appointments

2. **Using Search**
   - Enter search term and/or select date
   - Click "Search" button
   - Results will be filtered accordingly
   - Click "Clear Filters" to reset

---

## Features Guide

### Navigation

- **Dashboard:** Main page with overview statistics
- **Patients:** Manage patient records
- **Appointments:** Manage appointments

### Flash Messages

The application provides feedback through flash messages:
- **Success (Green):** Operation completed successfully
- **Error (Red):** Something went wrong, check the message
- **Info (Blue):** Informational messages

### Form Validation

All forms include validation:
- **Required Fields:** Marked with red asterisk (*)
- **Error Messages:** Displayed if validation fails
- **Help Text:** Guidance below each field

### Responsive Design

The application is responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

---

## Troubleshooting

### Common Issues

#### Issue: "Patient not found" error
**Solution:** 
- Ensure the patient exists in the system
- Check if the patient was deleted
- Refresh the page and try again

#### Issue: Validation errors when adding patient
**Solution:**
- Check that all required fields are filled
- Ensure age is a number between 0-150
- Verify phone number contains only digits (7-15 characters)
- Name must be at least 2 characters

#### Issue: Cannot create appointment
**Solution:**
- Ensure at least one patient exists in the system
- Check that date is in YYYY-MM-DD format
- Verify description is between 3-500 characters
- Ensure selected patient exists

#### Issue: Search not working
**Solution:**
- Try clearing filters and searching again
- Check date format if filtering by date
- Ensure search term is spelled correctly

#### Issue: Page not loading
**Solution:**
- Check that the application server is running
- Verify you're accessing the correct URL (http://127.0.0.1:5001)
- Check browser console for errors
- Try refreshing the page

### Browser Compatibility

The application works best with:
- Chrome (recommended)
- Firefox
- Edge
- Safari

### Data Persistence

**Important:** The current version stores data in memory. This means:
- Data is lost when the server restarts
- Data is not shared between different browser sessions
- For production use, database integration is recommended

---

## Keyboard Shortcuts

- **Tab:** Navigate between form fields
- **Enter:** Submit forms
- **Escape:** Close modals/dialogs

---

## Best Practices

### Patient Management
1. **Use Full Names:** Enter complete patient names for better identification
2. **Accurate Phone Numbers:** Ensure phone numbers are correct for contact
3. **Add Notes:** Use notes field for important patient information
4. **Regular Updates:** Keep patient information up to date

### Appointment Management
1. **Clear Descriptions:** Use descriptive appointment descriptions
2. **Future Dates:** Use future dates for upcoming appointments
3. **Regular Review:** Review and manage appointments regularly
4. **Search Feature:** Use search to quickly find specific appointments

---

## Support

For technical support or questions:
- Review the README.md file
- Check the documentation in the docs/ folder
- Contact the development team

---

## Version History

- **Version 2.0 (December 2025):** Refactored version with modern UI and features
- **Version 1.0:** Initial legacy version

---

**Last Updated:** December 2025  
**Prepared by:** Development Team

