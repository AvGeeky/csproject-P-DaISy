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

# Welcome screen, login details to be shifted into a file
welcome = tk.Tk()
#we need to refine this part and make it a csv file, another database
usernames = ["Sai", "Ayushi"]
passwords = ["123"]
registered_email = ["saipranav.sai2005@gmail.com", "ayushi16055@gmail.com"]
sixdig_pass = str(random.randint(100000, 999999))

#Search based on image window
def search_img():
    print("")
        #new window with two options(buttons), take a picture and upload a picture
        #for button: take a picture
        #camera_search()
        #for button: upload a picture
        #upload_search()
        #function definitions added to the end



# Database screen
def screen2():
    def search_name():
        print("")
    def new_report():
        def submit_missingreport(): #upon clicking submit
            print("")
        # This is the section of code which creates a button
        tk.Button(sc2, text='SEARCH BASED ON IMAGE', bg='#00FFFF', font=('courier', 12, 'normal'),
               command=search_img).place(x=47, y=247)

        # This is the section of code which creates a button
        tk.Button(sc2, text='SEARCH BASED ON NAME', bg='#00FFFF', font=('courier', 12, 'normal'),
               command=search_name).place(x=357, y=247)

        # This is the section of code which creates a button
        tk.Button(sc2, text='FILE NEW REPORT', bg='#00FFFF', font=('courier', 12, 'normal'), command=new_report).place(
            x=667, y=247)

        # This is the section of code which creates a text input box
        NAME = tk.Entry(sc2)
        NAME.place(x=397, y=367)

        # This is the section of code which creates a text input box
        lastseen = tk.Entry(sc2)
        lastseen.place(x=397, y=407)

        # This is the section of code which creates a text input box
        contacts = tk.Entry(sc2)
        contacts.place(x=397, y=487)

        # This is the section of code which creates a text input box
        info = tk.Entry(sc2)
        info.place(x=397, y=527)

        # This is the section of code which creates the a Label
        tk.Label(sc2, text='FULL NAME', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=297, y=367)

        # This is the section of code which creates the a Label
        tk.Label(sc2, text='LAST SEEN', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=297, y=407)

        # This is the section of code which creates the a Label
        tk.Label(sc2, text='PICTURE', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=307, y=447)

        # This is the section of code which creates the a Label
        tk.Label(sc2, text='CONTACT(S)', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=287, y=487)

        # This is the section of code which creates the a Label
        tk.Label(sc2, text='ADDITIONAL DETAILS', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=207, y=527)
        tk.Button(sc2, text='SUBMIT', bg='#7FFFD4', font=('verdana', 15, 'normal'), command=submit_missingreport).place(
            x=642, y=327)

    sc2 = tk.Tk()
    #welcome.destroy()
    sc2.title("Database Section")
    sc2.geometry('888x584')
    sc2.configure(background='#F0F8FF')
    l1 = tk.Label(sc2, text="Tamilnadu Police Data Management System", font=font_head, foreground="Blue", width=1280)
    l1.pack()
    l4 = tk.Label(sc2, text="CRIMINAL SEARCH SYSTEM", foreground="White", background="Red", font=font_subhead)
    l4.pack()
    b2= tk.Button(sc2, text='SEARCH BASED ON IMAGE', bg='#00FFFF', font=('courier', 12, 'normal'), command=search_img)
    b2.place(x=47, y=247)
    b3=tk.Button(sc2, text='SEARCH BASED ON NAME', bg='#00FFFF', font=('courier', 12, 'normal'), command=search_name).place(x=357, y=247)
    b4=tk.Button(sc2, text='FILE NEW REPORT', bg='#00FFFF', font=('courier', 12, 'normal'), command=new_report).place(x=667, y=247)



# Password forgot dialogues
count = 2


def passwordreset():
    def reset():
        def check():
            def verify():
                global sixdig_pass, count
                ans = e3.get()
                if count == 0:
                    _show('Warning', 'Shutting down')
                    welcome.destroy()
                if ans == sixdig_pass:
                    screen2()
                if ans != sixdig_pass:
                    count -= 1
                    _show('Denied!', 'The answer is wrong. Attempts left: ' + str(count + 1))

            global registered_email, sixdig_pass
            z = e2.get()

            if z in registered_email:
                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)
                # start TLS for security
                s.starttls()
                # Authentication
                s.login("policedtb.csproject@gmail.com", "iozseffpojvyhnwu")
                s.sendmail("policedtb.csproject@gmail.com", z, sixdig_pass)
                # terminating the session
                s.quit()

                l5 = tk.Label(text="Enter your 6 digit Verification-Code", bg="#5d8dac")
                l5.place(x=563, y=580)
                e3 = tk.Entry(welcome)
                e3.place(x=593, y=600)
                b3 = tk.Button(text="Enter Answer", command=verify, background="Grey", foreground="Blue")
                b3.place(x=614, y=625)
            else:
                global count
                count -= 1
                _show('Denied!', 'The answer is wrong. Attempts left: ' + str(count + 1))
                if count == 0:
                    _show('Warning', 'Shutting down')
                    welcome.destroy()

        l1 = tk.Label(welcome, text="Enter your REGISTERED EMAIL ID", bg="#5d8dac")
        l1.place(x=563, y=515)
        e2 = tk.Entry(welcome)
        e2.place(x=595, y=535)
        b2 = tk.Button(text="Enter Answer", command=check, background="Grey", foreground="Blue")
        b2.place(x=614, y=555)

    b1 = tk.Button(welcome, text="Forgot Username/Password?", command=reset, foreground="Blue")
    b1.place(x=576, y=480)


