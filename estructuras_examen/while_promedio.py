import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


counter = 0
acumulador = 0

title_prompt = "Completar"

while True:
    entry = prompt(title_prompt, "Ingrese el dato")

    if entry == None or entry == "":
        continue
    else:
        acumulador = acumulador + int(entry)
        counter += 1

if counter > 0:
    acumulador_avg = acumulador/counter
else:
    message = "Nadie aplica"