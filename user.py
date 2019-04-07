import random
import string
class user:
    '''
    class that generates new instance of a user
    '''
    user_list=[]

    def _init_(self,user_name,account_name):
        self.user_name=user_name
        self.account_name=account_name

user_name=input("Input your username ")

account_name=input("Type your account name: ")


class credentials:
    '''
    class that generates new password
    '''
    credentials_list=[]
    def _init_(self,user_password):
        self.user_password=user_password 
print("type own-to generate your own password or random-to randomly generate a password")
passwordtype=input()

if passwordtype=='own':
    print("Key in your password")
    passwordtype=input() 
    print("your user name is " + user_name, "for " + account_name,"your password is " + passwordtype)
    
elif passwordtype=='random':
    

    def randomStringDigits(stringLength):
        password = string.ascii_letters + string.digits
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
        # randomStringDigits(12)

print("your user name is " + user_name, "for " + account_name," your random password is " + randomStringDigits(12))
