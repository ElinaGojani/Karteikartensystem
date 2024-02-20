import tkinter
from tkinter import *
import tkinter.font as font
import subprocess

# Fenster "Hinzufügen erstellen"
master = Tk()
master.title('Hinzufügen')

# Ikon hinzufügen
master.iconbitmap("hand-page01.ico")

# Hintergrundfarbe von "Hinzufügen" oliv
master.configure(bg='olive')

# Schriftart, Schriftgröße und Breite
myFont = font.Font(size=10, weight="bold", family="Helvetica")

# Eingabefelder
label_frage = Label(master, text='Frage:', font=myFont, bg='olive', fg='white')
label_frage.grid(row=0, column=0)
entry_frage = tkinter.Text(master, height=5, width=30, bg='darkgrey', fg='white', borderwidth=5)
entry_frage.grid(row=1, column=0)
label_antwort = Label(master, text='Antwort:', font=myFont, bg='olive', fg='white')
label_antwort.grid(row=2, column=0)
entry_antwort = tkinter.Text(master, height=5, width=30, bg='darkgrey', fg='white', borderwidth=5)
entry_antwort.grid(row=3, column=0)

# platzhalter für datenbank
text_dict = {}


# Funktion beim Klicken
def speichereDieKarte():
    #liest das "entry_frage" aus und speichert den Text in "text_key"
    text_key = entry_frage.get("1.0", tkinter.END)
    #liest das "entry_antwort" aus und speichert den Text in "text_value"
    text_value = entry_antwort.get("1.0", tkinter.END)
    #key und value dem Dictionary anfügen
    text_dict[text_key] = text_value
    #Text aus den Eingabefeldern löschen
    entry_antwort.delete(1.0, tkinter.END)
    entry_frage.delete(1.0, tkinter.END)

# Funktion zum speichern von key und value im "text_dict" (Dictionary)
def speichern():
    # "Datenbank.txt" öffnen und Inhalt löschen oder Datei erstellen
    with open("Datenbank.txt", "w") as file:
        for key in text_dict.keys():
            # prüft ob key und value leer sind
            if key and text_dict[key]:
                # schreibt key und value in "Datenbank.txt", wenn sie nicht leer sind
                file.write(f"{key}{text_dict[key]}")


def ClickForum():
    # Hier öffnen wir die "Forumseite.py" Datei mit subprocess und schließen "Hinzufügen.py"
    subprocess.Popen(["python", "Forumseite.py"])
    speichern()
    master.destroy()


# Buttons hinzufügen
label1 = tkinter.Label(master, text="           ", bg='olive').grid(row=1, column=1)
label2 = tkinter.Label(master, text="           ", bg='olive').grid(row=3, column=1)

# Button zum eingeben der Frage
HinzufuegenButton = Button(master, text='Frage hinzufügen', bg='darkgrey', fg='white', height=1, width=30, font=myFont,
                           pady=1, command=speichereDieKarte).grid(row=3, column=2)

# Button zum eingeben der Antwort
ZurueckZurForumSeite = Button(master, text='Zurück zum Forum', bg='darkgrey', fg='white', height=1, width=30,
                              font=myFont, pady=1, command=ClickForum).grid(row=1, column=2)

mainloop()
