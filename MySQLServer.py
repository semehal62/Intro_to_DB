import mysql.connector

mycursor = mydb.cursor()
try:
    mycursor.excute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except:
     if err.errno == 1007:  # Error code for "Can't create database; database exists"
            print(f"Database '{database_name}' already exists.")
except mysql.connector.Error as e
    print(e)
else:
    print("Database 'alx_book_store' created successfully! ")
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

finally:
    mycursor.close()  
