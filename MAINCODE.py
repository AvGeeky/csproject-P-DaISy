# all modules used
import random
import tkinter as tk
import smtplib
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter.messagebox import _show

# Welcome screen, login details to be shifted into a file
welcome = tk.Tk()
usernames = ["Sai", "Ayushi"]
passwords = ["123"]
registered_email = ["saipranav.sai2005@gmail.com", "ayushi16055@gmail.com"]
sixdig_pass = str(random.randint(100000, 999999))


# Database screen
def screen2():
    sc2 = tk.Tk()
    welcome.destroy()
    sc2.title("Database Section")
    sc2.state("zoomed")
    l1 = tk.Label(sc2, text="Tamilnadu Police Data Management System", font=font_head, foreground="Blue", width=1280)
    l1.pack()
    l4 = tk.Label(sc2, text="CRIMINAL SEARCH SYSTEM", foreground="White", background="Red", font=font_subhead)
    l4.place(x=505, y=40)


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
intro_image = Image.open("folder.png")
bg_img = Image.open("jurgen-jester-_PizUeTnvFE-unsplash.jpg")
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

