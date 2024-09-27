from admin_mode import admin_mode
from user_mode import user_mode

def main():
    """Main menu to choose between admin and user modes."""
    while True:
        print("\nClinic Management System")
        print("1. Admin Mode")
        print("2. User Mode")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            admin_mode()
        
        elif choice == "2":
            user_mode()
        
        elif choice == "3":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
