#!/usr/bin/env python3

#import json
#from difflib import get_close_matches
import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = tk.Tk()

root.geometry('600x400+50+50')

def dict:
# meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
  synonym.config(text=dictionary.synonym(word.get()))

Label(root, text="Dots", font=(
  "Poppins, 20 bold"), fg="Orange").pack(pady=20)

frame = Frame(root)
Label(frame, text="Enter name: ", font=("Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=30)
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning: ", font=("Helvetica, 10 bold")).pack(side="left")
meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

#Button(root, text="Search", font=("Helvetica, 15 bold"), command=dict).pack()
word.bind('<Return>', dict)

root.mainloop() # runs the GUI or program


#use this website for reference: https://www.geeksforgeeks.org/word-dictionary-using-tkinter/
