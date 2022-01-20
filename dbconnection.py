import pymysql.cursors
import hashlib


class DataBaseConnection:
    pass


class DataBaseConnection:
    __shared_instance = None

    def getConnection(host, user, password, database):
        if DataBaseConnection.__shared_instance is None:
            DataBaseConnection.__shared_instance = pymysql.connect(host=host, user=user, password=password,
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
            c.execute(
                "create table clepubs (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , clepub varchar(50) NOT NULL );"
            )
            c.execute(
                "create table messages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , message varchar(150) NOT NULL );"
            )
            c.execute(
                "create table asymmessages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , message varchar(150) NOT NULL ,reciever varchar(50) NOT NULL );"
            )

            c.execute(
                "create active messages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL );"
            )
            c.execute(
                "INSERT INTO `active`(`nom`) VALUES('nouser');"
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
                raise Exception("User doesn't exist")
            else:
                for row in records:
                    hashedPassword = row[5]

                if (hashedPassword == hash_object.hexdigest()):
                    print("login done")
                    self.set_active_user(row[1])
                    return True
                else:
                    print("false credential")
                    raise Exception("False Credentials")


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

    def update_pubkey(self, username, pubkey):
        with self.db.cursor() as c:
            query = ("select * from clepubs where nom ='%s'" % (username))
            c.execute(query)
            records = c.fetchall()
            if c.rowcount == 0:
                query = ("insert into clepubs ( nom, clepub) values ('%s'  , '%s') " % (username, pubkey))
                c.execute(query)
            else :
                query = ("update clepubs set clepub='%s' where nom ='%s'" % (username, pubkey))
                c.execute(query)
        self.db.commit()

    def get_pubkey(self, username):
        with self.db.cursor() as c:
            query = ("select * from clepubs where nom ='%s'" % (username))
            c.execute(query)
            records = c.fetchall()
            if c.rowcount == 0:
                print("user doesn't exist")
            else:
                for row in records:
                    return row[2]

    def verify_code(self, email, code):

        with self.db.cursor() as c:
            query = ("select * from users where email ='%s'" % (email))
            c.execute(query)
            records = c.fetchall()
            print(c.rowcount)
            print(email)
            if c.rowcount == 0:
                print("User doesn't exist")
                raise Exception("User doesn't exist")
            else:
                for row in records:
                    oldcode = row[6]

                if (oldcode == code):
                    print("verification done")
                    return True
                else:
                    print("Not verified")
                    raise Exception("Not verified")

    def add_message(self, nom, message):
        with self.db.cursor() as c:
            query = ('insert into messages(nom,message) values ( "%s" , "%s" )' % (
                nom, message.decode("utf-8")))
            print(query)
            c.execute(query)
        self.db.commit()
        return

    def add_asymmessage(self, nom, message,username):
        with self.db.cursor() as c:
            query = ('insert into asymmessages(nom,message,reciever) values ( "%s" , "%s","%s" )' % (
                nom, message.decode("utf-8"),username))
            print(query)
            c.execute(query)
        self.db.commit()
        return

    def get_messages(self):
        with self.db.cursor() as c:
            query = "select * from messages"
            c.execute(query)
            records = c.fetchall()
            return records

    def get_asymessages(self, username):
        with self.db.cursor() as c:
            query = 'select * from asymmessages where reciever  ="%s" '%(username)
            c.execute(query)
            records = c.fetchall()
            return records
    def set_active_user(self, nom):
        with self.db.cursor() as c:
            query = ("update active set nom='%s' where id ='%s'" % (nom, '1'))
            c.execute(query)
        self.db.commit()

    def unset_active_user(self):
        with self.db.cursor() as c:
            query = ("update active set nom='%s' where id ='%s'" % ("nouser", '1'))
            c.execute(query)
        self.db.commit()

    def get_active_user(self):
        with self.db.cursor() as c:
            query = "select * from active"
            c.execute(query)
            records = c.fetchall()
            return records[0][1]