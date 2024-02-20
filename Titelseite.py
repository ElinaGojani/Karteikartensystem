from tkinter import *

import tkinter.font as font

# Fenster "Titelseite" erstellen
titelseite = Tk()
titelseite.title('Wilkommen im Karteikartensystem')

# Ikon hinzufügen (auskommentiert)
titelseite.iconbitmap("hand-page01.ico")

# Hintergrundfarbe von "Hinzufügen" auf oliv setzen
titelseite.configure(bg='olive')

# Schriftart, Schriftgröße und Breite definieren
myFont = font.Font(size=50, weight="bold", family="Helvetica")

# Beschriftung
Wilkommen = Label(titelseite, text="Wilkommen im Karteikartensystem \n von Elina und Lea", bg='darkgrey', fg='white',
                  height=5, width=35, font=myFont).grid(row=3, column=1)

titelseite.mainloop()
