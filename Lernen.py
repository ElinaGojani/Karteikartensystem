import tkinter as tk
import tkinter.font as font
import subprocess


class FragenAntwortenApp:
    def __init__(self, master):
        # Abfragen laden und Index der Frage auf 0 setzen
        self.master = master
        self.master.title("Fragen und Antworten")
        self.frage_antwort_liste = self.lade_fragen_antworten()
        self.aktuelle_frage_index = 0

        # bestimmt Hintergrundfarbe, Ikon und Schriftart
        self.master.configure(bg='olive')
        self.master.iconbitmap("hand-page01.ico")
        self.myFont = font.Font(size=10, weight="bold", family="Helvetica")

        # Frage_Label
        self.frage_label = tk.Label(master, text="Frage:", bg="olive")
        self.frage_label.grid(row=0, column=0, padx=10, pady=10)

        #Textfeld_Frage
        self.frage_text = tk.Label(master, text=self.frage_antwort_liste[self.aktuelle_frage_index], height=5, width=30,
                                   bg='darkgrey', fg='white', borderwidth=2, relief="sunken")
        self.frage_text.grid(row=0, column=1, padx=10, pady=10)

        #Antwort_Button
        self.antwort_button = tk.Button(master, text="Antwort", bg='darkgrey', fg='white', height=2, width=25,
                                        font=self.myFont, command=self.zeige_antwort)
        self.antwort_button.grid(row=1, column=1, padx=10, pady=10)
        #Forum_Button
        self.ZumForumButton = tk.Button(master, text='Zum Forum', bg='darkgrey', fg='white', height=2, width=12,
                                        font=self.myFont, command=self.ClickForum).grid(row=0, column=3)
        #Nächste_Frage_Button
        self.naechste_button = tk.Button(master, text="Nächste Frage", bg='darkgrey', fg='white', height=2, width=12,
                                         font=self.myFont, command=self.naechste_frage)
        self.naechste_button.grid(row=1, column=3, padx=10, pady=10)

    def ClickForum(self):
        # per Klick, öffnet "Forumseite.py" und schließt "Lernen.py" 
        subprocess.Popen(["python", "Forumseite.py"])
        self.master.destroy()

    def lade_fragen_antworten(self):
        #liest "Datenbank.txt" aus und gibt die Liste der Fragen und Antworten zurück
        try:
            with open("datenbank.txt", "r", encoding="utf-8") as file:
                fragen_antworten = [line.strip() for line in file.readlines()]
            return fragen_antworten
        except FileNotFoundError:
            #Fehlerbenachrichtigung
            print("Datei 'datenbank.txt' nicht gefunden.")
            return []

    def zeige_antwort(self):
        #Funktion Anwort anzeigen, erhöht ebenso den Index 
        antwort_index = self.aktuelle_frage_index + 1
        if antwort_index < len(self.frage_antwort_liste):
            antwort = self.frage_antwort_liste[antwort_index]
            self.frage_text.config(text=f"Antwort: {antwort}")
            #Button "Antwort" deaktivieren
            self.antwort_button.config(state=tk.DISABLED)
            #Button "Nächste Frage" aktivieren
            self.naechste_button.config(state=tk.NORMAL)

    def naechste_frage(self):
        #Funktion Anwort anzeigen, erhöht ebenso den Index
        self.aktuelle_frage_index += 2
        if self.aktuelle_frage_index < len(self.frage_antwort_liste):
            self.frage_text.config(text=self.frage_antwort_liste[self.aktuelle_frage_index])
            #Button "Antwort" aktivieren
            self.antwort_button.config(state=tk.NORMAL)
            #Button "Nächste Frage" deaktivieren
            self.naechste_button.config(state=tk.DISABLED)
        else:
            #bei Bearbeitung aller Fragen
            self.frage_text.config(text="Herzlichen Glückwunsch,\n alle Fragen beantwortet.")
            self.antwort_button.config(state=tk.DISABLED)
            self.naechste_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = FragenAntwortenApp(root)
    root.mainloop()
