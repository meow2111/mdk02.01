import unittest
from hello import greet
class TestGreet (unittest.TestCase):
    def test_simple(self):
         self.assertEqual(greet("Соня"), "Привет, Соня!")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")

if __name__ == "__main__":
    unittest.main()