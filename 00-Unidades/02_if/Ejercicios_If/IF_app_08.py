import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
Ejercicio: if_08
---
Enunciado:
Al ingresar una edad menor a 18 años y un estado civil distinto a "Soltero", NO HACER NADA,
pero si no es asi, y es soltero y no es menor, mostrar el siguiente mensaje: 'Es soltero y no
es menor.'
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.lbl_estado_civil = customtkinter.CTkLabel(master=self, text="Estado Civil")
        self.lbl_estado_civil.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_estado_civil = customtkinter.CTkComboBox(master=self, values=["Soltero", "Casado", "Divorciado"])
        self.combobox_estado_civil.grid(row=1, column=1, padx=20, pady=10)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        usr_age = int(self.txt_edad.get())
        usr_marital_status = str(self.combobox_estado_civil.get())

        if usr_age < 18:
            if usr_marital_status !=  "Soltero":
                pass
        else:
            if usr_marital_status == "Soltero":
                title = "Estado civil"
                message = "Es soltero y no es menor."

                alert(title, message)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()