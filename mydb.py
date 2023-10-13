import mysql.connector
from mysql.connector import errorcode

try:
    dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password123',
        auth_plugin='mysql_native_password'
    )
    print("it Works!")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username and password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("DataBase does not exist")
    else:
        print(e)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE django")

print("ALL Done!")