import unittest
import main_2

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a function')
        return super().setUp()
    
    def test_do_stuff(self):
        test_param = 10
        result = main_2.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = ('astring')
        result = main_2.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        test_param = None
        result = main_2.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
    
    def test_do_stuff4(self):
        test_param = ''
        result = main_2.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
    
    def tearDown(self):
        print('Cleaning Up')
        return super().tearDown()
        
if __name__ == '__main__':
    unittest.main()    
