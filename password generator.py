import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#creer la fenetre
window = Tk()
window.title("Password Generator")
window.geometry('720x480')
window.iconbitmap("favicon.ico")
window.config(background='gray')

#creer la frame principale
frame = Frame(window, bg='gray')

#creation image
width = 300
height = 300
image = PhotoImage(file="Yo.png").zoom(18).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='gray')
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticly=W)


#creer une sous boite
rigth_frame = Frame(frame, bg='Gray')

#creer un titre
label_title = Label(rigth_frameframe, text="Mot de passe", font=('Helvetica', 20), bg='gray', fg='white')
label_title.pack()


label_title.grid(rpw=0, column=1, sticky=W)

#input
password_entry = Entry(rigth_frameframe, text="Mot de passe", font=('Helvetica', 20), bg='gray', fg='white')
password_entry.pack()

#button
generate_password_button = Button(rigth_frameframe, text="Generer", font=('Helvetica', 20), bg='gray', fg='white', command=generate_password())
generate_password_button.pack(fill=X)


#afficher la frame
frame.pack(expand=YES)

#afficher la fenetre
window.mainloop()