#Customer Details
from database import *

class customer:
    def __init__(self,username,password,name,age,city,acc_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__acc_number = acc_number
        
    def create_user(self):
        db_query(f"INSERT INTO CUSTOMER VALUES('{self.__username}','{self.__password}','{self.__name}','{self.__age}','{self.__city}','{self.__acc_number}',1);")
        mydb.commit()