from register import *

while True:
    try:
        register = int(input("""1. Register\n 2. Login\n 3. Exit\n Enter your choice: """))
        
        if register == 1 or register == 2:
            if register == 1:
               signup() 
        
        else:
            print("Invalid Input Try Again from Number!!")
            
    except ValueError:
        print("Invalid Input Try Again!!")