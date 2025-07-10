import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='matthew@42166223'  # Update if needed
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

