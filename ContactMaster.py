def contacts_master():
    contacts = {}

    while True:
        print("CONTACT MASTER")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Mark as Favorite")
        print("6. View Favorite Contacts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            if name in contacts:
                print("This contact already exists")
            else:
                age = int(input("Enter age: "))
                phone = int(input("Enter phone number: "))
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
                print("No contacts available")

        elif choice == "5":
            name = input("Enter the name to mark as favorite: ")
            if name in contacts:
                contacts[name]['favorite'] = True
                print(f"Contact {name} marked as favorite.")
            else:
                print("Contact not found")
            
        elif choice == "6":
            favorite_contacts = {name: contact for name, contact in contacts.items() if contact['favorite']}
            if favorite_contacts:
                print("Favorite Contacts:")
                for name, details in favorite_contacts.items():
                    print(f"Name: {name}, Age: {details['age']}, Phone: {details['phone']}, Email: {details['email']}, Favorite: {details['favorite']}")
            else:
                print("No favorite contacts available.")
        
        elif choice == '7':
            print("Exiting Contact Master")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contacts_master()
