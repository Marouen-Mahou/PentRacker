import tkinter as tk

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
        menu1_btn = tk.Button(self, command=lambda : controller.show_frame(3) , textvariable=menu1_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu1_text.set("Encoding/Decoding a message")
        menu1_btn.grid(column=0,row=1)

        #Hash button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda : controller.show_frame(4), textvariable=menu2_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu2_text.set("Hash a message")
        menu2_btn.grid(column=1,row=1)

        #Crack button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda : controller.show_frame(5), textvariable=menu3_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu3_text.set("Crack a message")
        menu3_btn.grid(column=0,row=2)

        #Encypt / Decrypt button
        menu4_text = tk.StringVar()
        menu4_btn = tk.Button(self, command=lambda :  controller.show_frame(6) , textvariable=menu4_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu4_text.set("Symetric Encrypt/Decrypt")
        menu4_btn.grid(column=1,row=2)

        #Crack button
        menu5_text = tk.StringVar()
        menu5_btn = tk.Button(self, command=lambda :  controller.show_frame(7) , textvariable=menu5_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu5_text.set("Asymetric Encrypt/Decrypt")
        menu5_btn.grid(column=0,row=3)

        #Encypt / Decrypt button
        menu6_text = tk.StringVar()
        menu6_btn = tk.Button(self, command=lambda : controller.show_frame(15) , textvariable=menu6_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 30)
        menu6_text.set("Secure Chat")
        menu6_btn.grid(column=1,row=3)
        # Encypt / Decrypt button
        #menu6_text = tk.StringVar()
        #menu6_btn = tk.Button(self, command=lambda: controller.show_frame(18), textvariable=menu6_text,
        #                      font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=30)
        #menu6_text.set("Asym Secure Chat")
        #menu6_btn.grid(column=1, row=4)

        #Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda :  controller.show_frame(0) , textvariable=quit_text, font=("Anonymous Pro", 14), bg="#57B947",fg="black", width = 20)
        quit_text.set("Disconnect")
        quit_btn.grid(columnspan=2,row=4)

