import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        INTERACTION_MAX = 10
        counter = 0

        title = "Interacción"
        message = 0
        
        while counter <= INTERACTION_MAX:
            if counter % 2 == 0:
                message = message + counter

            counter = counter + 1

        
        alert(title, message)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()