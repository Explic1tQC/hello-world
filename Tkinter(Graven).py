from tkinter import *
import webbrowser

def ouvre_lien_internet():
    webbrowser.open("https://www.youtube.com/watch?v=1Y6AtucYAGw")

#premiere fenetre
window =Tk()

# personnaliser la fenetre
window.title("MY APP BITCH!!")
window.geometry('480x360')
window.minsize(480, 360)
window.iconbitmap("favicon.ico") #mettre une icone
window.config(background='gray')

#creer la frame
frame = Frame(window, bg='gray')

#premier texte
label_title = Label(frame, text="Yessir Miller!!!", font=('Courrier',40), bg='gray')
label_title.pack(expand=YES)

#deuxieme texte
label_subtitle = Label(frame, text="On s'eclate?", font=('Courrier',40), bg='gray')
label_subtitle.pack(expand=YES)

#ajouter un premier bouton
yt_button = Button(frame, text="Lien de la mort qui tue", font=("Courrier, 25"), bg='white', command=ouvre_lien_internet)
yt_button.pack(pady=25, fill=X)

#ajouter
frame.pack(expand=YES)

# afficher
window.mainloop()