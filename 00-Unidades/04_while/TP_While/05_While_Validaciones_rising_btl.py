import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        MIN_AGE = 18
        MAX_AGE = 90

        SINGLE = "S"
        SINGLE_TEXT = "Soltero/a"
        MARRIED = "C"
        MARRIED_TEXT = "Casado/a"
        DIVORSED = "D"
        DIVORSED_TEXT = "Divorciado/a" 
        WIDOW = "V"
        WIDOW_TEXT = "Viudo/a"

        CHARACTERS_FILE_NUMBER = 4

        title_prompt = "Completar" 

        #SURNAME
        message_surname = "Apellido: "

        surname_entry = prompt(title_prompt, message_surname)

        while surname_entry == None or surname_entry == "":
            surname_entry = prompt(title_prompt, message_surname)
        
        self.txt_apellido.delete(0, tkinter.END)
        self.txt_apellido.insert(0, surname_entry)
        
        #AGE
        message_age = "Edad (entre 18 y 90 años): "

        age_entry = prompt(title_prompt, message_age)

        while age_entry == None or age_entry == "" or MIN_AGE > int(age_entry) or int(age_entry) > MAX_AGE:
            age_entry = prompt(title_prompt, message_age)
        
        self.txt_edad.delete(0, tkinter.END)
        self.txt_edad.insert(0, age_entry)

        #MARITAL STATE
        message_marital_state = "Complete su Estado Civil con alguna de estas letras: \n   S = Soltero/a \n   C = Casado/a \n   D = Divorciado/a \n   V = Viudo/a"

        marital_state_entry = prompt(title_prompt, message_marital_state)
        
        while marital_state_entry != SINGLE and marital_state_entry != MARRIED and marital_state_entry != DIVORSED and marital_state_entry != WIDOW:
            marital_state_entry = marital_state_entry = prompt(title_prompt, message_marital_state)
        
        match marital_state_entry:
            case "S":
                self.combobox_tipo.set(SINGLE_TEXT)
            case "C":
                self.combobox_tipo.set(MARRIED_TEXT)
            case "D":
                self.combobox_tipo.set(DIVORSED_TEXT)
            case _:
                self.combobox_tipo.set(WIDOW_TEXT)
                    
        '''

        match marital_state_entry:
            case "S":
                self.combobox_tipo.set(SINGLE_TEXT)
            case "C":
                self.combobox_tipo.set(MARRIED_TEXT)
            case "D":
                self.combobox_tipo.set(DIVORSED_TEXT)
            case "V":
                self.combobox_tipo.set(WIDOW_TEXT)
            case _:
                marital_state_entry = prompt(title_prompt, message_marital_state)

        '''

        #FILE NUMBER
        message_file_num = "Nro de legajo: "

        file_num_entry = prompt(title_prompt, message_file_num)

        while file_num_entry == None or file_num_entry == "" or len(file_num_entry) != CHARACTERS_FILE_NUMBER:
            file_num_entry = prompt(title_prompt, message_file_num)
        
        self.txt_legajo.delete(0, tkinter.END)
        self.txt_legajo.insert(0, file_num_entry)            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
