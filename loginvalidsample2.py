#from stdiomask import getpass
import hashlib
import os
clear=lambda:os.system('cls')


def main():
    clear()
    print("main Menu")
    print("---------")
    print()
    print("1.Register")
    print("2.Login")
    print()
    while True:
        print()
        userChoice=input("Choose An Option")
        if userChoice in ['1','2']:
            break
        if userChoice =='1':
            Register()
        else:
            Login()
def Register():
    clear()
    print("Register")
    print("---------")
    print()
    while True:
        userName=input("Enter your Name:").title()
        if userName !='':
            break
    userName=sanitizeName(userName)
    while True:
        userPassword=input("Enter your password:")
        if userPassword != '':
            break
    while True:
        confirmPassword=input("Confirm your Password:")
        if confirmPassword == userPassword:
            break
        else:
            print("Passwords Don't match")
            print()
    if userAlreadyExist(userName,userPassword):
        while True:
            print()
            error=input("You are already Registered.\n\n Press(T)to try again :\n Press L to login:").lower
            if error=='t':
                Register()
                break
            elif error=='l':
                Login()
                break
    addUserInfo([userName,hash_password(userPassword)]) 
    print()
    print("Registered")
    
def Login():
    clear()
    print("Login")
    print("------")
    print()
    userInfo={}
    with open('userInfo.txt','r') as file:
              for line in file:
                 line =line.split()
                 userInfo.update({line[0]:line[1]})
    while True:
       userName=input("Enter your Name:").title()
       userName=sanitizeName(userName)
       if userName not in userInfo:
              print("You are not registered")
              print()
       else:
              break
       print()
       print("LoggedIn")       
def addUserInfo(userInfo:list):
      with open('userInfo.txt','a') as file:
              for info in userInfo:
                 file.write(info)
                 file.write('')
              file.write('\n')
def userAlreadyExist():
    userInfo={}
    with open('userInfo.txt','r') as file:
        for line in file:
            line = line.split()
            if line[0]==userName and line[1] == userPassword:
               userInfo.update({line[0]:line[1]})
    if userInfo =={}:
              return False
    return userInfo[userName]==userPassword
              
              
def sanitizeName(userName):
    userName=userName.split()
    userName='-'.join(userName)
    return userName          
    
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def check_password_hash(password,hash):
    return hash_password(password)==hash
    
main()
