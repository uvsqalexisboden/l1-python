import tkinter as tk
import random as rd

def dessin_cercle():
    x= rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_oval(x, y, x+100, y+100, fill="blue")

def dessin_carre():
    x= rd.randint(0,400)
    y=rd.randint(0,400)
    canvas.create_rectangle(x, y, x+100, y+100, fill="red")

def dessin_croix():
    x1= rd.randint(0,400)
    y1=rd.randint(0,400)

    x2=x1+100
    y2=y1+100

    x3=x1+100
    y3=y1

    x4=x1
    y4=y1+100
    canvas.create_line(x1, y1, x2, y2, fill="yellow")
    canvas.create_line(x3, y3, x4, y4, fill="yellow")




racine = tk.Tk()

bouton_cercle = tk.Button(racine, text="Cercle", bg="Red",command=dessin_cercle)
bouton_carre = tk.Button(racine, text="Carre", fg="blue", command=dessin_carre)
bouton_croix = tk.Button(racine, text="Croix", padx=20, command=dessin_croix)
bouton_couleur = tk.Button(racine, text="Choisir une couleur", font=("times", 20))
canvas = tk.Canvas(racine, width=500, height=500, bd=20, relief="raised", bg="black")


bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
bouton_couleur.grid(column=1, row=0)
canvas.grid(column=1, row=1, rowspan=3)

racine.mainloop()