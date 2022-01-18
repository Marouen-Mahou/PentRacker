import tkinter as tk
from PIL import ImageTk, Image

from dbconnection import DAO
from homepage import HomePage
from registerpage import RegisterPage


class DoubleFA(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent)
        self.configure(bg="black")
        self.parent=parent

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=8)

        image = Image.open("logo.png")
        image = image.resize((150, 150), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=image1)
        label.image = image1

        label.configure(background='black')
        label.grid(columnspan=3, row=0)

        # Validation
        validationText = tk.Label(self, text="2FA validation ")
        validationText.config(font=("Anonymous Pro", 30))
        validationText.config(fg="#FFFFFF")
        validationText.config(bg="black")
        validationText.grid(column=1, row=1)

        # hint
        hintText = tk.Label(self, text="your verification code has been sent to your email and your phone")
        hintText.config(font=("Anonymous Pro", 20))
        hintText.config(fg="#FFFFFF")
        hintText.config(bg="black")
        hintText.grid(column=1, row=1)

        # username
        tk.Label(self, text="email :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=1)
        email = tk.StringVar()
        tk.Entry(self, textvariable=email, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=3, column=1)
        # code
        tk.Label(self, text="Authentification Code :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=4, column=1)
        code = tk.StringVar()
        tk.Entry(self, textvariable=code, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=5, column=1)

        # button
        verif_text = tk.StringVar()
        verif_btn = tk.Button(self, command=lambda: self.verify(email,code, controller),
                                  textvariable=verif_text, font=("Anonymous Pro", 14), bg="#57B947", fg="black")
        verif_text.set("Verify")
        verif_btn.grid(column=1, row=6)

        # button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda: self.register(controller), textvariable=connexion_text,
                                  font=("Anonymous Pro", 14), bg="#57B947", fg="black")
        connexion_text.set("Return")
        connexion_btn.grid(column=1, row=7)

    def verify(self,email,code , controller):

        dao = DAO()
        result = dao.verify_code(email.get(), code.get())
        if (result):
            print("hello")
            controller.show_frame(2)




