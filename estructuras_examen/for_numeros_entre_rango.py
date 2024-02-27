import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

title = "Números primos"

number_entry = int(prompt(title, "Número: "))

for i in range(1, number_entry +1):
    multiple_counter = 0

    for j in range(1, i + 1):
        
        if i % j == 0:
            multiple_counter += 1
    
    if multiple_counter <= 2:
        alert(title, i)