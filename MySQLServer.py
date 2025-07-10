import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (default: localhost, user=root, no password)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='matthew@42166223'  # Add your password if you have one
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
