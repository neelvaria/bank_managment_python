#User Registration
from database import *
import random
from customer import *
from bank import Bank

def signup():
    username = input("Create username: ")
    temp = db_query(f"SELECT username FROM customer WHERE username='{username}';")
    if temp:
        print("Username is already taken")
        signup()
    else:
        print("Username available")
        password = input("Create password: ")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter your city: ")
        while True:
            acc_number = int(random.randint(a:=10000000,b:=99999999))
            temp = db_query(f"SELECT acc_number FROM customer WHERE acc_number= '{acc_number}';")
            if temp:
                continue
            else:
                print("Your Account number will be: ",acc_number)
                break
    obj = customer(username,password,name,age,city,acc_number)
    obj.create_user()
    bobj = Bank(username,acc_number)
    bobj.createtransaction_table()
    
def signin():
    username = input("Enter username: ")
    temp = db_query(f"SELECT username FROM customer WHERE username='{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()}, Enter password: ")
            temp = db_query(f"SELECT password FROM customer WHERE username='{username}';")
            #print(temp[0][0])
            if temp[0][0] == password:
                print("Login successful")
                return username
            else:
                print("Incorrect password")
                continue

    else:
        print("Username not found")
        signin()
    