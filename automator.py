import time
from colorama import *
from pystyle import *
import os
import threading
import subprocess

os.system("cls")

videolink = input(Fore.CYAN + "Veuillez entrez l'URL de la vidéo : ")
videoname = input(Fore.CYAN + "Veuillez entrez le nom de la vidéo : ")

os.system(f'python main.py --url "{videolink}" --name "{videoname}"')


# Obtient le répertoire du fichier Python en cours d'exécution
current_directory = os.path.dirname(os.path.abspath(__file__))

# Ouvre une fenêtre de commande (cmd) dans le répertoire actuel
subprocess.Popen('cmd.exe', cwd=current_directory)


