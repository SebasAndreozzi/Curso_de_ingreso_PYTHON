import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        final_adition_pos = 0
        final_adition_neg= 0

        counter_pos = 0
        counter_neg = 0

        counter_zero = 0

        while True:
            num_entry = prompt("Número a sumar", "Número")

            if num_entry != None:
                num_entry = int(num_entry)

                if num_entry > 0:
                    final_adition_pos = final_adition_pos + num_entry
                    counter_pos += 1

                elif num_entry < 0:
                    final_adition_neg = final_adition_neg + num_entry
                    counter_neg += 1

                else:
                    counter_zero +=1
            else:
                break
        
        dif_counter_pos_counter_neg = abs(counter_pos - counter_neg)

        title = "Resultado"
        message = f"Suma de los positivos: {final_adition_pos}.\nCantidad de números positivos ingresados{counter_pos}.\nSuma de los negativos: {final_adition_neg}.\nCantidad de números negativos ingresados: {counter_neg}.\nCantidad de ceros: {counter_zero}.\nDiferencia entre la cantidad de números positivos ingresados y números negativos ingresados: {dif_counter_pos_counter_neg}"

        alert(title, message)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
