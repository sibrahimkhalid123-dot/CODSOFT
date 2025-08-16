import sqlite3

db = sqlite3.connect("contacts.db")
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT,
        address TEXT
    )
""")
db.commit()

# Utility functions
def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                   (name, phone, email, address))
    db.commit()
    print("Contact added successfully.")

def view_contacts():
    cursor.execute("SELECT id, name, phone FROM contacts")
    contacts = cursor.fetchall()
    print("\nContacts:")
    print("-" * 40)
    for contact in contacts:
        print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
    print("-" * 40)

def search_contacts():
    query = input("Search by name or phone: ").strip()
    cursor.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                   (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()
    print("\nSearch Results:")
    for contact in results:
        print(f"ID: {contact[0]} | Name: {contact[1]} | Phone: {contact[2]}")
    if not results:
        print("No matching contacts found.")

def update_contact():
    contact_id = input("Enter contact ID to update: ").strip()
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    contact = cursor.fetchone()
    if not contact:
        print("Contact not found.")
        return

    print("Leave field blank to keep current value.")
    name = input(f"New Name [{contact[1]}]: ").strip() or contact[1]
    phone = input(f"New Phone [{contact[2]}]: ").strip() or contact[2]
    email = input(f"New Email [{contact[3]}]: ").strip() or contact[3]
    address = input(f"New Address [{contact[4]}]: ").strip() or contact[4]

    cursor.execute("""
        UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?
    """, (name, phone, email, address, contact_id))
    db.commit()
    print("Contact updated successfully.")

def delete_contact():
    contact_id = input("Enter contact ID to delete: ").strip()
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    if not cursor.fetchone():
        print("Contact not found.")
        return

    confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
    if confirm == "y":
        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        db.commit()
        print("Contact deleted.")
    else:
        print("Deletion cancelled.")

# Main loop
def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()
db.close()