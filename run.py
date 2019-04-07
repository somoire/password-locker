import random
import string
from user import user
from user import credentials

def create_user(user_name,account_name):
    '''
    Function to create a new user
    '''
    new_user = user(user_name,account_name)
    return new_user

def create_credential(user_password):
    '''
    Function to create a new password
    '''
    new_credential = credentials(user_password)
    return new_credential

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credential(credentials):
    '''
    Function to save password
    '''
    credentials.save_credential()

def del_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def del_credential(credentials):
    '''
    Function to delete credential
    '''
    credentials.delete_credential()

def display_user(user):
    '''
    Function to display a user
    '''
    return user.display_user()

def display_credential(credentials):
    '''
    Function to display a credential
    '''
    return credentials.display_credential()
    









# def randomStringDigits(stringLength=6):
#     password=string.ascii_letters + string.digits
#     lettersAndDigits = string.ascii_letters + string.digits
#     return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
# print (randomStringDigits(12))

