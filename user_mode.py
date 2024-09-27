from functions import *

def show_reservations_for_patient():
    """Show all reservations for a specific patient."""
    patient_id = int(input("Enter Patient ID: "))
    reservations = get_reservations_by_patient(patient_id)
    
    if reservations:
        print(f"\nReservations for Patient ID {patient_id}:")
        for reservation in reservations:
            print(f"Reservation ID: {reservation[0]}")
            print(f"Slot Time: {reservation[1]}")
            print(f"Date: {reservation[2]}")
            print("--------")
    else:
        print(f"No reservations found for Patient ID {patient_id}")

def user_mode():
    """User mode menu."""
    while True:
        print("\nUser Mode:")
        print("1. View Patient Record")
        print("2. View Today's Reservations")
        print("3. View Reservations by Patient ID")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            patient_id = int(input("Enter Patient ID: "))
            view_patient(patient_id)
        
        elif choice == "2":
            view_todays_reservations()
        
        elif choice == "3":
            show_reservations_for_patient()
        
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")
