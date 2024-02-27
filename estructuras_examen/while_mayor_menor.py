import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

title_prompt = "Completar"

while True:
    entry = prompt(title_prompt, "Ingrese: ")
    if entry == None or entry == "" or entry > 5 or entry < 5:
        continue
    else:
        break