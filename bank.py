#Bank Service
from database import *
import datetime 

class Bank:
    
    def __init__(self,username,acc_number):
        self.__username = username
        self.__acc_number = acc_number
        
    def createtransaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
                 f"(timedate varchar(50),"
                 f"acc_number INTEGER,"
                 f"remarks varchar(50),"
                 f"amount INTEGER)")
    
    def balance(self):
        temp = db_query(f"SELECT balance FROM customer WHERE username = '{self.__username}';")
        print(f"{self.__username} Balance is {temp[0][0]}")
        
    def deposit(self,amount):
        temp = db_query(f"SELECT balance FROM customer WHERE username = '{self.__username}';")
        
        test = amount + temp[0][0]
        db_query(f"UPDATE customer SET balance='{test}' WHERE username = '{self.__username}';")
        self.balance()
        
        db_query(f"INSERT INTO {self.__username}_transaction VALUES("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__acc_number}',"
                    f"'Amount Deposit',"
                    f"'{amount}')")
        print(f"{self.__username} Amount is Succesfully Deposited to your Account {self.__acc_number}")
    
    def withdraw(self,amount):
        temp = db_query(f"SELECT balance FROM customer WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance")
        else:
            test = temp[0][0] - amount 
            db_query(f"UPDATE customer SET balance='{test}' WHERE username = '{self.__username}';")
            self.balance()
            
            db_query(f"INSERT INTO {self.__username}_transaction VALUES("
                        f"'{datetime.datetime.now()}',"
                        f"'{self.__acc_number}',"
                        f"'Amount Withdraw',"
                        f"'{amount}')")
            print(f"{self.__username} Amount is Succesfully Deposited to your Account {self.__acc_number}")
            
    def transfer(self,sender_acc_number,amount):
        temp = db_query(f"SELECT balance FROM customer WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance")
        else:
            temp2 = db_query(f"SELECT balance FROM customer WHERE acc_number = '{sender_acc_number}';")
            test1 = temp[0][0] - amount            
            test2 = temp2[0][0] + amount
            db_query(f"UPDATE customer SET balance='{test1}' WHERE username = '{self.__username}';")

            db_query(f"UPDATE customer SET balance='{test2}' WHERE acc_number = '{sender_acc_number}';")
            self.balance()
            
            db_query(f"INSERT INTO {self.__username}_transaction VALUES("
                        f"'{datetime.datetime.now()}',"
                        f"'{self.__acc_number}',"
                        f"'Amount Transfer -> {sender_acc_number}',"
                        f"'{amount}')")
            print(f"{self.__username} Amount is Transaction from your Account {self.__acc_number}")
            
            receiver_username = db_query(f"SELECT username FROM customer WHERE acc_number = '{sender_acc_number}';")
            db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES("
                        f"'{datetime.datetime.now()}',"
                        f"'{sender_acc_number}',"
                        f"'Amount Transfer -> {self.__acc_number}',"
                        f"'{amount}')")
        
        
                        