# Password authentication
def store():
    global tb1, tb2, usernames, passwords
    user, passw = tb1.get(), tb2.get()
    if user in usernames and passw in passwords:
        _show('Welcome', 'Redirecting you now, ' + user)
        screen2()
    else:
        _show('Unauthorized', 'Check the details you entered.')
        passwordreset()

filepath=""
found=False

def upload_search():
    uw = tk.Tk()
    uw.geometry("700x350")
    def open_file():
        global filepath
        file = tk.filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')])
        if file:
            filepath = str(os.path.abspath(file.name))
            #we can skip these steps
            #need to add a label that shows the image saved in 'filepath'
            #need to have a confirmation button that redirects to the searching page
            img_search()
            uw.destroy()
    
    l2=tk.Label(uw, text="Upload picture", font=('Georgia 13'))
    l2.pack(pady=10)
    tk.Button(uw, text="Browse", command=open_file).pack(pady=20)
    uw.mainloop()

def camera_search():
    global filepath
    camera = cv2.VideoCapture(0)
    cv2.namedWindow("Capture an image")

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Try Again")
            break
        cv2.imshow("Capture an image", frame)

        key = cv2.waitKey(1)
        if key%256 == 27:
            # ESC pressed, closes the window--dont destroy previous window, overwrite it
            break
        elif key%256 == 32:
            # SPACE pressed
            filepath = "C:\\Users\\ayush\\Desktop\\CS project\\temporary_image\\imgcampture.jpg"
            cv2.imwrite(filepath, frame)
            break

    camera.release()
    cv2.destroyAllWindows()


#image search
def img_search():
    global filepath
    uimg = face_recognition.load_image_file(filepath)
    u_encoding = face_recognition.face_encodings(uimg)[0]
    #open database
    f=open("policedatabase.csv","r")
    rr=reader(f)
    #need to exclude headers while checking
    global found
    MPIN=0
    for i in rr:
        if i[0]=='MPIN':
            continue
        else:
            path=i[6]
            cimg = face_recognition.load_image_file(path)
            c_encoding = face_recognition.face_encodings(cimg)[0]
            result = face_recognition.compare_faces([c_encoding], u_encoding)
            #output of result is [boolean]
            if True in result:
                found=True
                MPIN=i[0]
                print(i)
                #add details of i(MPIN stored in variable), search up based on MPIN and display as separate window
                break
    f.close()




#if found:
    #add function linking to next window where details are shown
#else:
    #try again popup box



# FONTS
font_head = Font(
    family='Garmond',
    size=30,
    weight='bold',
)

font_subhead = Font(
    family='Times New Roman',
    size=20,
    weight='bold',
)
u_name = Font(
    family='Century Gothic',
    size=15,
    weight='bold',
)
# IMAGES
intro_image = PIL.Image.open("folder.png")
bg_img = PIL.Image.open("jurgen-jester-_PizUeTnvFE-unsplash.jpg")
size = (200, 200)
size1 = (1920, 1280)
intro_image = intro_image.resize(size)
bg_img = bg_img.resize(size1)
policeimg = ImageTk.PhotoImage(intro_image)
bgimg = ImageTk.PhotoImage(bg_img)

# loginscreen
welcome.title("Police Data Management System - LOGIN")
welcome.state("zoomed")
limg = tk.Label(image=bgimg)
limg.pack()
l1 = tk.Label(welcome, text="Tamilnadu Police Data Management System", font=font_head, foreground="White",
              background="Red", width=1280)
l1.pack()
# similar to pack, place places it using coordinate system
l4 = tk.Label(text="LOGIN", foreground='white', bg='blue', font=font_head, width=10)
l4.place(x=540, y=185)
l3 = tk.Label(text="USERNAME", foreground='green', bg="#5d8dac", font=u_name)
l3.place(x=602, y=285)
l3 = tk.Label(text="PASSWORD", foreground='green', bg="#5d8dac", font=u_name)
l3.place(x=602, y=345)
tb1 = tk.Entry()
tb1.place(x=595, y=315)
tb2 = tk.Entry(show="*")
tb2.place(x=595, y=375)
b1 = tk.Button(text="SUBMIT", command=store, foreground="green")
b1.place(x=631, y=410)

welcome.mainloop()  # apparently this should end every window to print it in pycharm

