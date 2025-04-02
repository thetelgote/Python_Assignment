def hello():
    return "Hello, CI/CD!"

if __name__ == "__main__":
    print(hello())

import unittest
from app import hello

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, CI/CD!")

if __name__ == "__main__":
    unittest.main()

