import mysql.connector

data_base_name = "alx_book_store"
mycursor = mydb.cursor()
mycursor.excute(f"CREATE DATABASE IF NOT EXISTS {data_base_name}")
# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="alx_book_store"
)


# Execute SQL statements using the execute() method on the cursor

# Close connection to the databasse  
mycursor.close()
mydb.close()
