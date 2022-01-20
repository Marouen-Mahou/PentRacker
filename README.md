# PentRacker
A desktop application in python that provides some security functionalities.
## Functionalities
- Double factor authentification
- Encoding / Decoding (Base 64, Base 32, Base 16)
- Hashing / Cracking (MD5, SHA1, SHA256)
- Symetric encryption / decryption (DES, AES)
- Asymetric encryption / decryption (EL GAMAL, RSA)
- Secure chat room (AES based)
## Requirements
- MySQL server (dbconnection.py)
- Run SQL commands : 
   ```
  create table users (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , prenom  varchar(50),email varchar(50) NOT NULL UNIQUE ,numero varchar(8) NOT NULL , password varchar(256) NOT NULL ,  code varchar(6) NOT NULL );
  create table clepubs (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , clepub varchar(50) NOT NULL );
  create table messages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , message varchar(150) NOT NULL );
  create table asymmessages (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL , message varchar(150) NOT NULL ,reciever varchar(50) NOT NULL );
  create table active (id  integer PRIMARY KEY AUTO_INCREMENT , nom varchar(50) NOT NULL );
  INSERT INTO `active`(`nom`) VALUES('nouser');
   ```
