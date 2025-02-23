def contacts_master():
    contacts = {}

    while True:
        print("CONTACT MASTER")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            if name in contacts:
                print("This contact already exists.")
            else:
                age = input("Enter age: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                contacts[name] = {'age': age, 'phone': phone, 'email': email}
                print("Contact added successfully!")
        
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted successfully!")
            else:
                print("Contact not found!")
        
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            if name in contacts:
                contact = contacts[name]
                print(f"Name: {'name'},Age: {contact['age']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found!")
        
        elif choice == '4':
            if contacts:
                print("All Contacts:")
                for name, details in contacts.items():
                    print(f"Name: {name}, Age: {details['age']}, Phone: {details['phone']}, Email: {details['email']}")
            else:
                print("No contacts available.")
        
        elif choice == '5':
            print("Exiting Contact Master. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contacts_master()
