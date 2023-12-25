import uuid

class Contact:
    def __init__(self, first_name, last_name, phone_number, city):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numbers = [phone_number]
        self.city = city

class Phonebook:
    def __init__(self):
        self.contacts = {}
        self.deleted_contacts = {}

    def add(self, first_name, last_name, phone_number, city):
        if len(first_name) >= 2 and len(last_name) >= 1 and self._validate_phone_number(phone_number):
            contact = Contact(first_name, last_name, phone_number, city)
            self.contacts[contact.id] = contact
            return contact.id
        else:
            raise ValueError("Invalid input parameters")

    def find_by_lastname(self, ln):
        for contact in self.contacts.values():
            if contact.last_name == ln:
                yield contact

    def find_id(self, contact_id):
        return self.contacts.get(contact_id)

    def remove(self, contact_id):
        contact = self.contacts.pop(contact_id, None)
        if contact:
            self.deleted_contacts[contact_id] = contact
        return contact

    def restore(self, contact_id):
        contact = self.deleted_contacts.pop(contact_id, None)
        if contact:
            self.contacts[contact_id] = contact
            return True
        return False

    def add_phone(self, contact_id, new_phone_number):
        contact = self.contacts.get(contact_id)
        if contact and self._validate_phone_number(new_phone_number):
            contact.phone_numbers.append(new_phone_number)
            return True
        return False

    def group_by(self, arg):
        result = {}
        if arg == 'city':
            for contact in self.contacts.values():
                result.setdefault(contact.city, []).append(contact)
        elif arg == 'lastname':
            for contact in self.contacts.values():
                result.setdefault(contact.last_name, []).append(contact)
        return result

    def _validate_phone_number(self, phone_number):
        return len(phone_number) == 10 and phone_number[:2].isdigit() and phone_number[2] == '-' and phone_number[3:].isdigit()


# Example usage:
phonebook = Phonebook()

# Add contacts
contact1_id = phonebook.add("hamad", "abo", "123-4567890", "City1")
contact2_id = phonebook.add("mohamad", "sbet", "456-7890123", "City2")

# Add another phone to a contact
phonebook.add_phone(contact1_id, "987-6543210")

# Find contacts by last name
for contact in phonebook.find_by_lastname("Doe"):
    print(contact.first_name, contact.last_name)

# Remove a contact
removed_contact = phonebook.remove(contact2_id)

# Restore a contact
phonebook.restore(contact2_id)

# Group contacts by city
grouped_by_city = phonebook.group_by("city")
print(grouped_by_city)

# Group contacts by last name
grouped_by_lastname = phonebook.group_by("lastname")
print(grouped_by_lastname)
