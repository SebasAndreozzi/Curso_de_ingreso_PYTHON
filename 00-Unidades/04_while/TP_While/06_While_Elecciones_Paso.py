import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián Javier
apellido: Andreozzi
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        counter_candidates = 0
        counter_votes = 0

        most_votes = 0
        most_voted_candidate = None

        least_votes = 0
        least_voted_candiate = None
        least_voted_candidate_age = 0

        age_sum = 0
        average_age = 0

        title_prompt = "Completar"

        while True:
            candidate_name = prompt(title_prompt, "Nombre:")

            if candidate_name == None:
                break
            else:
                #CANDIDATE NAME

                while candidate_name == "":
                    candidate_name = prompt(title_prompt, "Nombre:")
                
                #CANDIDATE AGE
                
                candidate_age = prompt(title_prompt, "Edad: ")

                while candidate_age == None or candidate_age == "":
                    candidate_age = prompt(title_prompt, "Edad: ")
                
                candidate_age = int(candidate_age)

                #VOTES CUANTITY
                    
                votes_cuantity = prompt(title_prompt, "Cantidad de votos: ")

                while votes_cuantity == None or votes_cuantity == "":
                    votes_cuantity = prompt(title_prompt, "Cantidad de votos: ")
                
                votes_cuantity = int(votes_cuantity)

                #MOST AND LEAST VOTED CANDIDATE

                if most_votes == 0 and least_votes == 0:
                    most_votes = votes_cuantity
                    most_voted_candidate = candidate_name.capitalize()
                    least_votes = votes_cuantity
                    least_voted_candiate = candidate_name.capitalize()
                    least_voted_candidate_age = candidate_age

                #MOST VOTED CANDIDATE

                if votes_cuantity > most_votes:
                    most_votes = votes_cuantity
                    most_voted_candidate = candidate_name.capitalize()
                else:

                    #LEAST VOTED CANDIDATE NAME & AGE

                    if votes_cuantity < least_votes:
                        least_votes = votes_cuantity
                        least_voted_candiate = candidate_name.capitalize()
                        least_voted_candidate_age = candidate_age
                
                #AGE SUM
                        
                age_sum = age_sum + candidate_age

                #COUNTERS: VOTES & CANDIDATES

                counter_votes = counter_votes + votes_cuantity
                counter_candidates += 1

        average_age = age_sum / counter_candidates

        title = "Resultado"
        message = f"El candidato con más votos es: {most_voted_candidate}.\nEl candidato con menos votos es: {least_voted_candiate} de {least_voted_candidate_age} años.\nEl promedio de edades de los candidatos es: {average_age} años.\nEl total de votos es de {counter_votes}."
        
        alert(title, message)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
