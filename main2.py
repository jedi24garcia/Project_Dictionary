#!/usr/bin/env python3

import tkinter as tk
from tkinter import *
from PyDictionary import PyDictionary
import speech_recognition as sr
import pyttsx3
# import time
# import datetime
# from ecapture import ecapture as ec
# import requests
# import subprocess
# import webbrowser
# import wikipedia
# import wolframalpha
# import os

# print("Welcome!")

dictionary = PyDictionary()
window = tk.Tk()
engine = pyttsx3.init()

# This is UI
window.title("Personal Dictionary")
window.geometry("900x600+100+100")
window.attributes("-topmost", 1)
window.configure(bg="darkgrey")

def dict(event=None):
  meaning.config(text=dictionary.meaning(word.get())['Noun'][0])

# will need to figure this out

"""
# audio
def takeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
  # print("Listening...")
    audio=r.Listen(source)
"""

# speak("Welcome!")

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

def speak(text):
  engine.say(text)
  engine.runAndWait()

speak("Welcome")

window.mainloop()
 
