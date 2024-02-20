# main.py
import time
import subprocess


def execute_titelseite():
    """
    Führt Titelseite.py für 3 Sekunden aus und öffnet Forumseite.py.
    """
    try:
        # Start Titelseite.py
        titelseite_process = subprocess.Popen(["python", "Titelseite.py"])

        # Wartet für 3 Sekunden
        time.sleep(3)

        # Schließt Titelseite.py
        titelseite_process.terminate()

        # Öffnet Forumseite.py
        subprocess.Popen(["python", "Forumseite.py"])
        
    #Aussgabe zur Fehlerbehebung
    except FileNotFoundError:
        print("Error: Make sure Titelseite.py and Forumseite.py exist in the same directory.")


if __name__ == "__main__":
    execute_titelseite()
