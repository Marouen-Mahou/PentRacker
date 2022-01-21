import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
from dotenv import load_dotenv
import os


from dbconnection import DAO

from functools import partial

from decodepage import DecodePage
from encodepage import EncodePage
from encryptingaes import EncryptingAES
from homepage import HomePage
from rsa import EncDecRsa
from gamal import EncDecGAMAL
from loginpage import LoginPage
from doubleFA import DoubleFA
import hashlib
# re module provides support
# for regular expressions
import re

from encodingmenu import EncodingMenu
from hashingmenu import HashingMenu
from symencryptingmenu import SymEncryptingMenu
from encryptingdes import EncryptingDES
from decryptingdes import DecryptingDES

from decryptingaes import DecryptingAES

from asymencryptingmenu import AsymEncryptingMenu
from crackingmenu import CrackingMenu
from registerpage import RegisterPage

from secretchat import SecretChat
from asymsecretchat import AsymSecretChat

LARGEFONT =("Verdana", 35)

load_dotenv()


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.email= None
        ico = Image.open('logo.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        self.title(" PentRacker ")

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.resizable(False, False)

        # initializing frames to an empty array
        self.frames = [LoginPage, RegisterPage, HomePage, EncodingMenu,
                       HashingMenu, CrackingMenu, SymEncryptingMenu, AsymEncryptingMenu,
                       EncodePage,DecodePage,DoubleFA, EncryptingDES,
                       DecryptingDES, EncryptingAES, DecryptingAES, SecretChat,
                       EncDecRsa,EncDecGAMAL,AsymSecretChat
                       ]

        # iterating through a tuple consisting
        # of the different page layouts
        # initializing frame of that object from
        # startpage, page1, page2 respectively with
        # for loop

        self.show_frame(0)

    # to display the current frame passed as
    # parameter
    def show_frame(self, ind):
        frame = self.frames[ind](self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def get_email(self):
        return self.email

    def set_email(self,email):
        self.email=email

# first window frame startpage










# Driver Code
app = tkinterApp()
app.mainloop()


















