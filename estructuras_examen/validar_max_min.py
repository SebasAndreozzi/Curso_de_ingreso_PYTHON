import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

max_entry = 0
min_entry = 0


flag_first_entry = True
title_prompt = "Completar"

while True:
    entry = prompt(title_prompt, "Ingrese dato:")

    if entry == None or entry == "":
        continue
    else:
        if flag_first_entry:
            max_entry = int(entry)
            min_entry = int(entry)

            flag_first_entry = False

            break
        else:
            if int(entry) > max_entry:
                max_entry = entry

                break
            elif int(entry) < min_entry:
                min_entry = entry

                break
            else:
                break