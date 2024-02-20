from tkinter import *

import tkinter.font as font
import subprocess


def ClickForum1():
    # Hier öffnen wir die "einführung.py" Datei mit subprocess
    subprocess.Popen(["python", "Forumseite.py"])
    einfuehrungsseite.destroy()


# Fenster "Titelseite" erstellen
einfuehrungsseite = Tk()
einfuehrungsseite.title('Einführung')

# Ikon hinzufügen (auskommentiert)
einfuehrungsseite.iconbitmap("hand-page01.ico")

# Hintergrundfarbe von "Hinzufügen" auf oliv setzen
einfuehrungsseite.configure(bg='olive')

# Schriftart, Schriftgröße und Breite definieren
myFont = font.Font(size=10, weight="bold", family="Helvetica")

# Beschriftung
Wilkommen = Label(einfuehrungsseite, text="Im Forum findest du alles was du zum Lernen brauchst.", bg='darkgrey',
                  fg='white', height=2, width=80, font=myFont).grid(row=0, column=1)
Wilkommen1 = Label(einfuehrungsseite, text="Du kannst....", bg='darkgrey', fg='white', height=2, width=80,
                   font=myFont).grid(row=1, column=1)
Wilkommen2 = Label(einfuehrungsseite, text="- Karten hinzufügen", bg='darkgrey', fg='white', height=2, width=80,
                   font=myFont).grid(row=2, column=1)
Wilkommen3 = Label(einfuehrungsseite, text="-direkt loslegen", bg='darkgrey', fg='white', height=2, width=80,
                   font=myFont).grid(row=3, column=1)
Wilkommen4 = Label(einfuehrungsseite, text="oder sogar ", bg='darkgrey', fg='white', height=2, width=80,
                   font=myFont).grid(row=4, column=1)
Wilkommen5 = Label(einfuehrungsseite, text="-das Programm beenden", bg='darkgrey', fg='white', height=2, width=80,
                   font=myFont).grid(row=5, column=1)
Wilkommen3 = Label(einfuehrungsseite, text="\nViel Erfolg beim Lernen!", bg='darkgrey', fg='white', height=2, width=80,
                   font=myFont).grid(row=6, column=1)

ZurueckZurForumSeite = Button(einfuehrungsseite, text='Zurück zum Forum', bg='darkgrey', fg='white', height=1, width=80,
                              font=myFont, pady=1, command=ClickForum1).grid(row=7, column=1)
einfuehrungsseite.mainloop()
