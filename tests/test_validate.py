import unittest
from validate import  validate_num, validate_str, validate_email


class TestValidate(unittest.TestCase):
    """
        A class for unit-testing function in the validate.py file
        It inherits from the unittest module
	""" 
    def setUp(self):
        self.test = {'validate_num':{'test':8990, 'expected_output':True},
                    'validate_str':{'test':9943, 'expected_output':False},
                    'validate_email':{'test':'jksrt@main', 'expected_output':False}}

    def test_validate_num(self):
        self.assertEqual(validate_num(self.test['validate_num']['test']), 
                                self.test['validate_num']['expected_output'])

    def test_validate_str(self):
        self.assertEqual(validate_str(self.test['validate_str']['test']), 
                                self.test['validate_str']['expected_output'])

    def test_validate_email(self):
        self.assertEqual(validate_email(self.test['validate_email']['test']), 
                                self.test['validate_email']['expected_output'])


if __name__ == '__main__':
	unittest.main()