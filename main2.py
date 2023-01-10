#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
# from tkinter.ttk import *
from PyDictionary import PyDictionary

password = "admiral"

userinput = input("Enter password: ") 
if userinput == (password):
  print("Thanks")
else:
  print("Try again: ")
if userinput != password:
  print("Wrong password")
  
dictionary = PyDictionary()
window = tk.Tk()

# This is UI
window.title("Personal Dictionary")
window.geometry("900x600+100+100")
window.attributes("-topmost", 1)
window.configure(bg="black")


def dict(event=None):
  meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

def newWindow():
  newWindow = Toplevel(window) 
  newWindow.title("New Window")
  newWindow.geometry("900x600+100+100") 
  Label(newWindow, text = "This is a new window").pack()

Label(window, text="System Dictionary", font=("Helvitica, 40 bold"), fg="Red").pack(pady=20)

frame = Frame(window)
Label(frame, text="Enter word: ", font=("Helvetica, 15 bold")).pack(side="left")
word = Entry(frame, font=("Helvetica, 15 bold"), width=10)
word.pack()
frame.pack(pady=10)

meaning = Label(window, height=25, width=95) 
meaning.configure(bg="black")
meaning.pack()
btn = Button(window, text="Click to open new window", command = newWindow)
btn.pack(pady = 10)

word.bind('<Return>', dict)

window.mainloop()
