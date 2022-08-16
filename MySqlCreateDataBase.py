# ------------------------#
# ----- Create Database---#
# ------------------------#

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="Edsonj*1"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE RemoteData")
