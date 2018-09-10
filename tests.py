from app import *
import unittest


class TestStringMethods(self):
    
    def setUp(self):
        self.duplicate_list = ['Sarah', 'Sarah', 'James', 'Sarah', 'James', 'Kelly', 'Mark']
        self.non_duplicate_list =['Sarah', 'James', 'Kelly', 'Mark']
    
    def test_remove_duplicates(self):
        self.assertEqual((remove_duplicates(self.duplicate_list)), self.non_duplicate_list)
        print("Test passes")
        

if __name__ == '__main__':
    unittest.main()