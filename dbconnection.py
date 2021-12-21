import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ssi"
)

# faire quelque chose d'utile avec la connexion
with db.cursor() as c:
        c.execute("create table MAROUEN (id  varchar(20) , name varchar(50) , email varchar(50)  , password varchar(20))")
        db.commit()
print(db.ping())
db.close()