import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="root",database="Bank")

cursor = mydb.cursor()
def create_customer():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Customer
               (username varchar(50),
               password varchar(25),
               name varchar(50),
               age INTEGER,
               city varchar(50),
               acc_number INTEGER,
               status BOOLEAN)
            """)

    mydb.commit()


if __name__ == "__main__":
    create_customer()