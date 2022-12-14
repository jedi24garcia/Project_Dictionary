#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
window = tk.Tk()

# This is UI
window.title("Personal Dictionary")
window.geometry("900x600+100+100")
window.attributes("-topmost", 1)
window.configure(bg="black")

def dict(event=None):
  meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

Label(window, text="System Dictionary", font=("Helvitica, 40 bold"), fg="Black").pack(pady=20)

frame = Frame(window)
Label(frame, text="Enter word: ", font=("Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=10)
word.pack()
frame.pack(pady=10)

meaning = Label(window, height=25, width=95) 
meaning.configure(bg="black")
meaning.pack()

word.bind('<Return>', dict)

window.mainloop() 
