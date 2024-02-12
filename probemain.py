# main.py
import tkinter as tk
from tkinter import messagebox
import sys
import time
import subprocess

def execute_titelseite():
    """
    Führt Titelseite.py für 3 Sekunden aus und öffnet Forumseite.py.
    """
    try:
        # Start Titelseite.py
        titelseite_process = subprocess.Popen(["python", "Titelseite.py"])

        # Wait for 3 seconds
        time.sleep(3)

        # Close Titelseite.py
        titelseite_process.terminate()

        # Open Forumseite.py
        subprocess.Popen(["python", "Forumseite.py"])

    except FileNotFoundError:
        print("Error: Make sure Titelseite.py and Forumseite.py exist in the same directory.")



if __name__ == "__main__":
    execute_titelseite()

# In der Datei "Forumseite.py"

import tkinter as tk
from tkinter import messagebox

class Forumseite:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Forumseite")

        # Button erstellen
        self.hinzufuegen_button = tk.Button(self.root, text="Hinzufügen", command=self.hinzufuegen)
        self.hinzufuegen_button.pack()
# Button zum Öffnen des Lernen-Fensters
#learn_button = tk.Button(root, text="Lernen", command=open_learning_window)
#learn_button.pack()

    def hinzufuegen(self):
        # Hier wird das Fenster "Forumseite.py" geschlossen
        self.forumseite.destroy()

        # Und das Fenster "Hinzufuegen.py" geöffnet
        hinzufuegen_window = tk.Toplevel(self.forumseite)
        hinzufuegen_window.title("Hinzufuegen")
        # Hier kannst du den Inhalt des Hinzufuegen-Fensters gestalten

if __name__ == "__main__":

    forumseite = Forumseite()
    forumseite.mainloop()
