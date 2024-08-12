#User Registration
from database import *

def signup():
    username = input("Create username: ")
    temp = cursor.execute("SELECT username FROM customer WHERE username=%s",(username,))
    print(temp)