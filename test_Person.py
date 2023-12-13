from Person import Person
import unittest





class TestPerson(unittest.TestCase):
    def test_print_age(self):
        p1 = Person("hamad",44)
        self.assertEqual(p1.getAge(),"The person is an adult.")
        self.assertNotEqual(p1.getAge(), "The person is a child.")
