import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "byg6zmXp@#$%",
    database = "wsu"
)

my_cursor = connection.cursor()
my_cursor.execute("SELECT * FROM employees")

for i in my_cursor:
    print(i)
