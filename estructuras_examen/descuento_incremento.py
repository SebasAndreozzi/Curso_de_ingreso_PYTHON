import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

BASE_PRICE = 5000
percentage = 0

final_price_increase = BASE_PRICE + ((BASE_PRICE * percentage) / 100)
final_price_decrease = BASE_PRICE - ((BASE_PRICE * percentage) / 100)