import unittest
from Contacts import Contact

class ContactTest(unittest.TestCase):
    def test_instance_creates_successfully(self):
        person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
        self.assertTrue(isinstance(person_x, Contact))

    def test_save_contact(self):
        Contact.clear_all()
        person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
        person_x.save()
        self.assertEqual(len(Contact.contact_list),1)
        self.assertEqual(Contact.contact_list[0].first_name, person_x.first_name)

    def test_delete_contact(self):
        Contact.clear_all()
        person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
        person_x.save()
        self.assertEqual(Contact.delete_contact(1), True)

    def test_find_contact_by_id(self):
        Contact.clear_all()
        person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
        person_x.save()
        self.assertEqual(person_x.first_name,  Contact.find_contact_by_id(1))

    def test_fullname(self):
        person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
        self.assertEqual(person_x.full_name,"Allan Walker")

    def test_find_all_contacts(self):
        self.assertEqual(len(Contact.contact_list), len(Contact.find_all_contacts()))







if __name__ == "__main__":
    unittest.main()