# --------------------------------------#
# Partie interface graphique
# --------------------------------------#

from tkinter import * # Gère l'interface graphique
import tkinter as tk
import tkinter.messagebox as msgbox # Gère les boîtes de dialogue
from PIL import Image, ImageTk # Gère les images
import customtkinter as ctk # Tkinter mais avec des boutons plus "jolis"

# --------------------------------------#
# Gestion des chemins de fichiers et les téléchargements
# --------------------------------------#

import os # Gère les chemins de fichiers
from pathlib import Path # Gère les chemins de fichiers
import AppOpener # Permet l'ouverture d'applications
import requests # Gère les téléchargements

# --------------------------------------#
# Gestion des éléments s'éxécutant en arrière plan
# --------------------------------------#
import threading
import time # Gère le temps


# --------------------------------------#
# GEstion du launcher Minecraft
# --------------------------------------#

import minecraft_launcher_lib 
import subprocess # Gère les processus
import sys # Gère les processus

# --------------------------------------#
# Librairies supplémentaires
# --------------------------------------#

import playsound as ps # Gère les sons




class robilauncher:
    def __init__(self):

        self.root = ctk.CTk()
        self.root.resizable(width=0,height=0)
        self.root.geometry("850x550")
        self.root.title("Robi Launcher")

        #--------------------------------------#
        # Création de la fenêtre
        #--------------------------------------#


        # Bouton de confirmation de l'âge

        result = msgbox.askyesno(title="Robi Launcher", message="Bienvenue sur le Robi Launcher ! Avant de pouvoir utiliser le Launcher, nous devons vérifier si vous êtes majeur !")
        if result:
            pass
        else:
            sys.exit()
    

        self.label = tk.Label(self.root, bg="gray14", text="Robi Launcher", foreground="white", font=("Minecraft", 35))
        self.label.pack(padx = 0 , pady = 25)

        # Boutton de téléchargement de la version Forge requise pour jouer sur le serveur
        self.button_dlforge = ctk.CTkButton(self.root, fg_color=("red"), text="Download Forge", text_color="white", font=("Minecraft", 25), command = lambda : download("forge"))
        self.button_dlforge.pack(padx = 0 , pady = 10)

        # Boutton de téléchargement des mods requis pour jouer sur le serveur
        self.button_dlmods = ctk.CTkButton(self.root, fg_color=("orange"), text="Download Mods", font=("Minecraft", 25), command = lambda : download("mods"))
        self.button_dlmods.pack(padx = 0 , pady = 10)

        # Bouton pour ouvrir le launcher Minecraft
        self.button_openmc = ctk.CTkButton(self.root, fg_color=("green"), text="Open Minecraft", font=("Minecraft", 25), command = open_minecraft)
        self.button_openmc.place(x=325, y=480)

        # Bouton pour ouvrir la calculatrice
        calculatoricon = PhotoImage(file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images", "calculator.png"))
        calculator = calculatoricon.subsample(9, 9)
        self.button_calculator = tk.Button(self.root, image=calculator, background="gray14", text="Calculator", font=("Minecraft", 25), borderwidth=0, command = open_calculator)
        self.button_calculator.configure(width="40", height="45")
        self.button_calculator.place(x=20, y= 480)

        # Bouton pour ouvrir le lecteur de vidéos  

        videoicon = PhotoImage(file =  r"c:\Users\ryder\Desktop\Code\Projet_robilauncher\Images\videoicon.png")
        videoicon = videoicon.subsample(10, 10)
        self.button_videoplayer = tk.Button(self.root, image = videoicon, background=("gray14") ,text="NayxoBrocolis", font=("Arial", 25), borderwidth=0, command = open_videoplayer)
        self.button_videoplayer.configure(width="55", height="60") 
        self.button_videoplayer.place(x=780, y= 480)
        
        eugeugy = resize_image(300, 220, os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images", "RAPHAELLEGROSDEGUEU.png"))
        label_image = tk.Label(self.root, image=eugeugy, bg="gray14") # Créer un widget Label pour afficher l'image
        label_image.place(x=250, y=250)

        #--------------------------------------#

        # Jouer le Gif

        def play_gif(nb_image, name, path, h, w, delay, posx, posy):
            # Créer le widget Label une fois
            label_test = tk.Label(self.root, bg="gray14")
            label_test.pack()

            while True:
                for i in range(nb_image):
                    # Charger l'image suivante
                    photo = Image.open(os.path.join(path, f"{name}-{i}.png"))
                    image = photo.resize((h, w), Image.ANTIALIAS)
                    photo = ImageTk.PhotoImage(image)

                    # Placer le widget Label et le mettre à jour
                    label_test.place(x=posx, y= posy)
                    label_test.configure(image=photo)
                    
                    label_test.image = photo


                    time.sleep(delay)

        # Utiliser le threading pour exécuter la fonction en arrière-plan
        gifcochon = threading.Thread(target=play_gif, args=(71, "pig_walking", os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images", "pig_walking_gif"), 165, 165, 0.03, -15, -35,))
        gifcochon.daemon = True # Lorsque le programme principal se termine, le thread se termine également
        gifcochon.start()

        #--------------------------------------#
        self.root.mainloop()





    

def open_minecraft():
    AppOpener.open("Minecraft Launcher") 

    


def download(whatToDownload):
    flag = False
    if whatToDownload == "forge":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.2.9/forge-1.18.2-40.2.9-installer.jar"
        flag = True
        
    elif whatToDownload == "mods":
        url = "https://download1588.mediafire.com/llw18wys4xzg3L6cAwWNQ16J9C8s9JrOMqM8NWXbve85RxiC8JfuQvCpX4PmEsrJgy7JNk5fQFJ3a3gGvcD2FYXZKWBjHgjZi0mxhM1lRvdjeYUsAIHwA8ve2iczynZMuu_jaxtaBnX-lb3Xe5N_IgDWoOKSTeMigR_qcbCqj7KR/fc86jc07b1iixyc/Exemples_Valeur_Cible.xlsx"
        flag = True
    else: 
        msgbox.showerror(title = "Download - Error", message = "An error occured, wrong parameter in download function")
        flag = False
    if flag:
        r = requests.get(url)
        filename = url.split('/')[-1] # Recupère le nom du fichier à partir de l'url, chaque éléments séparés par un / est une partie de l'url, on récupère la dernière partie, le nom du fichier.
        user_folder = str(Path.home())
        destination_path = os.path.join(user_folder, "Downloads", filename)  # Lie les différents éléments du chemin de fichier, ici, le dossier de l'utilisateur, le dossier Downloads et le nom du fichier
        
        if os.path.exists(destination_path): # Vérifie si le fichier existe déjà
            result = msgbox.askyesno(title="Download Forge - Error", message="Le fichier existe déjà ! Souhaitez-vous le supprimer afin de télécharger le nouveau fichier ?")
            if result: # Si l'utilisateur souhaite supprimer le fichier existant, on le supprime
                os.remove(destination_path)

                with open(destination_path, 'wb') as out_file: # On re-télécharge le fichier après l'avoir supprimé
                    out_file.write(r.content)
                msgbox.showinfo(title="Download Forge", message="You successfully downloaded Forge !" + "\n" + "File saved in " + destination_path)
            else:
                msgbox.showerror(title="Download Forge", message ="Download cancelled")
        else: # Si le fichier n'existe pas, on le télécharge
            with open(destination_path, 'wb') as out_file:
                    out_file.write(r.content)
            msgbox.showinfo(title="Download Forge", message="You successfully downloaded Forge !" + "\n" + "File saved in " + destination_path)


def open_videoplayer():
    AppOpener.open("Windows media player", match_closest=True)
    # Ajouter un vrai lecteur de vidéo intégré au launcher


def open_calculator():
    for i in range(1):
        AppOpener.open("Calculator", match_closest=True)
    

def resize_image(h, w, path):
    photo = Image.open(path)
    image = photo.resize((h, w), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


robilauncher()