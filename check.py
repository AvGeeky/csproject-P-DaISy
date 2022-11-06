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

# Welcome screen, login details to be shifted into a file
welcome = tk.Tk()
# we need to refine this part and make it a csv file, another database
usernames = ["1", "Ayushi"]
passwords = ["1"]
registered_email = ["saipranav.sai2005@gmail.com", "ayushi16055@gmail.com"]
sixdig_pass = str(random.randint(100000, 999999))

filepath = ''
found = False
newpath = ""
MPINid = ""


# image search
def img_search():
    root.attributes('-topmost', True)
    global sc2
    global filepath
    print(filepath)
    uimg = face_recognition.load_image_file(filepath)
    u_encoding = face_recognition.face_encodings(uimg)[0]
    # open database
    f = open("policedatabase.csv", "r")
    rr = reader(f)
    # need to exclude headers while checking
    global found
    MPIN = 0
    for i in rr:
        if i[0] == 'MPIN':
            continue
        else:
            path = i[6]
            cimg = face_recognition.load_image_file(path)
            try:
                c_encoding = face_recognition.face_encodings(cimg)[0]
            except:
                print("not found")
                break
            result = face_recognition.compare_faces([c_encoding], u_encoding)
            # output of result is [boolean]
            if True in result:
                root.attributes('-topmost', False)
                found = True
                MPIN = i[0]
                print(i)
                sc3 = tk.Tk()
                sc3.title("Database Section")
                sc3.geometry('888x584')
                sc3.configure(background='#F0F8FF')
                sc3.attributes('-topmost', True)

                # This is the section of code which creates the a label
                tk.Label(sc3, text=i[0], bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=216, y=275)

                # This is the section of code which creates the a label
                tk.Label(sc3, text=i[1], bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=416, y=275)

                # This is the section of code which creates the a label
                tk.Label(sc3, text=i[2], bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=626, y=275)

                # This is the section of code which creates the a label
                tk.Label(sc3, text=i[3], bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=416, y=375)

                # This is the section of code which creates the a label
                tk.Label(sc3, text=i[4], bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=416, y=445)

                # This is the section of code which creates the a label
                tk.Label(sc3, text=i[5], bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=356, y=535)
                root.destroy()

                # add details of i(MPIN stored in variable), search up based on MPIN and display as separate window
                break
    f.close()


def upload_search():
    uw = tk.Tk()
    uw.lift()
    uw.geometry("700x350")
    tk.Label(root, text="loading", bg='#F0F8FF', font=('arial', 15, 'normal')).pack()

    def open_file():
        global filepath
        file = tk.filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')])
        if file:
            filepath = str(os.path.abspath(file.name))
            uw.destroy()
            tk.Label(root, text="hold on, searching", bg='#F0F8FF', font=('arial', 15, 'normal')).pack()
            img_search()

    l2 = tk.Label(uw, text="Upload picture", font=('Georgia 13'))
    l2.pack(pady=10)
    tk.Button(uw, text="Browse", command=open_file).pack(pady=20)
    uw.mainloop()


