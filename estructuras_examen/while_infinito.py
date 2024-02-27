import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Ingresar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=5, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        add = True

        title_add = "Seguir"
        message_add = "¿Agregar más datos?"

        while seguir:
            
            seguir = question(title_add, message_add)

        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
