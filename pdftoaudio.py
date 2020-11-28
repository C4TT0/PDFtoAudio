#imports

import PyPDF2
import pyttsx3
import os
import time

#Speak Function

def speak(audio):
    engine = pyttsx3.init('sapi5')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125) 
    engine.say(audio)
    engine.runAndWait()

#Opening and reading pdf content with some prints

print('If you want another pdf to read then change the path in pdf variable. \n And remeber to mention double backslash because python only likes double blackslabs \n for example C:\\PAth\\To\\My\\PDF\\File')
pdf = open('E:\\Languges\\Python\\test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf, strict=False)
time.sleep(2)
os.system('cls || clear')
print("Number of pages:-"+str(pdfReader.numPages))

# Some variables for loop

num = pdfReader.numPages

i = 0

# Actual loop

while(i<num):
    pageObj = pdfReader.getPage(i)
    text=pageObj.extractText()
    text1 = text.lower()
    print(text1)
    speak(text1)
    i= i+1
