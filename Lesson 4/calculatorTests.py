import unittest
import calculator

class Tests(unittest.TestCase):

    def AddTests(self):
        self.assertEqual(calculator.Add(3, 6), 9)

    def SubtractTests(self):
        self.assertEqual(calculator.Subtract(10, 4), 6)
        
if __name__ == '__main__':
    unittest.main()