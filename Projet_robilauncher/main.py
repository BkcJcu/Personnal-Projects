from launchminecraft import launch
from tkinter import *

window = Tk()
window.geometry("220x120")
window.resizable(False, False)

def valider():
    info.config(fg="black")
    info["text"] = "lancement !"
    info.update()
    s = launch(emailen.get(), mdpe.get())
    if s == "mdpi":
        info.config(fg="red")
        info["text"] = "Identifiants incorectes !"
    else:
        window.destroy()
        pass


vide = Label(window, text="    ")
vide.grid(row=0, column=0)

emaill = Label(window, text="  email : ")
emaill.grid(row=1, column=0)

emailen = Entry(window)
emailen.grid(row=1, column=1)

mdpl = Label(window, text="    m.d.p : ")
mdpl.grid(row=2, column=0)

mdpe = Entry(window, show="●")
mdpe.grid(row=2, column=1)

valid = Button(window, text="jouer !", command=valider)
valid.grid(row=3, column=1)

info = Label(window, text=" ")
info.grid(row=4, column=1)

mainloop()
