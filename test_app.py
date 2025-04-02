import unittest
from app import hello

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, CI/CD!")

if _name_ == "_main_":
    unittest.main()
