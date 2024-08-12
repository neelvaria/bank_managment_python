from register import *
from bank import *
status = False

while True:
    try:
        register = int(input("""1. Register\n 2. Login\n 3. Exit\n Enter your choice: """))
        
        if register == 1 or register == 2:
            if register == 1:
               signup() 
            
            if register == 2:
                user = signin()
                status = True
                break
        
        else:
            print("Invalid Input Try Again from Number!!")
            
    except ValueError:
        print("Invalid Input Try Again!!")
        
acc_num = db_query(f"SELECT acc_number from customer WHERE username = '{user}';")
#print(acc_num[0][0])

while status:
    print(f"Welcome!! {user.capitalize()} Choose your Banking facality")
    try:
        facality = int(input("1. Balance\n" 
                            "2. Cash Deposit\n" 
                            "3. Cash Withdrawal\n"
                            "4. Fund Transfer\n" 
                            "Enter your choice: "))
        
        if facality >= 1 or register <= 5:
            if facality == 1:
                bobj = Bank(user,acc_num[0][0])
                bobj.balance()
                            
            elif facality == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit: "))
                        bobj = Bank(user,acc_num[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Invalid Input Try Again!!")
                        continue
            
            elif facality == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw: "))
                        bobj = Bank(user,acc_num[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Invalid Input Try Again!!")
                        continue
            
            elif facality == 4:
                while True:
                    try:
                        sender_acc_number = int(input("Enter Sender Account Number: "))
                        amount = int(input("Enter a Amount to Transfer: "))

                        bobj = Bank(user,acc_num[0][0])
                        bobj.transfer(sender_acc_number,amount)
                        mydb.commit()
                        break
        
                    except ValueError:
                        print("Invalid Input Try Again!!")
                        continue
            elif facality == 5:
                print("Thanks For Using Banking Services")
                status = False
              
        else:
            print("Invalid Input Try Again from Number!!")
            continue
            
    except ValueError:
        print("Invalid Input Try Again!!")
        continue