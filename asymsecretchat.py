import base64
import binascii
import hashlib
import tkinter as tk
from dbconnection import DAO
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class AsymSecretChat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="black")
        self.dao=None
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=5)

        menuText = tk.Label(self, text="Asym Secure Chat")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=3, row=0)

        # message
        tk.Label(self, text="Room :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=1, column=0)
        room = tk.Text(self, height=15, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                          insertbackground="#57B947")
        room.grid(row=1, column=1)

        self.fillMessages(room,controller)

        # key
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=3, column=0)
        message = tk.Text(self, height=2, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                      insertbackground="#57B947")
        message.grid(row=3, column=1)

        # key
        tk.Label(self, text="Username :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=0)
        user = tk.Text(self, height=2, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                      insertbackground="#57B947")
        user.grid(row=2, column=1)

        # Encryption button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.sendMessage(message,room,self.dao.getuser(controller.get_email())[1],controller),
                              textvariable=menu3_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                              width=10)
        menu3_text.set("Send")
        menu3_btn.grid(column=2, row=2)

        # Refresh button
        menu4_text = tk.StringVar()
        menu4_btn = tk.Button(self, command=lambda: self.fillMessages(room,controller),
                              textvariable=menu4_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                              width=10)
        menu4_text.set("Refresh")
        menu4_btn.grid(column=2, row=3)

        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(2), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=4)

        print("*********************")
        print(controller.get_email())

        print("*********************")

        # RSA key generation
        self.keyPair = RSA.generate(2048)
        self.pubKey = self.keyPair.publickey()
        print(f"Public key: \n (n={hex(self.pubKey.n)}, \n e={hex(self.pubKey.e)})")
        print(f"Private key:\n (n={hex(self.pubKey.n)}, \n d={hex(self.keyPair.d)})")
        self.dao=DAO()
        self.username=self.dao.getuser(controller.get_email())[1]
        self.dao.update_pubkey(self.username,self.pubKey)


    def sendMessage(self, input,room,username,controller):
        text = input.get("1.0", "end-1c")
        pub_key=self.dao.get_pubkey(username)
        encrypted = self.encrypt(text, pub_key)
        DAO().add_asymmessage(self.username, encrypted,username)
        input.delete(1.0,"end")
        room.delete(1.0,"end")
        self.fillMessages(room,controller)

    def fillMessages(self, room,controller):
        records = DAO().get_asymessages(DAO().getuser(controller.get_email())[1])
        for row in records:
            decrypted_message = self.decrypt(row[2], self.keyPair)
            message = row[1] + ':' + decrypted_message + '\n'
            room.insert(1.0, message)

    def encrypt(self,  message, key):
        print(message)
        print(key)
        encryptor = PKCS1_OAEP.new(key)
        encrypted = encryptor.encrypt(bytes(message, 'utf-8'))
        encrypted = binascii.hexlify(encrypted)
        return encrypted

    def decrypt(self, message, key):

        decryptor = PKCS1_OAEP.new(key)
        decrypted = decryptor.decrypt(binascii.unhexlify(message))
        plain_text =decrypted
        return plain_text

    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]