from dbconnection import DAO
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
from dbconnection import DAO

import twilio
import re
from functools import partial

import hashlib

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=11)

        image = Image.open("logo.png")
        image = image. resize((100, 100), Image. ANTIALIAS)
        image1 = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=image1)
        label.image = image1

        label.configure(background='black')
        label.grid(columnspan=3,row=0)


        #Login
        loginText = tk.Label(self, text="Register")
        loginText.config(font=("Anonymous Pro", 30))
        loginText.config(fg="#FFFFFF")
        loginText.config(bg="black")
        loginText.grid(column=1, row=1)


        #username
        tk.Label(self, text="Email :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=2, column=1)
        email = tk.StringVar()
        tk.Entry(self, textvariable=email,font=("Anonymous Pro", 12), bg="black",fg="#57B947", insertbackground="#57B947").grid(row=3, column=1)

        #username
        tk.Label(self, text="User Name :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=4, column=1)
        username = tk.StringVar()
        tk.Entry(self, textvariable=username,font=("Anonymous Pro", 12), bg="black",fg="#57B947", insertbackground="#57B947").grid(row=5, column=1)
        # phone
        tk.Label(self, text="Phone Number :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=6, column=1)
        phone = tk.StringVar()
        tk.Entry(self, textvariable=phone, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=7, column=1)

        #password label and password entry box
        tk.Label(self,text="Password :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=8, column=1)
        password = tk.StringVar()
        tk.Entry(self, textvariable=password, show='*',font=("Anonymous Pro", 12), bg="black",fg="#57B947",insertbackground="#57B947").grid(row=9, column=1)

        #password label and password entry box
        tk.Label(self,text="Confirm Password :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=10, column=1)
        confirmPassword = tk.StringVar()
        tk.Entry(self, textvariable=confirmPassword, show='*',font=("Anonymous Pro", 12), bg="black",fg="#57B947",insertbackground="#57B947").grid(row=11, column=1)

        #button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda : self.register(email,username, password, confirmPassword,phone, controller) , textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black")
        connexion_text.set("Register")
        connexion_btn.grid(column=1,row=12)

    def register(self, email, username, password, confirmPassword,phone, controller):
        print("username entered :", username.get())

        print("email enterd:", email.get())
        print("password entered :", password.get())
        print("confirmpassword entered :", confirmPassword.get())

        # Make a regular expression
        # for validating an Email
        emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(not(re.fullmatch(emailregex, email.get()))):
            print("inValid Email")
            raise Exception("inValid Email Format")

        passwordregex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        if(not(re.fullmatch(passwordregex, password.get()))):
            print("inValid password")
            raise Exception("inValid Password Format")
        if((password.get()!= confirmPassword.get())):
            print("inValid password confirmation")
            raise Exception("inValid Password confirmation")

        dao = DAO()
        result = dao.register(username.get(), username.get(), email.get(), password.get(),phone.get())
        if(result):
            self.grid_forget()
            #controller.show_frame(LoginPage)
