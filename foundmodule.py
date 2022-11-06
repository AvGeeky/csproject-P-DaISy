# all modules used
import random
import tkinter as tk
import smtplib
import PIL
from PIL import ImageTk
from tkinter.font import Font
from tkinter.messagebox import _show
import imghdr
from tkinter import *
from tkinter.filedialog import askopenfile
import os
import face_recognition
import cv2
import numpy as np
from csv import reader, writer
import os


details=["TN14","Ed Sheeran","15:51 16/05/2018","Coimbatore","1398087688 Geeta","seen","MPIN_pictures\TN14.jpg"]

def person_found():
    global details
    sc3 = tk.Tk()
    sc3.title("Details of person")
    sc3.geometry('888x584')
    sc3.configure(background='#F0F8FF')
    sc3.attributes('-topmost', True)

    heading = Font(
    family='Times New Roman',
    size=15,
    weight='bold',
    ) 
    text = Font(
    family='Times New Roman',
    size=14,
    weight='normal'
    )


    #load image of person
    img = PIL.Image.open(details[6])
    img.thumbnail((300, 250))
    height=img.height
    width=img.width
    img.save("imgresized.gif")
    imgcanvas= tk.Canvas(sc3, height=height, width=width)
    picture_file = tk.PhotoImage(file = 'imgresized.gif')
    imgcanvas.create_image(0, 0, anchor=NW, image=picture_file)
    imgcanvas.place(x=310, y=29)
    
    # need to change alignment
    tk.Label(sc3, text="MPIN ID:", bg='#F0F8FF', font=(heading)).place(x=300, y=300)
    tk.Label(sc3, text=details[0], bg='#F0F8FF', font=(text)).place(x=500, y=300)
    tk.Label(sc3, text="Name:", bg='#F0F8FF', font=(heading)).place(x=300, y=330)
    tk.Label(sc3, text=details[1], bg='#F0F8FF', font=(text)).place(x=500, y=330)
    tk.Label(sc3, text="Last Seen(Time/Date):", bg='#F0F8FF', font=(heading)).place(x=300, y=360)
    tk.Label(sc3, text=details[2], bg='#F0F8FF', font=(text)).place(x=500, y=360)
    tk.Label(sc3, text="Last Seen(Place):", bg='#F0F8FF', font=(heading)).place(x=300, y=390)
    tk.Label(sc3, text=details[3], bg='#F0F8FF', font=(text)).place(x=500, y=390)
    tk.Label(sc3, text="Point of Contact:", bg='#F0F8FF', font=(heading)).place(x=300, y=420)
    tk.Label(sc3, text=details[4], bg='#F0F8FF', font=(text)).place(x=500, y=420)
    tk.Label(sc3, text="Additional Information:", bg='#F0F8FF', font=(heading)).place(x=300, y=450)
    tk.Label(sc3, text=details[5], bg='#F0F8FF', font=(text)).place(x=500, y=450)
    sc3.mainloop()
person_found()