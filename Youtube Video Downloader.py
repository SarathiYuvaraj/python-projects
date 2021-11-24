
from tkinter import *
from tkinter import ttk
from pytube import YouTube
import os

root=Tk()
root.geometry('500x600')
root.resizable(False,False)
root.title('yt video downloader')
root.config(bg='black')

def download():

    quality=combo.get()

    if quality=='mp4 720':
        url=YouTube(str(link.get()))
        video=url.streams.get_highest_resolution()
        video.download()

    elif quality=='mp4 360':
        url=YouTube(str(link.get()))
        video=url.streams.first()
        video.download()

    elif quality=='mp3':
        url=YouTube(str(link.get()))
        video=url.streams.filter(only_audio=True).first()
        outfile=video.download()
        base,ext=os.path.splitext(outfile)
        newfile=base+'.mp3'
        os.rename(outfile,newfile)





#icon to project
imageicon=PhotoImage(file="images.png")
root.iconphoto(False,imageicon)
#add logo at  anchor

photo=PhotoImage(file="yt4.png")
myimage=Label(image=photo,bg='black')
myimage.pack(padx=5,pady=5)
link=StringVar()
ourlink=Entry(root,width=20,font='arial 30',textvariable=link).place(x=32,y=190)

#Button
Button(root,text='Enter',font='arial 30 bold',bg='green',width=5,height=1,command=download).place(x=110,y=260)

#add combo box
option=('mp4 360','mp4 720','mp3')
combo=ttk.Combobox(root,values=option,font='roboto 20 bold',width=10,state='r')
combo.place(x=240,y=260)
combo.set('mp4 720')
root.mainloop()
