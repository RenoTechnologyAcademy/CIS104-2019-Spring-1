import unittest
import calculator

class TestStringMethods(unittest.TestCase):

    def testAddTests(self):
        self.assertEqual(calculator.Add(3, 6), 9)

    def testSubtractTests(self):
        self.assertEqual(calculator.Subtract(10, 4), 6)

if __name__ == '__main__':
    unittest.main()