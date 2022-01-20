import base64
import hashlib
import tkinter as tk
from dbconnection import DAO

from Crypto.Cipher import AES
from Crypto import Random


class SecretChat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=6)

        menuText = tk.Label(self, text="Secure Chat")
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

        self.fillMessages(room)

        # key
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=0)
        message = tk.Text(self, height=2, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                      insertbackground="#57B947")
        message.grid(row=2, column=1)

        # Encryption button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.sendMessage(message,room, controller),
                              textvariable=menu3_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                              width=10)
        menu3_text.set("Send")
        menu3_btn.grid(column=2, row=2)

        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(2), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=5)

    def sendMessage(self, input,room, controller):
        print(controller.get_email())
        text = input.get("1.0", "end-1c")
        encrypted = self.encrypt(text, "ssi")
        DAO().add_message(DAO().getuser(controller.get_email())[1], encrypted)
        input.delete(1.0,"end")
        room.delete(1.0,"end")
        self.fillMessages(room)

    def fillMessages(self, room):
        print("fill messages")
        room.delete(1.0, "end")
        records = DAO().get_messages()
        for row in records:
            decrypted_message = self.decrypt(row[2], "ssi")
            message = row[1] + ':' + decrypted_message + '\n'
            room.insert(1.0, message)

    def encrypt(self,  message, key):
        message = self._pad(message)
        iv = Random.new().read(AES.block_size)
        key = hashlib.sha256(key.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = base64.b64encode(iv + cipher.encrypt(message.encode()))
        return encrypted

    def decrypt(self, message, key):
        message = base64.b64decode(message)
        iv = message[:AES.block_size]
        key = hashlib.sha256(key.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plain_text = self._unpad(cipher.decrypt(message[AES.block_size:])).decode('utf-8')
        return plain_text

    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]