from app import *
import unittest


class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.duplicate_list = ['Sarah', 'Sarah', 'James', 'Sarah', 'James', 'Kelly', 'Mark']
        self.non_duplicate_list =['Sarah', 'James', 'Kelly', 'Mark']
    
    def test_remove_duplicates(self):
        self.assertEqual((remove_duplicates(self.duplicate_list)), self.non_duplicate_list)
        print("Test 'test_remove_duplicates' passes")
        

if __name__ == '__main__':
    unittest.main()