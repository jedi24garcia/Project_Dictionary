#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = tk.Tk()

class alien:
  def __init__(self, root):
    self.root.geometry("570x500")
    self.root.title("Waterford")
    self.root.attributes("-topmost", 1)

def dict(event=None):
  meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

Label(root, text="Private Dictionary", font=(
  "Poppins, 20 bold"), fg="Orange").pack(pady=20)

frame = Frame(root)
Label(frame, text="Enter word: ", font=("Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=10)
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Results: ", font="Helvetica, 10 bold")
meaning = Label(frame1, height=20, width=65) 
meaning.pack()
frame1.pack(pady=10)

word.bind('<Return>', dict)

root.mainloop() # runs the GUI or program


# use this website for reference: https://www.geeksforgeeks.org/word-dictionary-using-tkinter/
