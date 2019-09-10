import speech_recognition as sr
import webbrowser as wb
import pyttsx3
# import speak
from tkinter import *
import os
import datetime
import requests
from PyDictionary import PyDictionary

def rex_start():

    r = sr.Recognizer()
    engine1 = pyttsx3.init()
    engine1.setProperty('rate', 150)
    engine1.say("Hello, I am Rex the voice assistant.")
    engine1.runAndWait()
    with sr.Microphone() as source:
        print('Say Something!')
        engine1.say("Say Something that i can do for you")
        engine1.runAndWait()
        audio = r.listen(source)
        print('Done!')

    try:
        text = r.recognize_google(audio)
        print('You said:\n' + text)
        lang = 'en'
        engine1 = pyttsx3.init()
        engine1.setProperty('rate', 150)

        engine1.say("You Searched " + text)
        engine1.runAndWait()

        if text == 'YouTube':
            wb.open('https://www.youtube.com')

        elif text == 'tell a joke':
            z = """A man asks a farmer near a field, Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.\n\
              The farmer says, Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one."""
            engine1.say(z)
            print(z)
            engine1.runAndWait()

        elif text == 'tell me a weather':
            api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=c3b39dac5374cedd511992b18e7fb675&q=Sahiwal'
            # city = input('City Name :')
            # url = api_address + city
            json_data = requests.get(api_address).json()
            format_add = json_data['weather'][0]['description']
            engine1.say(format_add)
            print(format_add)
            engine1.runAndWait()

        elif text == 'tell me a time':
            z = datetime.datetime.now()
            z1 = z.strftime("%I hours %M minutes %S seconds %p")
            z2 = z.strftime("%A, %B %d, %Y")
            engine1.say(z2)
            engine1.say(z1)
            print(z1)
            print(z2)
            engine1.runAndWait()
        elif text == 'dictionary':
            dictionary = PyDictionary()
            engine1.say("say a word")
            engine1.runAndWait()
            with sr.Microphone() as source1:
                audio1 = r.listen(source1)
                text1 = r.recognize_google(audio1)
                lang = 'en'
                print(text1)
                engine1.say("You Said " + text1)
                engine1.say("Meaning")
                print("Meanings:")
                print(dictionary.meaning(text1))
                print(dictionary.translate(text1, 'ur-PK'))
                engine1.say(dictionary.meaning(text1))
                engine1.say(dictionary.translate(text1, 'ur-PK'))
                engine1.runAndWait()

        else:
            f_text = 'https://www.google.com.pk/search?hl=en&source=hp&ei=x80UXKqXMK6QmgXI8oDwAg&q=' + text
            wb.open(f_text)

    except Exception as e:
        print(e)

def rex_exit():
    sys.exit()

root = Tk()
root.geometry("1366x768")
root.title("Rex Application")
label1 =Label(root)
label1.pack()
imgf1 = PhotoImage(file="rex2.png")

label1_text = Label(root,font=(10),text="1: For Google Search Say (What you want) ", fg='#18162F')
label1_text.pack()
label2_text = Label(root,font=(10),text="2: To Open YouTube Say (YouTube) ", fg='#18162F')
label2_text.pack()
label3_text = Label(root,font=(10),text="3: To Listen Joke Say (Tell a Joke)", fg='#18162F')
label3_text.pack()

start_button = Button(root,font=("Buxton Sketch", 14, 'bold'),relief=FLAT, border=1,width=30, height=2, text="Start", bg="#B1AEA7", fg="#18162F", command=lambda: rex_start()  )
start_button.pack(pady=10)
exit_button = Button(root,font=("Buxton Sketch", 14, 'bold'),relief=FLAT, border=1,width=30, height=2, text="Exit", bg="#B1AEA7", fg="#18162F", command=lambda: rex_exit() )
exit_button.pack(pady=20)

img1 = imgf1.subsample(1, 2)
label1.config(image=img1)
root.mainloop()