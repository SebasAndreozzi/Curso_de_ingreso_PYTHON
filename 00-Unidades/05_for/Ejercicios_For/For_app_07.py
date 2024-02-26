import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        title = "Número"
    
        number_entry = int(prompt(title, "Número: "))

        flag_prime = True

        for number in range(2, number_entry):
            
            if number_entry % number == 0:
                flag_prime = False
                break
        
        if flag_prime:
            message = f"{number_entry} es primo"
        else:
            message = f"{number_entry} no es primo"
        
        alert(title, message)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()