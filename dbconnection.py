import mysql.connector
import hashlib




class DataBaseConnection :

    __shared_instance = None

    def getConnection(host,user,password,database) : 
        if DataBaseConnection.__shared_instance  == None : 
            DataBaseConnection.__shared_instance=mysql.connector.connect(host=host,user=user,password=password, database=database)
        return DataBaseConnection.__shared_instance 

    def __init__(self):
 
        """virtual private constructor"""
        if DataBaseConnection.__shared_instance != None :
            raise Exception ("This class is a singleton class !")
        else:
            DataBaseConnection = self
    


class DAO :
    def __init__(self) :
        
        self.db= DataBaseConnection.getConnection( 
            host="localhost",
            user="root",
            password="",
            database="ssi")

    def createTable(self) : 
        # faire quelque chose d'utile avec la connexion
            with self.db.cursor() as c:
                c.execute("create table users (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , prenom  varchar(50),email varchar(50) NOT NULL UNIQUE  , password varchar(256) NOT NULL)")
            self.db.commit()
        

    def register ( self, nom , prenom , email , password) : 
          
            hash_object = hashlib.sha256(bytes(password, encoding='utf-8'))
            

            with self.db.cursor() as c:
                query =("select * from users where email ='%s'"%(email))
                c.execute(query)
                records = c.fetchall()
                
                if c.rowcount!= 0 : 
                    raise Exception("email already used ")
                
 
            with self.db.cursor() as c:
                query =( "insert into users(nom,prenom,email,password) values ( '%s' , '%s' , '%s' , '%s' )" %(nom , prenom ,email , hash_object.hexdigest()))
                print(query)
                c.execute(query)
            self.db.commit()
            return True
            
    def login (self,email,password) : 
            hash_object = hashlib.sha256(bytes(password, encoding='utf-8'))
            
            with self.db.cursor() as c:
                query =("select * from users where email ='%s'"%(email))
                c.execute(query)
                records = c.fetchall()
                print(c.rowcount)
                print(email)
                if c.rowcount== 0 : 
                    print("user doesn't exist")
                else :
                    for row in records:
                        hashedPassword  =  row[4] 
                    if(hashedPassword == hash_object.hexdigest()) :
                        print("login done")
                        return True
                    else : 
                        print("false credential")

            
            


