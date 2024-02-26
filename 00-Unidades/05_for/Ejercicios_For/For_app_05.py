import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        title = "Números"

        number_entry = int(prompt(title, "Número: "))

        pair_counter = 0

        for number in range(1, number_entry + 1):
            
            if number % 2 == 0:

                alert(title, number)

                pair_counter +=1
        
        message_pair_counter = f"Se encontraron {pair_counter} números pares"
        
        alert(title, message_pair_counter)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()