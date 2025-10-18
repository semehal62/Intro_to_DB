import mysql.connector


mycursor = mydb.cursor()
mycursor.excute("CREATE DATABASE IF NOT EXISTS alx_book_store")
# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    
)


# Execute SQL statements using the execute() method on the cursor

# Close connection to the databasse  
mycursor.close()
mydb.close()
