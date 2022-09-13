#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = tk.Tk()

class CoolThing:
  def __init__(self, root):
    self.root = root
    self.root.resizable(False, False)
    self.root.geometry('570x500')
    self.root.title('Waterford')
    self.root.attributes('-topmost', 1)

"""
root.geometry("570x500")
root.title("Waterford")
root.attributes("-topmost", 1)
"""

def dict(event=None):
  meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

Label(root, text="Private Dictionary", font=(
  "Poppins, 20 bold"), fg="Orange").pack(pady=20)

frame = Frame(root)
Label(frame, text="Enter word: ", font=("Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=10)
word.pack()
frame.pack(pady=10)

"""
frame1 = Frame(root)
Label(frame1, text="Result: ", font=("Helvetica, 10 bold")).pack(side="left")
#meaning = Label(frame1, text="", font=("Helvetica 10"))
meaning = Label(frame1, text="", font=("Helvetica 10"), height=20, width=65)
meaning.pack(pady=10)
frame1.pack(pady=10)
"""

frame1 = Frame(root)
Label(frame1, text="Results: ", font="Helvetica, 10 bold")
meaning = Text(frame1, height=20, width=65) 
meaning.pack()
frame1.pack(pady=10)

# just a sample
"""
my_text = Text(root, height=20, width=65, wrap=WORD)
my_text.pack(pady=10)
"""

word.bind('<Return>', dict)

root.mainloop() # runs the GUI or program


# use this website for reference: https://www.geeksforgeeks.org/word-dictionary-using-tkinter/
