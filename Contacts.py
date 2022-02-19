class Contact:

    contact_list = []
    id = 0

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save(self):
        if len(Contact.contact_list) == 0:
            self.id = 1
            Contact.id  = 1
            self.contact_list.append(self)
        else:
            Contact.id += 1
            self.id = Contact.id
            self.contact_list.append(self)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def delete_contact(cls, id):
        for contact in cls.contact_list:
            if contact.id == id:
                cls.contact_list.remove(contact)
                return True
            else: return False

    @classmethod
    def print_contacts(cls):
        for contact in cls.contact_list:
            print(contact.__dict__)
            

    @classmethod
    def clear_all(cls):
        if(len(cls.contact_list) == 0):
                return "Empty"
        else:
            for contact in cls.contact_list:
                cls.contact_list.remove(contact)

    @classmethod
    def find_contact_by_id(cls, id):
        for contact in cls.contact_list:
            if contact.id == id:
                return contact.first_name

    @classmethod
    def find_all_contacts(cls):
        return cls.contact_list
            
            

    
