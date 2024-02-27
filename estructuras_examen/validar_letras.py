import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

title_prompt = "completar"

while True:
    entry = prompt(title_prompt, "Ingrese:\nA = bla\nB = bla\nC = bla")
    if entry == None or entry == "" or entry != "A" and entry != "B" and entry != "C":
        continue
    else:
        break