import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: while_04
---
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        NUM_VALID_MIN = 0
        NUM_VALID_MAX = 9

        title ="Validación"
        message = "Número válido"

        num = int(prompt(title, "Numero"))

        while num < NUM_VALID_MIN or num > NUM_VALID_MAX:
            num = int(prompt(title, "Número"))
        
        alert(title, message)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()