import mysql.connector

mycursor = mydb.cursor()
try:
    mycursor.excute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except:
     if err.errno == 1007:  # Error code for "Can't create database; database exists"
            print(f"Database '{database_name}' already exists.")
else:
    print("Database 'alx_book_store' created successfully! ")
finally:
    mycursor.close()  
