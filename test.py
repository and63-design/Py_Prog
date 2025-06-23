import unittest
import main 

class TestGame(unittest.TestCase):
    def test_input(self):
        #result = main.run_guess(5, 4)
        result = main.run_guess(5, 5)
        self.assertTrue(result)
    
    def test_input_invalid(self):
        #result = main.run_guess(2, 5)
        result = main.run_guess(15, 5)
        self.assertIsNone(result)

if __name__ == '__main__':
        unittest.main()