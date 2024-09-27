from functions import *

def admin_login(password):
    """Authenticate admin user."""
    default_password = "1234"
    attempts = 0
    while attempts < 3:
        if password == default_password:
            print("Login successful!")
            return True
        else:
            attempts += 1
            password = input("Incorrect password. Try again: ")
    print("Too many failed attempts. Access denied.")
    return False

def reserve_slot_for_patient():
    """Reserve a slot for a patient."""
    patient_id = int(input("Enter Patient ID: "))
    date = input("Enter Date (YYYY-MM-DD): ")
    
    available_slots = get_available_slots(date)
    if not available_slots:
        print("No available slots for the selected date.")
        return
    
    print("Available slots:")
    for slot in available_slots:
        # Show the full slot range to the admin
        print(f"{slot}-{(int(slot[:2]) + (1 if slot[-2:] == '00' else 0)) % 24}:{'00' if slot[-2:] == '30' else '30'}")
    
    slot_time = input("Enter the desired slot start time from the above options (e.g., 14:00): ")
    
    if slot_time not in available_slots:
        print("Invalid slot time selected.")
        return
    
    reservation_id = int(input("Enter Reservation ID: "))
    
    success = reserve_slot(reservation_id, patient_id, slot_time, date)
    if success:
        print("Reservation successful.")

def admin_mode():
    """Admin mode menu."""
    if admin_login(input("Enter admin password: ")):
        while True:
            print("\nAdmin Mode:")
            print("1. Add Patient")
            print("2. Edit Patient")
            print("3. Reserve Slot")
            print("4. Cancel Reservation")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                patient_id = int(input("Enter Patient ID: "))
                name = input("Enter Patient Name: ")
                age = int(input("Enter Patient Age: "))
                gender = input("Enter Patient Gender: ")
                add_patient(patient_id, name, age, gender)
            
            elif choice == "2":
                patient_id = int(input("Enter Patient ID to edit: "))
                new_name = input("Enter new name (leave blank to keep current): ")
                new_age = input("Enter new age (leave blank to keep current): ")
                new_gender = input("Enter new gender (leave blank to keep current): ")
                edit_patient(patient_id, new_name, new_age, new_gender)
            
            elif choice == "3":
                reserve_slot_for_patient()
            
            elif choice == "4":
                reservation_id = int(input("Enter Reservation ID to cancel: "))
                cancel_reservation(reservation_id)
            
            elif choice == "5":
                break
            else:
                print("Invalid option. Please try again.")
