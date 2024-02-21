<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->


 ```python
# Funktion beim Klicken
def speichereDieKarte():
    text_key = entry_frage.get("1.0", tkinter.END)
    text_value = entry_antwort.get("1.0", tkinter.END)
    text_dict[text_key] = text_value
    entry_antwort.delete(1.0, tkinter.END)
    entry_frage.delete(1.0, tkinter.END)


def speichern():
    with open("Datenbank.txt", "w") as file:
        for key in text_dict.keys():
            if key and text_dict[key]:
                # schreibt key und value in "Datenbank.txt", wenn sie nicht leer sind
                file.write(f"{key}{text_dict[key]}")


def ClickForum():
    # Hier öffnen wir die "einführung.py" Datei mit subprocess
    subprocess.Popen(["python", "Forumseite.py"])
    speichern()
    master.destroy()
``` 
 <br>

![image](https://github.com/ArthurFleck35x/Karteikartensystem/assets/152798623/d8e92b9c-5295-4d16-a88d-3b53d44bf5c4) <br>


# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->
    python
    class FragenAntwortenApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fragen und Antworten")
        self.frage_antwort_liste = self.lade_fragen_antworten()
        self.aktuelle_frage_index = 0

        self.master.configure(bg='olive')
        self.master.iconbitmap("hand-page01.ico")
        self.myFont = font.Font(size=10, weight="bold", family="Helvetica")

        self.frage_label = tk.Label(master, text="Frage:", bg="olive")
        self.frage_label.grid(row=0, column=0, padx=10, pady=10)

        self.frage_text = tk.Label(master, text=self.frage_antwort_liste[self.aktuelle_frage_index], height=5, width=30,
                                   bg='darkgrey', fg='white', borderwidth=2, relief="sunken")
        self.frage_text.grid(row=0, column=1, padx=10, pady=10)

        self.antwort_button = tk.Button(master, text="Antwort", bg='darkgrey', fg='white', height=2, width=25,
                                        font=self.myFont, command=self.zeige_antwort)
        self.antwort_button.grid(row=1, column=1, padx=10, pady=10)
        self.ZumForumButton = tk.Button(master, text='Zum Forum', bg='darkgrey', fg='white', height=2, width=12,
                                        font=self.myFont, command=self.ClickForum).grid(row=0, column=3)
        self.naechste_button = tk.Button(master, text="Nächste Frage", bg='darkgrey', fg='white', height=2, width=12,
                                         font=self.myFont, command=self.naechste_frage)
        self.naechste_button.grid(row=1, column=3, padx=10, pady=10)
        


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->
Entwurf:
https://github.com/ArthurFleck35x/Karteikartensystem/blob/main/Inhalt_und_Skizzierung_des_Projekts.md <br>

Funktionsfähigkeit:


Commits:
https://github.com/ArthurFleck35x/Karteikartensystem

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->



## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- PyCharm --> PyCharm <br>
![image](https://github.com/ArthurFleck35x/Karteikartensystem/assets/152798623/758208ea-4a25-4985-8fe5-93cb393c94fd)


<!-- GitHub --> GitHub <br>
![image](https://github.com/ArthurFleck35x/Karteikartensystem/assets/152798623/01a26106-104c-4bbe-b4a9-186f74751738)


<!--SQLite--> SQLite <br>
![image](https://github.com/ArthurFleck35x/Karteikartensystem/assets/152798623/7f9a32c8-abac-48c5-997a-c6bffdd42762) <br>


<!-- VSC --> <br>

<!-- Copilot --> Copilot <br>
![image](https://github.com/ArthurFleck35x/Karteikartensystem/assets/152798623/d74098e9-a12b-4790-9b08-c5d406a26676) <br> 

Nutzung von Copilot für Beispielcode, der abgeändert wiederverwendet wird.<br>

````python
def execute_titelseite():
    '''
    Führt Titelseite.py für 3 Sekunden aus und öffnet Forumseite.py.
    '''
    try:
        # Start Titelseite.py
        titelseite_process = subprocess.Popen(["python", "Titelseite.py"])

        # Wartet für 3 Sekunden
        time.sleep(3)

        # Schließt Titelseite.py
        titelseite_process.terminate()
```

<!-- other -->



## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->
Lea: <br> 
Tom und Dustin haben mir Tipps gegeben bezüglich Struktur im Code und wahl des Moduls für die Datenbank. <br>
Louis hat mir erklärt wie ich das Objekt in der Klasse selbst anwenden sollte. <br>
Elina habe ich geholfen in das Projekt einzusteigen, in dem ich ihr Updates gegeben, die Planung und den Code für die Benutzeroberfläche übernommen habe, während sie sich um die Datenbank gekümmert hat. <br>
<br>
Elina:

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
 


<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->
siehe  "Die Studierenden können ihre Software erläutern und begründen"


## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->



## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen

