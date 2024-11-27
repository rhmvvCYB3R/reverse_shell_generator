import customtkinter,tkinter
from tkinter import Tk, messagebox,filedialog

def app_main():
    app = customtkinter.CTk()
    app.title("REVERSE SHELL")
    app.geometry("740x540+470+200")
    app.resizable(False,False)
    app.iconbitmap('ico.ico')
    app.config(background="#6e6e6e")

    info = customtkinter.CTkLabel(app,text="Reverse Shell Generator",bg_color="#6e6e6e",text_color="#ff0000",font=("Ubuntu",25))
    info.place(x=230,y=15)
    







    app.mainloop()













app_main()