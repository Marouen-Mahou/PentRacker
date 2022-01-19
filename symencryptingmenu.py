
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
import base64
from Crypto.cipher import DES

import hashlib



class SymEncryptingMenu(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=5)


        menuText = tk.Label(self, text="DES Encrypting")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=3, row=0)

        #message
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=1, column=0)
        message = tk.Text(self, height=5, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                    insertbackground="#57B947")
        message.grid(row=1, column=1)

        output_text = tk.Label(self, text="Output :", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output_text.grid(row=3, column=0)
        output = tk.Label(self, relief='flat', text="", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output.grid(row=3, column=1)

        # key
        tk.Label(self, text="key :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=0)
        key = tk.Text(self, height=2, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                    insertbackground="#57B947")
        key.grid(row=2, column=1)


        # Encryption button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: print(message.get("1.0", "end-1c")), textvariable=menu3_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu3_text.set("Encrypt")
        menu3_btn.grid(column=2, row=2)

        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(3), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=4)

    def encrypt(self, message, key,):
        cipher = DES.new(key, DES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message.encode('ascii'))
        print(nonce)
        print(ciphertext)
        print(tag)