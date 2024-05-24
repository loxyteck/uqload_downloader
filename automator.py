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

current_directory = os.path.dirname(os.path.abspath(__file__))
subprocess.Popen('cmd.exe', cwd=current_directory)


