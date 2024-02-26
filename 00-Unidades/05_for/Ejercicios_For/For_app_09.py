import random
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        MAX_INTENTOS = 7

        title = "Adivinadivinador"
        message = None

        winning_number = random.randint(1, 101)
        print(winning_number)

        for i in range (1, MAX_INTENTOS+1):
            if i < 7:
                usr_entry = int(prompt(title, "Número: "))

                if usr_entry < winning_number:
                    message = "Falta…"
                
                else:
                    if usr_entry > winning_number:
                        message = "Se pasó…"
                    
                    else:
                        match i:
                            case 1:
                                message = "Usted es un psíquico 0o0"
                            case 2:
                                message = "Excelente percepción ._."
                            case 3:
                                message = "Esto es suerte ;)"
                            case 7:
                                message = "Perdiste, suerte para la próxima :/"
                            case _:
                                message = "Excelente técnica B)"

            else:
                message = "Perdiste, suerte para la próxima :/"

            alert(title, message)
            
            if usr_entry == winning_number:
                break

            
                

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()