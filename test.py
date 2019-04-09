import unittest
import pyperclip
import random
import string
from user import User
from user import credentials

class Testuser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Tash","Gmail") # create contact object


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Tash")
        self.assertEqual(self.new_user.account_name,"Gmail")
        

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Tash","Gmail") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a User object
        self.assertEqual(len(User.user_list),1)

   
        
    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_user(),User.user_list)

    def test_search_all_users(self):
        '''
        method that allows users to search accounts
        '''

        self.assertEqual(User.display_user(),User.user_list)


class Testcredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = credentials("yuyt6ty9") # create contact object


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            credentials.credentials_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_password,"yuyt6ty9")
      
        

    def test_save_credential(self):
        '''
        test_save_credentials test case to test if the user object is saved into
         the user list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(credentials.credentials_list),1)

    
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a user from our user list
        '''
        self.new_credential.save_credential()
        test_credential = credentials("yuyt6ty9") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(credentials.credentials_list),1)

   
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(credentials.display_credentials(),credentials.credentials_list)

    def test_search_all_credentials(self):
        '''
        method that allows users to search passwords
        '''

        self.assertEqual(credentials.display_credentials(),credentials.credentials_list)

        

if __name__ == '__main__':
    unittest.main()