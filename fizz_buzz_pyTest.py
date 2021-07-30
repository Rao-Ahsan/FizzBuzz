import unittest
from fizz_buzz import func_fizz_buzz

class TeseFizzBuzz(unittest.TestCase):

    def test_func_fizz_buzz(self):
        self.assertEqual(func_fizz_buzz(3), [1,2,'Fizz'])

if __name__ == '__main__':
    unittest.main()
