import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Jeiel9411'
)

# prepare a cursor object

cursorObject = dataBase.cursor()


# create a database
cursorObject.execute("CREATE DATABASE josh")

print("All Done, database created")