def camera_search():
    global filepath, root
    camera = cv2.VideoCapture(0)
    cv2.namedWindow("Capture an image with Space, ESC to close.")

    while True:
        ret, frame = camera.read()
        if not ret:
            print("Try Again")
            break
        cv2.imshow("Capture an image", frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:
            tk.Label(root, text="closed successfully", bg='#F0F8FF', font=('arial', 15, 'normal')).pack()
            # ESC pressed, closes the window--dont destroy previous window, overwrite it
            break
        elif key % 256 == 32:
            tk.Label(root, text="loading", bg='#F0F8FF', font=('arial', 15, 'normal')).pack()
            # SPACE pressed
            filepath = "temporary_image.jpg"
            cv2.imwrite(filepath, frame)
            break

    camera.release()
    cv2.destroyAllWindows()
    img_search()
    os.remove("temporary_image.jpg")
    tk.Label(root, text="hold on, searching", bg='#F0F8FF', font=('arial', 15, 'normal')).pack()


# if found:
# add function linking to next window where details are shown
# else:
# try again popup box

root = ''


# Search based on image window
def search_img():
    global root

    def dest():
        root.destroy()

    root = tk.Tk()
    root.lift()
    root.title("Search Window")
    root.geometry('890x580')
    root.configure(background='#F0F8FF')

    # This is the section of code which creates a button
    tk.Button(root, text='TAKE A PICTURE', bg='#00EEEE', font=('courier', 12, 'normal'), command=camera_search).place(
        x=107, y=63)

    # This is the section of code which creates a button
    tk.Button(root, text='UPLOAD A PICTURE', bg='#BCEE68', font=('courier', 12, 'normal'), command=upload_search).place(
        x=607, y=63)
    tk.Button(root, text='GO BACK', bg='#CD6600', font=('courier', 15, 'normal'), command=dest).place(x=387, y=273)


sc2 = ""


# Database screen
def screen2():
    global filepath
    global newpath
    global MPINid
    global sc2

    def search_name():
        print("")

    def upload_file():
        global MPINid, newpath
        file = tk.filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.*')])
        if file:
            filepath = str(os.path.abspath(file.name))
            img = cv2.imread(filepath)
            f = open("policedatabase.csv", "r")
            rr = list(reader(f))
            for n in range(-1,-10,-1):
                if rr[n]!=[]:
                    refid = rr[n][0]
                    break
            idnum = int(refid[2:]) + 1
            MPINid = "TN" + str(idnum)
            print(MPINid)
            newpath = "CS PROJECT\\MPIN_pictures" + MPINid + ".jpg"
            cv2.imwrite(newpath, img)
            f.close()
            _show('IMAGE UPLOAD SUCCESSFUL', 'Please make a note of your MPIN ID-' + str(MPINid))

    def new_report():
        def submit_missingreport():  # upon clicking submit
            sc2.state("zoomed")
            sc2.resizable(width=1, height=1)
            global name1, lastseentime, contacts, lastseenplace, info, MPINid, newpath
            name1, lastseentime, contacts, lastseenplace, info = name1.get(), lastseentime.get(), contacts.get(), lastseenplace.get(), info.get()

            def confirm_submit():
                global name1, lastseentime, contacts, lastseenplace, info, MPINid, newpath
                f = open("policedatabase.csv", "a")
                wr = writer(f)
                print([MPINid,name1,lastseentime,lastseenplace,contacts,info,newpath])
                wr.writerow([MPINid,name1,lastseentime,lastseenplace,contacts,info,newpath])
                f.close()
                aa="MPIN:"+str(MPINid)+"-NAME:"+str(name1)+"-LAST SEEN:"+str(lastseentime)+"-LAST SEEN PLACE:"+str(lastseenplace)+"-CONTACTS:"+str(contacts)+"-Information:"+str(info)
                _show("SUCCESS","Please note"+aa)
                screen2()


            frame = Frame(sc2)
            frame.pack(side=RIGHT)

            b4_ = tk.Label(frame, text="MPIN: "+MPINid, fg="green")
            b4_.pack(side=BOTTOM)

            b5_n = tk.Label(frame, text="NAME: "+name1, fg="green")
            b5_n.pack(side=BOTTOM)

            b6_ = tk.Label(frame, text="LAST SEEN: "+lastseentime, fg="green")
            b6_.pack(side=BOTTOM)

            b7_b = tk.Label(frame, text="CONTACTS: "+contacts, fg="green")
            b7_b.pack(side=BOTTOM)

            b8_b = tk.Label(frame, text="ADDL.INFORMATION: "+info, fg="green")
            b8_b.pack(side=BOTTOM)

            tk.Button(frame, text='CONFIRM', bg='#0EF4DF', font=('verdana', 10, 'normal'), command=confirm_submit).pack(
                side=LEFT)

            tk.Button(frame, text='EDIT', bg='#0EF4DF', font=('verdana', 10, 'normal'), command=new_report).pack(
                side=LEFT)

        global name1, lastseentime, contacts, lastseenplace, info
        name1 = tk.Entry(sc2)
        name1.place(x=397, y=367)
        lastseentime = tk.Entry(sc2)
        lastseentime.place(x=397, y=407)
        contacts = tk.Entry(sc2)
        contacts.place(x=397, y=487)
        lastseenplace = tk.Entry(sc2)
        lastseenplace.place(x=397, y=567)
        info = tk.Entry(sc2)
        info.place(x=397, y=527)
        tk.Label(sc2, text='FULL NAME', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=297, y=367)
        tk.Label(sc2, text='LAST SEEN', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=297, y=407)
        tk.Label(sc2, text='PICTURE', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=307, y=447)
        tk.Label(sc2, text='CONTACT(S)', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=287, y=487)
        tk.Label(sc2, text='ADDITIONAL DETAILS', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=207, y=527)
        tk.Label(sc2, text='LAST SEEN TIME', bg='#F0F8FF', font=('verdana', 12, 'normal')).place(x=207, y=567)
        tk.Button(sc2, text='SUBMIT', bg='#7FFFD4', font=('verdana', 15, 'normal'), command=submit_missingreport).place(x=642, y=447)
        tk.Button(sc2, text='UPLOAD IMAGE', bg='#0EF4DF', font=('verdana', 9, 'normal'), command=upload_file).place(x=397, y=447)

    sc2 = tk.Tk()
    welcome.destroy()
    sc2.title("Database Section")
    sc2.geometry('900x650')
    sc2.resizable(width=0, height=1)
    sc2.configure(background='#F0F8FF')
    l1 = tk.Label(sc2, text="Tamilnadu Police Data Management System", font=font_head, foreground="Blue", width=1280)
    l1.pack()
    l4 = tk.Label(sc2, text="CRIMINAL SEARCH SYSTEM", foreground="White", background="Red", font=font_subhead)
    l4.pack()
    b2 = tk.Button(sc2, text='SEARCH BASED ON IMAGE', bg='#00FFFF', font=('courier', 12, 'normal'), command=search_img)
    b2.place(x=47, y=247)
    b3 = tk.Button(sc2, text='SEARCH BASED ON NAME', bg='#00FFFF', font=('courier', 12, 'normal'),
                   command=search_name).place(x=357, y=247)
    b4 = tk.Button(sc2, text='FILE NEW REPORT', bg='#00FFFF', font=('courier', 12, 'normal'), command=new_report).place(
        x=667, y=247)
    name1, lastseentime, contacts, lastseenplace, info="","","","",""


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
