import os
import win32com.client as win

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Krish")
    while True:
        x= input("Enter what you want me to speak: ")
        if x == 'q' :
            break
        speak = win.Dispatch("SAPI.SpVoice")
        speak.Speak(x)
