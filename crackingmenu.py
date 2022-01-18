import tkinter as tk
import hashlib
from tkinter import filedialog


class CrackingMenu(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(bg="black")

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=6)

        # Login
        menuText = tk.Label(self, text="Hash")
        menuText.config(font=("Anonymous Pro", 30))
        menuText.config(fg="#FFFFFF")
        menuText.config(bg="black")
        menuText.grid(columnspan=3, row=0)

        # Input field
        tk.Label(self, text="Message :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=1, column=0)

        T = tk.Text(self, height=5, width=52, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                    insertbackground="#57B947")
        T.grid(row=1, column=1)

        # file input button
        fileinput_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda: self.select_file(selected_file_root),
                              textvariable=fileinput_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        fileinput_text.set("File")
        menu1_btn.grid(column=0, row=3)

        selected_file_root = tk.Label(self, relief='flat', text="", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        selected_file_root.grid(row=3, column=1)

        #output field
        output_text = tk.Label(self, text="Output :", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output_text.grid(row=4, column=0)
        output = tk.Label(self, relief='flat', text="", bg="black", fg="#57B947", font=("Anonymous Pro", 12))
        output.grid(row=4, column=1)

        # Coding button
        menu1_text = tk.StringVar()
        menu1_btn = tk.Button(self, command=lambda: self.hash(T, output, output_text, "MD5"), textvariable=menu1_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu1_text.set("MD5")
        menu1_btn.grid(column=0, row=2)

        # Decoding button
        menu2_text = tk.StringVar()
        menu2_btn = tk.Button(self, command=lambda: self.hash(T, output, output_text, "SHA1"), textvariable=menu2_text,
                              font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu2_text.set("SHA1")
        menu2_btn.grid(column=1, row=2)

        # Decoding button
        menu3_text = tk.StringVar()
        menu3_btn = tk.Button(self, command=lambda: self.hash(T, output, output_text, "SHA256"),
                              textvariable=menu3_text, font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=10)
        menu3_text.set("SHA256")
        menu3_btn.grid(column=2, row=2)

        # Quit button
        quit_text = tk.StringVar()
        quit_btn = tk.Button(self, command=lambda: controller.show_frame(2), textvariable=quit_text,
                             font=("Anonymous Pro", 14), bg="#57B947", fg="black", width=20)
        quit_text.set("Return")
        quit_btn.grid(columnspan=3, row=5)

    def select_file(self, selected_file_root):
        global  selected_file
        selected_file = filedialog.askopenfilename(title='Open a file',initialdir='./files',filetypes=(
        ('text files', '*.txt'),
        ('All files', '*.*')
    ))
        selected_file_root.config(text=selected_file)

    def hash(self, input, out, out_text, type):
        message = input.get("1.0", "end-1c")

        file1 = open(selected_file, 'r')
        Lines = file1.readlines()

        if (type == "MD5"):
            out_text.config(text="MD5 :")
            out.config(text="loading...")
            for line in Lines:
                hash_object = hashlib.md5(bytes(line.strip(), encoding='utf-8'))
                if message == hash_object.hexdigest():
                    out.config(text=line)
                    return
            out.config(text="Not found")



        if (type == "SHA1"):
            out_text.config(text="SHA1 :")
            out.config(text="loading...")
            for line in Lines:
                hash_object = hashlib.sha1(bytes(line.strip(), encoding='utf-8'))
                if message == hash_object.hexdigest():
                    out.config(text=line)
                    return
            out.config(text="Not found")

        if (type == "SHA256"):
            out_text.config(text="SHA256 :")
            out.config(text="loading...")
            for line in Lines:
                hash_object = hashlib.sha256(bytes(line.strip(), encoding='utf-8'))
                if message == hash_object.hexdigest():
                    out.config(text=line)
                    return
            out.config(text="Not found")