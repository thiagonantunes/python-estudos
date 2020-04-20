import mysql.connector

mydb = mysql.connector.connect(
    host ='127.0.0.1',
    port = 3306,
    user ='root',
    password = '',
    database="cadastro"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM gafanhotos LIMIT 3")
resultado = cursor.fetchall()

for x in resultado:
    print(x)