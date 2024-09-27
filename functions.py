import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="121314",
    database="clinic_management"  # replace with your actual database name
)
cursor = conn.cursor()

# Define default slots as start times only
DEFAULT_SLOTS = [
    "14:00",
    "14:30",
    "15:00",
    "16:00",
    "16:30"
]

def get_available_slots(date):
    """Fetch available slots for a given date."""
    cursor.execute("SELECT slot_time FROM reservation WHERE date = %s", (date,))
    reserved_slots = cursor.fetchall()
    reserved_slots = [slot[0] for slot in reserved_slots]

    available_slots = [slot for slot in DEFAULT_SLOTS if slot not in reserved_slots]
    return available_slots

def reserve_slot(reservation_id, patient_id, slot_time, date):
    """Reserve a slot for a patient if available."""
    available_slots = get_available_slots(date)
    if slot_time not in available_slots:
        print("This slot is already reserved. Please choose another slot.")
        return False
    
    cursor.execute("INSERT INTO reservation (reservation_id, patient_id, slot_time, date) VALUES (%s, %s, %s, %s)", 
                   (reservation_id, patient_id, slot_time, date))
    conn.commit()
    print("Slot reserved successfully")
    return True

def add_patient(patient_id, name, age, gender):
    """Add a new patient record."""
    cursor.execute("INSERT INTO patient (patient_id, name, age, gender) VALUES (%s, %s, %s, %s)", 
                   (patient_id, name, age, gender))
    conn.commit()
    print("Patient added successfully")

def edit_patient(patient_id, new_name=None, new_age=None, new_gender=None):
    """Edit an existing patient record."""
    if new_name:
        cursor.execute("UPDATE patient SET name = %s WHERE patient_id = %s", (new_name, patient_id))
    if new_age:
        cursor.execute("UPDATE patient SET age = %s WHERE patient_id = %s", (new_age, patient_id))
    if new_gender:
        cursor.execute("UPDATE patient SET gender = %s WHERE patient_id = %s", (new_gender, patient_id))
    conn.commit()
    print("Patient record updated")

def cancel_reservation(reservation_id):
    """Cancel an existing reservation."""
    cursor.execute("DELETE FROM reservation WHERE reservation_id = %s", (reservation_id,))
    conn.commit()
    print("Reservation canceled")

def view_patient(patient_id):
    """View a patient's details."""
    cursor.execute("SELECT * FROM patient WHERE patient_id = %s", (patient_id,))
    patient = cursor.fetchone()
    if patient:
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Gender:", patient[3])
    else:
        print("Patient not found")

def view_todays_reservations():
    """View all reservations for today."""
    cursor.execute("SELECT * FROM reservation WHERE date = CURDATE()")
    reservations = cursor.fetchall()
    if reservations:
        for reservation in reservations:
            print("Reservation ID:", reservation[0])
            print("Patient ID:", reservation[1])
            print("Slot Time:", reservation[2])
            print("Date:", reservation[3])
            print("--------")
    else:
        print("No reservations for today")

def get_reservations_by_patient(patient_id):
    """View reservations for a specific patient by their ID."""
    cursor.execute("SELECT reservation_id, slot_time, date FROM reservation WHERE patient_id = %s", (patient_id,))
    reservations = cursor.fetchall()
    return reservations
