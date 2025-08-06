import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Store Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("✅ Contact added successfully.")

def view_contacts():
    contacts = load_contacts()
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    print(f"{'No.':<5}{'Name':<25}{'Phone':<15}")
    print("-" * 45)
    for idx, c in enumerate(contacts, 1):
        print(f"{idx:<5}{c['name']:<25}{c['phone']:<15}")

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ").lower()
    contacts = load_contacts()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print(f"\nFound {len(results)} contact(s):")
        for c in results:
            print(f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n{'-'*30}")
    else:
        print("No matching contact found.")

def update_contact():
    print("\n--- Update Contact ---")
    contacts = load_contacts()
    view_contacts()
    if not contacts:
        return
    try:
        idx = int(input("Enter contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            print("Leave blank to keep current value.")
            name = input(f"New Store Name ({contacts[idx]['name']}): ") or contacts[idx]['name']
            phone = input(f"New Phone Number ({contacts[idx]['phone']}): ") or contacts[idx]['phone']
            email = input(f"New Email ({contacts[idx]['email']}): ") or contacts[idx]['email']
            address = input(f"New Address ({contacts[idx]['address']}): ") or contacts[idx]['address']
            contacts[idx] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            print("✅ Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    print("\n--- Delete Contact ---")
    contacts = load_contacts()
    view_contacts()
    if not contacts:
        return
    try:
        idx = int(input("Enter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            confirm = input(f"Are you sure you want to delete '{contacts[idx]['name']}'? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(idx)
                save_contacts(contacts)
                print("✅ Contact deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n" + "="*40)
        print("📒 Contact Manager")
        print("="*40)
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()