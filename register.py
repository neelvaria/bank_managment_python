#User Registration
from database import *
import random
from customer import *

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
                print("Account number generated: ",acc_number)
                break
    obj = customer(username,password,name,age,city,acc_number)
    obj.create_user() 