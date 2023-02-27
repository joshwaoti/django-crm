import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Jeiel9411',
    # auth_plugin='mysql_native_password'
)

# prepare a cursor object

cursorObject = dataBase.cursor()


# create a database
cursorObject.execute("CREATE DATABASE josh")

print("All Done, database created")