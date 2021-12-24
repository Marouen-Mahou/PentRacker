import tkinter as tk
from PIL import  ImageTk, Image  
from functools import partial

root = tk.Tk()
root.configure(bg="black")

canvas = tk.Canvas(root, width=800, height=500)
canvas.configure(background='black')
canvas.grid(columnspan=3, rowspan=8)


#Logo 
logo = Image.open('logo.png')
logo = logo. resize((200, 200), Image. ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.configure(background='black')
logo_label.grid(column=1, row=0)

#Login
loginText = tk.Label(root, text="Connexion")
loginText.config(font=("Anonymous Pro", 30))
loginText.config(fg="#FFFFFF")
loginText.config(bg="black")
loginText.grid(column=1, row=1)


#username
usernameLabel = tk.Label(root, text="User Name :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=2, column=1)
username = tk.StringVar()
usernameEntry = tk.Entry(root, textvariable=username,font=("Anonymous Pro", 12), bg="black",fg="#57B947", insertbackground="#57B947").grid(row=3, column=1)

#password label and password entry box
passwordLabel = tk.Label(root,text="Password :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=4, column=1)  
password = tk.StringVar()
passwordEntry = tk.Entry(root, textvariable=password, show='*',font=("Anonymous Pro", 12), bg="black",fg="#57B947",insertbackground="#57B947").grid(row=5, column=1) 


def login(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    
login = partial(login, username, password)

#button
connexion_text = tk.StringVar()
connexion_btn = tk.Button(root, command=lambda:login(), textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black")
connexion_text.set("Login")
connexion_btn.grid(column=1,row=6)



root.mainloop()









