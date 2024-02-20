import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: while_08
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        final_addition = 0
        final_product = 1

        no_neg = True

        while True:
            num_entry = prompt("Número a sumar", "Número")

            if num_entry == None or int(num_entry) == 0:
                break
            else:
                if int(num_entry) >= 0:
                    final_addition = final_addition + int(num_entry)
                else:
                    final_product = final_product * int(num_entry)
                    no_neg = False
        
        if no_neg:
            final_product = 0

        self.txt_suma_acumulada.delete(0, tkinter.END)
        self.txt_suma_acumulada.insert(0, final_addition)
        
        self.txt_producto.delete(0, tkinter.END)
        self.txt_producto.insert(0 , final_product)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
