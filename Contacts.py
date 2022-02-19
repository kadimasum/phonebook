# Read though Contact.txt to understand our goal
# This is our contact class. It contains all our methods and data for now in a list. In future the data will e stored in a database
class Contact:

    # The contact_list acts as our database for now
    contact_list = []
    
    # id has been initialized at class level so that we can access it and update it for every instance
    id = 0

    # Our initialization method allows us to create objects/instances
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    
    # Our save method saves the contact to the contact_list which acts as our database
    def save(self):
        if len(Contact.contact_list) == 0:
            self.id = 1
            Contact.id  = 1
            self.contact_list.append(self)
        else:
            Contact.id += 1
            self.id = Contact.id
            self.contact_list.append(self)

    # The full name method allows us to access the full name for every instance
    # The @property decorator allows us to access full_name as a property rather than as a method
    # We are passing in self as an argument. Self refers to the instance 
    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    # We create a method to delete a contact by id. Rememer when we were saving our instance we added an id to the instance in our save method. We are now accessing that id.
    @classmethod
    def delete_contact(cls, id):
        for contact in cls.contact_list:
            if contact.id == id:
                cls.contact_list.remove(contact)
                return True
            else: return False

    # Here we print all contacts in the list as a dictionary
    # The @classmethod decorator tells python that this method belongs to the class
    @classmethod
    def print_contacts(cls):
        for contact in cls.contact_list:
            print(contact.__dict__)
            
    # This method allows us to clear the whole list
    @classmethod
    def clear_all(cls):
        if(len(cls.contact_list) == 0):
                return "Empty"
        else:
            for contact in cls.contact_list:
                cls.contact_list.remove(contact)

    # This method allows us to find contact by id. For this case we are only returning the first name
    @classmethod
    def find_contact_by_id(cls, id):
        for contact in cls.contact_list:
            if contact.id == id:
                return contact.first_name

    # This method returns all saved contacts in a list
    @classmethod
    def find_all_contacts(cls):
        return cls.contact_list

    # We can use this method to update first_name after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its first name
    @classmethod
    def update_first_name(cls, id, name):
        for contact in cls.contact_list:
            if contact.id == id:
                contact.first_name = name

    # We can use this method to update last_name after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its last name
    @classmethod
    def update_last_name(cls, id, name):
        for contact in cls.contact_list:
            if contact.id == id:
                contact.last_name = name

    # We can use this method to update phone_number after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its phone_number
    @classmethod
    def update_phone_number(cls, id, phone_number):
        for contact in cls.contact_list:
            if contact.id == id:
                contact.phone_number = phone_number

    # We can use this method to update email after we have saved our instance in the list
    # We loop through the list and find the instance with the id that matches the one we are interested in changing its email
    @classmethod
    def update_email(cls, id, email):
        for contact in cls.contact_list:
            if contact.id == id:
                contact.email = email


            
            

    
