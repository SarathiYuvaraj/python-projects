import PyPDF2
from tkinter.filedialog import *
import pyttsx3

file=askopenfilename()
pdfReader=PyPDF2.PdfFileReader(file)
pages=pdfReader.numPages

speaker=pyttsx3.init()
for x in range(0,pages):
    page = pdfReader.getPage(x)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
