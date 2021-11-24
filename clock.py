# we are going to preapare clock using python
#first we are importing tkinter and time modules

from tkinter import *
from time import *

root=Tk() #calling window
root.title('clock') #title

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font=('times new roman',30),bg='black',fg='white')
label.pack(anchor='center')
time()
root.mainloop()