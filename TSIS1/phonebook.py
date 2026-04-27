contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})

def show_contacts():
    for c in contacts:
        print(c)

add_contact("Ali", "123")
add_contact("John", "456")

show_contacts()