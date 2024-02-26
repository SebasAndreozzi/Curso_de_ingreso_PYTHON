import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javeir
apellido: Andreozzi
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
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

        multiple_counter = 0

        for number in range(1, number_entry + 1):
            
            if number_entry % number == 0:

                alert(title, number)

                multiple_counter +=1
        
        message_multiple_counter = f"{number_entry} es divisible por {multiple_counter} números"
        
        alert(title, message_multiple_counter)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()