from tkinter import Tk, Canvas, Button, Label, Entry, CENTER, NW
from PIL import Image, ImageTk
from playsound import playsound
from time import sleep
from random import sample
from threading import Thread
from os import system

def fade(root):
    root.attributes("-alpha", sample((0,1), 1))
    sleep(0.1)
    root.attributes("-alpha", 0)
    sleep(0.1)
    root.attributes("-alpha", 1)
    root.configure(background='black')
    x = 0.2
    while x<5:
        root.attributes("-alpha", sample((0,1), 1))
        sleep(0.1)
        root.configure(background=sample(('black','white'), 1))
        x+=0.1
    sleep(0.1)
    root.attributes("-alpha", 1)
    root.configure(background='white')

root = Tk()
root.wm_attributes("-topmost", 1)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
playsound('sound1.mp3', block=False)
Thread(target= lambda: fade(root)).start()
def outgoing():
    root.destroy()
root.after(5600, outgoing)
root.mainloop()

root = Tk()
root.wm_attributes("-topmost", 1)
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
canvas = Canvas(root,width=w,height=h,bd=0,highlightthickness=0)
canvas.configure(background='black')
canvas.pack()
img = Image.open('scr.jpg')
imgWidth, imgHeight = img.size
ratio = min(w/imgWidth, h/imgHeight)
imgWidth, imgHeight = int(imgWidth*ratio), int(imgHeight*ratio)
img = img.resize((imgWidth,imgHeight), Image.ANTIALIAS)
imge = ImageTk.PhotoImage(img)
canvas.create_image(w/100,h/100,image=imge, anchor=NW)
playsound('scary.mp3', block=False)
def unblock():
    root.attributes("-alpha", 0)
    sleep(5)
    root.wm_attributes("-topmost", 1)
    root.attributes("-alpha", 1)
    playsound('scary.mp3')
    Thread(target= lambda: fade(root)).start()
    playsound('sound1.mp3', block=False)
root.after(2500, unblock)
root.mainloop()