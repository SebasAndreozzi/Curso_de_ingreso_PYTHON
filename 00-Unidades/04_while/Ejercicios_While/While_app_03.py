import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        PASSWORD = "utn750"

        usr_password_entry = ""

        title = "Inicio de seción"
        message = "¡Entraste!"

        while usr_password_entry != PASSWORD:
            usr_password_entry = prompt(title, "Contraseña")

        alert(title, message)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()