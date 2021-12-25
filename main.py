import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image  
from functools import partial
  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        ico = Image.open('logo.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.resizable(False, False)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginPage, RegisterPage, HomePage, Menu1Page, Menu2Page, Menu3Page, Menu4Page, Menu5Page):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(LoginPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        self.configure(bg="black")
        
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=8)
        
        image = Image.open("logo.png")
        image = image. resize((200, 200), Image. ANTIALIAS)
        image1 = ImageTk.PhotoImage(image)
        
        label = tk.Label(self, image=image1)
        label.image = image1
        
        label.configure(background='black')
        label.grid(columnspan=3,row=0)

        
        #Login
        loginText = tk.Label(self, text="Connexion")
        loginText.config(font=("Anonymous Pro", 30))
        loginText.config(fg="#FFFFFF")
        loginText.config(bg="black")
        loginText.grid(column=1, row=1)
        
        
        #username
        tk.Label(self, text="User Name :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=2, column=1)
        username = tk.StringVar()
        tk.Entry(self, textvariable=username,font=("Anonymous Pro", 12), bg="black",fg="#57B947", insertbackground="#57B947").grid(row=3, column=1)
        
        #password label and password entry box
        tk.Label(self,text="Password :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=4, column=1)  
        password = tk.StringVar()
        tk.Entry(self, textvariable=password, show='*',font=("Anonymous Pro", 12), bg="black",fg="#57B947",insertbackground="#57B947").grid(row=5, column=1)      
        
        #button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda : self.login(username, password, controller) , textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black")
        connexion_text.set("Login")
        connexion_btn.grid(column=1,row=6)
        
        #button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda : self.register(controller) , textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black")
        connexion_text.set("Register")
        connexion_btn.grid(column=1,row=7)
    
    def login(self, username, password, controller):
        print("username entered :", username.get())
        print("password entered :", password.get())
        controller.show_frame(HomePage)
    
    def register(self, controller):
        controller.show_frame(RegisterPage)
        

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
        
        #password label and password entry box
        tk.Label(self,text="Password :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=6, column=1)  
        password = tk.StringVar()
        tk.Entry(self, textvariable=password, show='*',font=("Anonymous Pro", 12), bg="black",fg="#57B947",insertbackground="#57B947").grid(row=7, column=1)
        
        #password label and password entry box
        tk.Label(self,text="Confirm Password :",bg="black",fg="#57B947",font=("Anonymous Pro", 12)).grid(row=8, column=1)  
        confirmPassword = tk.StringVar()
        tk.Entry(self, textvariable=confirmPassword, show='*',font=("Anonymous Pro", 12), bg="black",fg="#57B947",insertbackground="#57B947").grid(row=9, column=1)    
        
        #button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda : self.register(email,username, password, confirmPassword, controller) , textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black")
        connexion_text.set("Register")
        connexion_btn.grid(column=1,row=10)
    
    def register(self, email, username, password, confirmPassword, controller):
        print("username entered :", username.get())
        print("email enterd:", email.get())
        print("password entered :", password.get())
        print("confirmpassword entered :", confirmPassword.get())
        controller.show_frame(LoginPage)
  
        
  
  
# second window frame page1
class HomePage(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="black")
        
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=2, rowspan=8)
        
        #Login
        menuText = tk.Label(self, text="Menu")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=2, row=0)
        
        #Coding / Decoding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda : controller.show_frame(Menu1Page) , textvariable=menu1_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu1_text.set("Encoding/Decoding a message")
        menu1_btn.grid(column=0,row=1)
        
        #Hash button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda : controller.show_frame(Menu2Page)  , textvariable=menu2_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu2_text.set("Hash a message")
        menu2_btn.grid(column=1,row=1)
        
        #Crack button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda : controller.show_frame(Menu3Page)  , textvariable=menu3_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu3_text.set("Crack a message")
        menu3_btn.grid(column=0,row=2)
        
        #Encypt / Decrypt button
        menu4_text = tk.StringVar()
        menu4_btn = tk.Button(self, command=lambda : controller.show_frame(Menu4Page) , textvariable=menu4_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu4_text.set("Symetric Encrypt/Decrypt")
        menu4_btn.grid(column=1,row=2)
        
        #Crack button
        menu5_text = tk.StringVar()
        menu5_btn = tk.Button(self, command=lambda : controller.show_frame(Menu5Page) , textvariable=menu5_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu5_text.set("Asymetric Encrypt/Decrypt")
        menu5_btn.grid(column=0,row=3)
        
        #Encypt / Decrypt button
        menu6_text = tk.StringVar()
        menu6_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu6_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu6_text.set("Secure Chat")
        menu6_btn.grid(column=1,row=3)
        
        #Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(LoginPage) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Disconnect")
        quit_btn.grid(columnspan=2,row=5)
        
        
# second window frame page1
class Menu1Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="black")
        
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=2, rowspan=3)
        
        #Login
        menuText = tk.Label(self, text="Encode / Decode")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=2, row=0)
        
        #Coding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu1_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu1_text.set("Encoding a message")
        menu1_btn.grid(column=0,row=1)
        
        #Decoding button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu2_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu2_text.set("Encoding a message")
        menu2_btn.grid(column=1,row=1)
        
        #Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(HomePage) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=2,row=2)
        
class Menu2Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="black")
        
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=2, rowspan=4)
        
        #Login
        menuText = tk.Label(self, text="Hash")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=2, row=0)
        
        #Coding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu1_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu1_text.set("MD5")
        menu1_btn.grid(column=0,row=1)
        
        #Decoding button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu2_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu2_text.set("SHA1")
        menu2_btn.grid(column=1,row=1)
        
        #Decoding button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu3_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu3_text.set("SHA256")
        menu3_btn.grid(column=0,row=2)
        
        #Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(HomePage) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=2,row=3)
        
class Menu3Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="black")
        
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=2, rowspan=4)
        
        #Login
        menuText = tk.Label(self, text="Crack")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=2, row=0)
        
        #Coding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu1_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu1_text.set("MD5")
        menu1_btn.grid(column=0,row=1)
        
        #Decoding button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu2_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu2_text.set("SHA1")
        menu2_btn.grid(column=1,row=1)
        
        #Decoding button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda : print("1") , textvariable=menu3_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu3_text.set("SHA256")
        menu3_btn.grid(column=0,row=2)
        
        #Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(HomePage) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=2,row=3)
        
        
class Menu4Page(tk.Frame):
     
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
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(HomePage) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=2,row=3)
        
class Menu5Page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        self.configure(bg="black")
        
        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=2, rowspan=4)
        
        #Login
        menuText = tk.Label(self, text="Asymetric")
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
        quit_btn = tk.Button(self, command=lambda : controller.show_frame(HomePage) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=2,row=3)
        
  
# Driver Code
app = tkinterApp()
app.mainloop()


















