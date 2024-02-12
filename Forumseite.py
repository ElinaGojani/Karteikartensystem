import tkinter as Tk
from tkinter import *
import tkinter.font as font

import subprocess
import probemain


#Fenster "Titelseite" erstellen
forumseite =  Tk()
(forumseite.title('Wilkommen im Karteikartensystem'))

# Ikon hinzufügen (auskommentiert)
forumseite.iconbitmap("hand-page01.ico")


#Schriftart, Schriftgröße, und Breite
myFont = font.Font(size=20, weight="bold",family="Helvetica")
def ClickEinfuehrung():
    # Hier öffnen wir die "einführung.py" Datei mit subprocess
    subprocess.Popen(["python", "Einführung.py"])
    forumseite.destroy()
def ClickLernen():
    # Hier öffnen wir die "einführung.py" Datei mit subprocess
    subprocess.Popen(["python", "Lernen.py"])
    forumseite.destroy()

def ClickHinzufuegen():
    # Hier öffnen wir die "einführung.py" Datei mit subprocess
    subprocess.Popen(["python", "Hinzufügen.py"])
    forumseite.destroy()

def Beenden():
    forumseite.destroy()

#Button Einführung
EinfuehrungButton = Button(forumseite, text='Einführung', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command = ClickEinfuehrung).grid(row=1, column=1)

#Button Lernen
LernenButton = Button(forumseite, text='Lernen', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command = ClickLernen ).grid(row=2, column=1)

#Button Hinzufügen
HinzufuegenButton = Button(forumseite, text='Hinzufügen', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command= ClickHinzufuegen ).grid(row=1, column=2)

#Button Beenden
BeendenButton = Button(forumseite, text='Beenden', bg='darkgrey', fg='white', height=10, width=35,font = myFont, command= Beenden).grid(row=2, column=2)



#Hintergrundfarbe von "Hinzufügen" oliv
forumseite.configure(bg='olive')








mainloop()