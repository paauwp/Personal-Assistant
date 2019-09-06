import os
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr 
import time

while True:
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("Speak something")
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			print(text)
			if text == 'break':
				print("You're Assistant has ceased operating")
				break
			else:
				window=Tk()
				window.geometry("700x600")

		except Exception as e:
			print(e)
			answer = "Sorry I cannont hear you"
			print(answer)

