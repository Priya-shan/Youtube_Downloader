from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

fileLocation=""

def openLocation():
    global fileLocation
    fileLocation=filedialog.askdirectory()
    if(len(fileLocation)>1):
        locationError.config(text=fileLocation,fg="#005909")
    else:
        locationError.config(text="Please choose a folder",fg="red")

def DownloadVideo():
    optionSelected=selectQuality.get()
    url=entrybox.get()

    if(len(url)>1):
        yt=YouTube(url)

        if(optionSelected==options[0]):
            select=yt.streams.filter(progressive=True).first()
        elif(optionSelected==options[1]):
            select=yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(optionSelected==options[2]):
            select=yt.streams.filter(only_audio=True).first()
        else:
            errorMsgFinal.config(text="oopsiee")

    select.download(fileLocation)
    errorMsgFinal.config(text="Download Completed!!")






root=Tk()
root.title("Instant YouTube Downloader")
root.geometry("550x550")
root.columnconfigure(0,weight=1)
root.configure(bg="#1af0c1")

heading=Label(root,text="✨Instant Youtube Downloader✨",font=("Comic Sans MS",20,"bold"),bg="#1af0c1")
heading.grid(pady=(75,0))

mainlabel=Label(root,text="Enter the URL below",font=("Comic Sans MS",20,"bold"),bg="#1af0c1")
mainlabel.grid(pady=(40,0))

urlEntered=StringVar()
entrybox=Entry(root,width=50,textvariable=urlEntered,)
entrybox.grid()

location=Button(root,text="choose Location",width="15",bg="#00634e",fg="white",command=openLocation)
location.grid(pady=(30,10))

locationError = Label(root,text="Chosen path will be displayed here !! ",fg="red",font=("Comic Sans MS",10,"bold"),bg="#1af0c1")
locationError.grid()

Quality = Label(root,text="Select Preffered Quality",font=("Comic Sans MS",15,"bold"),bg="#1af0c1")
Quality.grid(pady=(20,0))

options = ["720p","144p","mp3"]
selectQuality = ttk.Combobox(root,values=options)
selectQuality.grid()

download = Button(root,text="Donwload",width=10,bg="#00634e",fg="white",command=DownloadVideo)
download.grid(pady=(30,0))

errorMsgFinal=Label(root,text=" ",fg="#005909",font=("Comic Sans MS",20,"bold"),bg="#1af0c1")
errorMsgFinal.grid(pady=(10,0))

root.mainloop()