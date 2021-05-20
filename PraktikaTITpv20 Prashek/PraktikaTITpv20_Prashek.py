import tkinter as tk
from tkinter.ttk import *
from tkinter import *

CT = ["Tallinn", "Tartu", "Rakvere", 'Pärnu', 'Narva', 'Kohtla-Järve', 'Kuressaare']
PPL = ["426538", "93124", "15526", "39620", "57130", "35187", "13382"]
IMGS= ["Tallinn.png", "Tartu.png", "Rakvere.png", "parnu.png", "Narva.png", "Kohtla.png", "kuressaare.png"]

global cv, wd, img

def GT():
    global cv, wd, img
    l1.set("")
    if ck.get() == 1:
        l1.set("Population in " + CTS.get(ACTIVE) + ": " + PPL[cmpr()] + " (2017)")
    else:
        l1.set("Population in " + CTS.get(ACTIVE) + ": " + PPL[cmpr()])

    img=PhotoImage(file = IMGS[cmpr()])
    cv.create_image(2, 2, image=img, anchor="nw")


def cmpr():
    m=0
    for i in CT:
        if i == CTS.get(ACTIVE):
            return m
        else:
            m+=1



wd = tk.Tk()
wd.title("Form")
wd.geometry("400x400")

butt = Button(wd, width=55, text = "Apply", command =GT)

ck = IntVar()
l1=StringVar()

CTS = Listbox(wd, width=65, height=7)
for el in CT:
    CTS.insert(END, el)

CK = Checkbutton(wd, text="Date of population count", variable=ck, onvalue=1, offvalue=0)

cv=Canvas(wd, width=120, height=120, bg="black")

butt.grid(row=0, column=2, sticky="NW")
CTS.grid(row=1, column=2, sticky="W")
Label(wd, textvariable=l1).grid(row=2, column=2, sticky="W")
CK.grid(row=3, column=2, sticky="W")

cv.grid(row=4, column=2)


wd.mainloop()
