
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image


class SymEncryptingMenu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=2, rowspan=4)

        #Login
        menuText = tk.Label(self, text="Symetric")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=2, row=0)

        #Coding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu1_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu1_text.set("Encrypt DES")
        menu1_btn.grid(column=0,row=1)

        #Decoding button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu2_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu2_text.set("Encrypt AES256")
        menu2_btn.grid(column=1,row=1)

        #Decoding button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu3_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu3_text.set("Decrypt DES")
        menu3_btn.grid(column=0,row=2)

        #Decoding button
        menu4_text = tk.StringVar()
        menu4_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu4_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu4_text.set("Decrypt AES256")
        menu4_btn.grid(column=1,row=2)

        #Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(2), textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=2,row=3)
