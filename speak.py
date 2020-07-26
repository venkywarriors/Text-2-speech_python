'''
Created on 12-Jul-2020

@author: venkateshwara D

Description :Sample python script to demonstrate TTS using pyttsx3
'''
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)

engine.setProperty('voice', 'en+f3')
engine.say("hello")

engine.runAndWait()
