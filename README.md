# Clinic Management System

## Project Description
The **Clinic Management System** is designed to streamline administrative tasks for a clinic. This system, built using Python and SQL, allows for the management of patient records, appointment scheduling, and reservation cancellation. It includes both an admin mode with password protection and a user mode for viewing records and appointments.

## Features

### Admin Mode
Admin mode requires a password (default is `1234`) and allows three attempts before the system shuts down. Once logged in, the admin has access to the following features:
1. **Add New Patient Record**: Admin can add a new patient by entering their name, age, gender, and a unique ID. If the ID already exists, the system rejects the entry.
2. **Edit Patient Record**: Admin can edit a patient's information by entering their ID. The system checks if the ID exists; if not, an error message is displayed.
3. **Reserve a Slot with the Doctor**: Admin can reserve one of the five available time slots for patients (e.g., 2 pm - 5 pm). Once a slot is booked, it will not be available for other patients.
4. **Cancel Reservation**: Admin can cancel a patient's reservation, freeing up the slot for future bookings.

### User Mode
The user mode does not require a password and allows access to the following features:
1. **View Patient Record**: Users can view a patient's details by entering the patient's ID.
2. **View Today’s Reservations**: Users can view all the appointments scheduled for the day.
