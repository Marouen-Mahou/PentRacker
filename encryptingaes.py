import base64
import tkinter as tk
import hashlib
import base64

from Crypto.Cipher import AES
from Crypto import Random


class EncryptingAES(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=5)

        menuText = tk.Label(self, text="AES Encrypting")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=3, row=0)

        # message
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=1, column=0)
        message = tk.Text(self, height=5, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                          insertbackground="#57B947")
        message.grid(row=1, column=1)

        output_text = tk.Label(self, text="Output :", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output_text.grid(row=3, column=0)
        output = tk.Text(self, height=2, width=52, relief='flat', bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output.grid(row=3, column=1)

        # key
        tk.Label(self, text="key :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=0)
        key = tk.Text(self, height=2, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                      insertbackground="#57B947")
        key.grid(row=2, column=1)

        # Encryption button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.encrypt(output,message.get("1.0", "end-1c"), key.get("1.0", "end-1c")),
                                                                 textvariable=menu3_text,
                                                                 font=("Anonymous Pro", 14), bg="#57B947", fg="black",
                                                                 width=10)
        menu3_text.set("Encrypt")
        menu3_btn.grid(column=2, row=2)

        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(2), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=4)

    def encrypt(self, output, message, key):
        message = self._pad(message)
        iv = Random.new().read(AES.block_size)
        key = hashlib.sha256(key.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = base64.b64encode(iv + cipher.encrypt(message.encode()))
        output.delete(1.0, "end")
        output.insert(1.0, encrypted)

    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
