import unittest
from Contacts import Contact

class ContactTest(unittest.TestCase):
    def test_instance_creates_successfully(self):
        person_x = Contact("Allan", "Walker", "076563738", "allanwarker@gmail.com")
        self.assertTrue(isinstance(person_x, Contact))


if __name__ == "__main__":
    unittest.main()