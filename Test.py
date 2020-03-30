from tkinter import Button, Label, Tk

fenetre = Tk()
fenetre.title('Hello World!')

mon_label = Label(test='Je suis du texte')
mon_label.grid()

mon_label2 = Label(text='Je suis aussi du texte')
mon_label2.grid()

mon_bouton = Button(text='Cliquez sur moi')
mon_bouton.grid()

fenetre.mainloop()