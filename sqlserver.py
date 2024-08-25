import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "byg6zmXp@#$%",
    database = "sibuta_book_store"
)

my_cursor = connection.cursor()
my_cursor.execute("SHOW DATABASES")
#employees = my_cursor.fetchall()

for i in my_cursor:
    print(i)
