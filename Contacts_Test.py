# This file contains all our tests
# We import unittest to allow us to access its TestCase subclass, inherit it in our ContactTest class and use it to run our tests
import unittest
from Contacts import Contact

class ContactTest(unittest.TestCase):
    # Setup method runs before every test
    def setUp(self):
        self.person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
 
    # Teardown method runs after every test
    def tearDown(self):
        Contact.clear_all()

    # Test if instance is created(The __init__ method)
    def test_instance_creates_successfully(self):
        self.assertTrue(isinstance(self.person_x, Contact))

    # Test that contact is saved successfully
    def test_save_contact(self):
        self.person_x.save()
        self.assertEqual(len(Contact.contact_list),1)
        self.assertEqual(Contact.contact_list[0].first_name, self.person_x.first_name)

    # Test that contact is deleted successfully
    def test_delete_contact(self):
        self.person_x.save()
        self.assertEqual(Contact.delete_contact(1), True)

    # Test that it is possible to find contact by id
    def test_find_contact_by_id(self):
        self.person_x.save()
        self.assertEqual(self.person_x.first_name,  Contact.find_contact_by_id(1))

    # Test that it is possile to return the full name
    def test_fullname(self):
        self.assertEqual(self.person_x.full_name,"Allan Walker")

    #  Test that we can use our method to find all contacts
    def test_find_all_contacts(self):
        self.assertEqual(len(Contact.contact_list), len(Contact.find_all_contacts()))

    # Test that contact information can be updated successfully
    def test_update_contact(self):
        self.person_x.save()

        Contact.update_first_name(1, "Paulo")
        Contact.update_email(1, "paulowalker@gmail.com")
        Contact.update_last_name(1, "Samuel")
        Contact.update_phone_number(1, "06573467")

        self.assertEqual(self.person_x.first_name, "Paulo")
        self.assertEqual(self.person_x.email, "paulowalker@gmail.com")
        self.assertEqual(self.person_x.last_name, "Samuel")
        self.assertEqual(self.person_x.phone_number, "06573467")






if __name__ == "__main__":
    unittest.main()