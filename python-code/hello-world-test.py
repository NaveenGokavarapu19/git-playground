import unittest
from hello import HelloWorld

class UnitTest(unittest.TestCase):
    def test_display(self):
        instance = HelloWorld()
        message = instance.print_message()
        print(message)
        self.assertEqual("Hello world","Hello world")



if __name__== "__main__":
    unittest.main()


