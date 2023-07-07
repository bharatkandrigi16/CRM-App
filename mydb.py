import MySQLdb as mysql_db

database = mysql_db.connect(
    host = 'localhost:3306',
    user = 'root',
    passwd = '$Nylonkitties$'
)

#Cursor object
cursor = database.cursor()

#Create database
cursor.execute("CREATE DATABASE elderco")

print("Database created!")