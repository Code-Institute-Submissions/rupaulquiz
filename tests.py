from app import *
import unittest

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.empty_list = []
        self.duplicate_list = ['Sarah', 'Sarah', 'James', 'Sarah', 'James', 'Kelly', 'Mark']
        self.non_duplicate_list = ['Sarah', 'James', 'Kelly', 'Mark']
        self.duplicate_list_two = ['Sarah', '£$^%$&$%&£', 'Sarah', '£$^%$&$%&£', 'James', 'Sarah', 'James', '8', 'Kelly', 'Mark', 'Tears for Fears', 'Mark', '332323443', '£$^%$&$%&£']
        self.non_duplicate_list_two = ['Sarah', '£$^%$&$%&£', 'James', '8', 'Kelly', 'Mark', 'Tears for Fears', '332323443']


    def test_tests(self):
        """Tests that the tests themselves are working"""
        self.assertEqual(100, 100)
        print("Test 'test_tests' passes")
    
    
    def test_home_status(self):
        """Tests the status of the home page"""
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            print("Test 'test_home_status' passes")
            """Tests the home page is not .json"""
            self.assertFalse(response.is_json)
            print("Confirms homepage is not .json")
            
            
    def test_bad_route(self):
        """Tests bad route from home page"""
        with app.test_client() as client:
            response = client.get('/sarah/sjdjdjree')
            self.assertEqual(response.status_code, 404)
            print("Test 'test_bad_route' passes")
            
            
    def test_page_status(self):
        """Tests the status of the each page is 200, not 404"""
        with app.test_client() as client:
                
            response = client.get('/index.html')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/quiz.html')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/score_bestfriend.html')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            response = client.get('/scorefrenemies.html')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)

            response = client.get('/score_squirrelfriends.html')
            self.assertEqual(response.status_code, 200)
            self.assertNotEqual(response.status_code, 404)
            
            print("Test 'test_page_status' passes")
    

    def test_remove_duplicates(self):
        """Compares empty lists"""
        self.assertEqual((remove_duplicates(self.empty_list)), self.empty_list)
        print("Empty 'test_remove_duplicates' with empty passes")
        
        """Compares simple lists to see if duplicates have been removed"""
        self.assertEqual((remove_duplicates(self.duplicate_list)), self.non_duplicate_list)
        print("Test 'test_remove_duplicates' with first list passes")
        
        """Compares more complicated lists to see if duplicates have been removed"""
        self.assertEqual((remove_duplicates(self.duplicate_list_two)), self.non_duplicate_list_two)
        print("Test 'test_remove_duplicates' with second list passes")
        
        """Compares two lists, which do not have duplicates removed, are not equal"""
        self.assertNotEqual((remove_duplicates(self.duplicate_list)), self.non_duplicate_list_two)
        print("Test 'test_remove_duplicates' with not equal lists passes")
        

if __name__ == '__main__':
    unittest.main()