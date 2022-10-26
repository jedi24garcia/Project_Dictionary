#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary
import json

dictionary = PyDictionary()
window  = tk.Tk()

window.title("Waterford Security")
window.geometry("900x600+100+100")
window.attributes("-topmost", 1)
window.configure(bg="black")


def dict(event=None):
  meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

Label(window, text="Waterford Assistant", font=(
  "Poppins, 20 bold"), fg="Orange").pack(pady=20)

frame = Frame(window)
Label(frame, text="Enter name: ", font=("Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=10)
word.pack()
frame.pack(pady=10)

meaning = Label(window, height=25, width=95) 
meaning.pack()

word.bind('<Return>', dict)

window.mainloop()
 
