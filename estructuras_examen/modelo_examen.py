import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Altura")
        self.label1.grid(row=2, column=0, padx=20, pady=10)
        self.txt_altura = customtkinter.CTkEntry(master=self)
        self.txt_altura.grid(row=2, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Días que asiste")
        self.label2.grid(row=4, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["1", "3", "5"])
        self.combobox_tipo.grid(row=4, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Kg de peso muerto que levanta")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Ingresar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=5, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        MIN_AGE = 12

        MIN_HIGHT = 0

        MIN_ASSISTANCE = 1
        MID_ASSISTANCE = 3
        MAX_ASSISTANCE = 5

        MIN_DEADWEIGHT = 0

        YES = "S"
        NO = "N"

        max_hight = 0
        max_hight_name = ""
        max_hight_age = 0

        dead_weight_total = 0

        counter_assistance = 0
        counter_min_assistance = 0
        counter_mid_assistance = 0
        counter_max_assistance = 0

        favorite_days = 0

        max_assistance_min_age = 0
        max_assistance_max_dead_weight_name = ""
        max_assistance_max_dead_weight = 0


        flag_first_entry_hight = True
        flag_first_entry_max_assistance = True
        flag_add = True

        title_prompt = "Completar"
        title_final ="Resultados"

        mid_assistance_dead_weight_avg_message = "Ningún alumno asiste 3 días"

        while True:
            if flag_add:
                #NAME
                message_name = "Nombre: "

                while True:
                    name_entry = prompt(title_prompt, message_name)

                    if name_entry == None or name_entry == "":
                        continue
                    else:
                        break    
                
                self.txt_nombre.delete(0, tkinter.END)
                self.txt_nombre.insert(0, name_entry)
                
                #AGE
                message_age = "Edad (mayor a 12): "

                while True:
                    age_entry = prompt(title_prompt, message_age)

                    if age_entry == None or age_entry == "" or MIN_AGE >= int(age_entry):
                        continue
                    else:
                        break
                
                self.txt_edad.delete(0, tkinter.END)
                self.txt_edad.insert(0, age_entry)

                #HIGHT
                message_hight = "Altura (m): "

                while True:
                    hight_entry = prompt(title_prompt, message_hight)

                    if hight_entry == None or hight_entry == "" or MIN_HIGHT > float(hight_entry):
                        continue
                    else:
                        if flag_first_entry_hight:
                            max_hight = float(hight_entry)
                            max_hight_name = name_entry
                            max_hight_age = age_entry

                            flag_first_entry_hight = False

                            break
                        else:
                            if float(hight_entry) > max_hight:
                                max_hight_name = name_entry
                                max_hight_age = age_entry

                                break
                            else:
                                break
                
                self.txt_altura.delete(0, tkinter.END)
                self.txt_altura.insert(0, hight_entry)

                #DEAD WEIGHT
                message_dead_weight = "Peso muerto que levanta (kg): "

                while True:
                    dead_weight_entry = prompt(title_prompt, message_dead_weight)

                    if dead_weight_entry == None or dead_weight_entry == "" or MIN_DEADWEIGHT >= float(dead_weight_entry):
                        continue
                    else:
                        break
                
                self.txt_legajo.delete(0, tkinter.END)
                self.txt_legajo.insert(0, dead_weight_entry)

                #ASSISTANCE
                message_assistance = "Días que asiste:\n1 día\n3 días\n5 días"

                while True:
                    assistance_entry = assistance_entry = prompt(title_prompt, message_assistance)

                    if assistance_entry == None or assistance_entry == "" or int(assistance_entry) != MIN_ASSISTANCE and int(assistance_entry) != MID_ASSISTANCE and int(assistance_entry) != MAX_ASSISTANCE:
                        continue
                    else:
                        counter_assistance += 1
                        break

                match int(assistance_entry):
                    case 1:
                        self.combobox_tipo.set(MIN_ASSISTANCE)

                        counter_min_assistance += 1
                    case 3:
                        self.combobox_tipo.set(MID_ASSISTANCE)

                        dead_weight_total = dead_weight_total + float(dead_weight_entry)
                        counter_mid_assistance += 1
                    case _:
                        self.combobox_tipo.set(MAX_ASSISTANCE)
                        if flag_first_entry_max_assistance:
                            max_assistance_min_age = int(age_entry)

                            max_assistance_max_dead_weight_name = name_entry
                            max_assistance_max_dead_weight = float(dead_weight_entry)

                            flag_first_entry_max_assistance = False

                        else:
                            if max_assistance_min_age >= int(age_entry) and max_assistance_max_dead_weight < float(dead_weight_entry):
                                max_assistance_min_age = int(age_entry)

                                max_assistance_max_dead_weight_name = name_entry
                                max_assistance_max_dead_weight = float(dead_weight_entry)

                
                message_add = "Agregar más datos:\nSI = S\nNO = N"

                while True:
                    add = prompt(title_prompt, message_add)

                    if add == None or add == "" or add != YES and add != NO:
                        continue
                    else:
                        if add == YES:
                            break
                        else:
                            flag_add = False
                            break
            else:
                break

        #FINAL
        #1. MESSAGE
            
        if counter_mid_assistance > 0:
            mid_assistance_dead_weight_avg = round(dead_weight_total / counter_mid_assistance, 2) #OK
        
            mid_assistance_dead_weight_avg_message = f"Los socios que asisten 3 días a la semana, levantan un promedio de pesomuerto de: {mid_assistance_dead_weight_avg}kg."
        
        #2. MESSAGE
            
        min_assistance_avg = round(counter_min_assistance / counter_assistance, 2) * 100
        min_assistance_avg_message = f"El{min_assistance_avg}% de los socios, asisten solo 1 día a la semana."

        #3. MESSAGE

        if counter_min_assistance < counter_mid_assistance > counter_max_assistance:
            favorite_days = MID_ASSISTANCE
        elif counter_min_assistance < counter_max_assistance > counter_mid_assistance:
            favorite_days = MAX_ASSISTANCE
        else:
            favorite_days = MIN_ASSISTANCE
        
        favorite_days_message = f"Los socios eligen más ir {favorite_days} día/s a la semana."

        #4. MESSAGE
        if flag_first_entry_max_assistance == False:
            max_assistance_max_dead_weight_message = f"{max_assistance_max_dead_weight_name} es el socio más joven que más cantidad de peso muerto levanta ({round(max_assistance_max_dead_weight, 2)}kg) que viene 5 días a la semana."

        #FINAL MESSAGE
        message_final = f"Resultados finales:\n{mid_assistance_dead_weight_avg_message}\n{min_assistance_avg_message}\n{favorite_days_message}\n{max_assistance_max_dead_weight_message}"

        alert(title_final, message_final)

        print(max_hight_name)
        print(max_hight_age)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
