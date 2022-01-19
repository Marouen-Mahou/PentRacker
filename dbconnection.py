import mysql.connector
import hashlib


class DataBaseConnection:
    pass


class DataBaseConnection:
    __shared_instance = None

    def getConnection(host, user, password, database):
        if DataBaseConnection.__shared_instance is None:
            DataBaseConnection.__shared_instance = mysql.connector.connect(host=host, user=user, password=password,
                                                                           database=database)
        return DataBaseConnection.__shared_instance

    def __init__(self):

        """virtual private constructor"""
        if DataBaseConnection.__shared_instance != None:
            raise Exception("This class is a singleton class !")
        else:
            DataBaseConnection = self


class DAO:
    def __init__(self):

        self.db = DataBaseConnection.getConnection(
            host="localhost",
            user="root",
            password="",
            database="ssi")

    def createTable(self):
        # faire quelque chose d'utile avec la connexion
        with self.db.cursor() as c:
            c.execute(
                "create table users (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , prenom  varchar(50),email varchar(50) NOT NULL UNIQUE ,numero varchar(8) NOT NULL , password varchar(256) NOT NULL ,  code varchar(6) NOT NULL );"
            )
        self.db.commit()

    def register(self, nom, prenom, email, password, phone):

        hash_object = hashlib.sha256(bytes(password, encoding='utf-8'))

        with self.db.cursor() as c:
            query = ("select * from users where email ='%s'" % (email))
            c.execute(query)
            records = c.fetchall()

            if c.rowcount != 0:
                raise Exception("email already used ")

        with self.db.cursor() as c:
            query = ("insert into users(nom,prenom,email,password,numero) values ( '%s' , '%s' , '%s' , '%s','%s' )" % (
                nom, prenom, email, hash_object.hexdigest(), phone))
            print(query)
            c.execute(query)
        self.db.commit()
        return True

    def login(self, email, password):
        hash_object = hashlib.sha256(bytes(password, encoding='utf-8'))

        with self.db.cursor() as c:
            query = ("select * from users where email ='%s'" % (email))
            c.execute(query)
            records = c.fetchall()
            print(c.rowcount)
            print(email)
            if c.rowcount == 0:
                print("user doesn't exist")
            else:
                for row in records:
                    hashedPassword = row[5]

                if (hashedPassword == hash_object.hexdigest()):
                    print("login done")
                    return True
                else:
                    print("false credential")

    def getuser(self, email,):
        with self.db.cursor() as c:
            query = ("select * from users where email ='%s'" % (email))
            c.execute(query)
            records = c.fetchall()
            if c.rowcount == 0:
                print("user doesn't exist")
            else:
                for row in records:
                    return row

    def update_verifcode(self, email, code):
        with self.db.cursor() as c:
            query = ("update users set code='%s' where email ='%s'" % (code, email))
            c.execute(query)
        self.db.commit()

    def verify_code(self, email, code):

        with self.db.cursor() as c:
            query = ("select * from users where email ='%s'" % (email))
            c.execute(query)
            records = c.fetchall()
            print(c.rowcount)
            print(email)
            if c.rowcount == 0:
                print("user doesn't exist")
            else:
                for row in records:
                    oldcode = row[6]

                if (oldcode == code):
                    print("verification done")
                    return True
                else:
                    print("not verified")