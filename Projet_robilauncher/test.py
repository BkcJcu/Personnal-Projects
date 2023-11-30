import tkinter as tk
from PIL import Image, ImageTk
import time
import os
import threading


fenetre = tk.Tk()
fenetre.title("Animation de gif")

photo = Image.open(r"C:\Users\ryder\Desktop\Code\Projet_robilauncher\Images\pig_walking_gif\pig_walking-2.png")
image = photo.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

label_test= tk.Label(fenetre, image=photo)
label_test.pack()


def play_gif(nb_image, path, h, w, delay):
        
    while True:

        for i in range(nb_image):
            photo = Image.open(path + r"\pig_walking-" + str(i) + ".png")
            image = photo.resize((h, w), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            print("popi le pd", i)
            
            label_test.configure(image=photo)
            label_test.image = photo

            time.sleep(delay)



caca = threading.Thread(target=play_gif, args=(71, os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images", "pig_walking_gif"), 100, 100, 0.03,))
caca.start()

print(str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images", "pig_walking_gif") + r"\pig_walking-" + "3" + ".png"))

fenetre.mainloop()

