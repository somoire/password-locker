#!/usr/bin/env python3.6
import unittest
import random
import string
from user import User
from user import credentials

def create_user(user_name,account_name):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,account_name)
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

def display_user():
    '''
    Function to display a user
    '''
    return User.display_user()

def display_credential():
    '''
    Function to display a credential
    '''
    return credentials.display_credentials()


def main():
        print("Welcome to your password locker.Please input your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')
        while True:
                print("run either of this codes according to your preference: ss - Sign-up a new account, dc - display accounts generated, fd -find an account, quit -close the password locker ")

                short_code = input().lower()

                if short_code == 'ss':
                        print("New account")
                        print("-"*10)

                        print ("user name ....")
                        user_name = input()

                        print("account name ...")
                        account_name = input()
                        save_user(create_user(user_name,account_name)) # create and save new user.
                        
                        print("type own-to generate your own password or random-to randomly generate a password")
                        user_password=input()
        
                        if user_password == 'own': 
                                print("enter password")
                                passwordtype=input() 
                                print("your user name is " + user_name, "for " + account_name,"your password is " + passwordtype)
                        
                        elif user_password =='random':
                                def randomStrings(stringLength):
                                        lettersAndDigits = string.ascii_letters + string.digits
                                        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
       
                                user_password = randomStrings(8)
                                print("your user name is " + user_name, "for " + account_name,"your password is " + user_password)
                        

                                save_credential(create_credential(user_password)) # create and save newcredential.


                           
                        print ('\n')
                        print(f"New account {user_name} {account_name} {user_password}  created")
                        print ('\n')

                elif short_code == 'dc':
                        if display_user():
                                print("There you go")
                                print('\n')

                                for user in display_user():
                                        print(f"{user.user_name} {user.account_name} .....")
                                        print('\n')
                                
                                for credentials in display_credential():
                                        print(f"{credentials.user_password}  .....")
                                        print('\n')
                        else:
                                print('\n')
                                print("Currently there are no existent accounts.")
                                print('\n')

                elif short_code == 'fd':
                        print("Key in the account username you want to search for")
                        search_account = input()
                        if(search_account):
                                search_account =(search_account)
                                print(f"{search_account.user_name} {search_account.account_name}")
                                print('-' * 20)

                                print(f"account name.......{search_account.account.name}")
                                print(f"user name.......{search_account.user_name}")
                        else:
                                print("Kindly verify that the account really exists from the user.")

                elif short_code == 'quit':
                            print("Thank you for visiting password locker;-)")
                            break
        else:
                print("Kindly use the specified codes to be able to run password locker")
if __name__ == '__main__':
        main()