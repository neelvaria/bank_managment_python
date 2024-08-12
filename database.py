import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="root",database="Bank")

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def create_customer():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Customer
               (username varchar(50) NOT NULL,
               password varchar(25) NOT NULL,
               name varchar(50) NOT NULL,
               age INTEGER NOT NULL,
               city varchar(50) NOT NULL,
               acc_number INTEGER NOT NULL,
               balance INTEGER NOT NULL,
               status BOOLEAN)
            """)

    mydb.commit()


if __name__ == "__main__":
    create_customer()