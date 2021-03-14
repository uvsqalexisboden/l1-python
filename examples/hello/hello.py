import tkinter as tk

cote = 50
pause = False

def bouton_pause():
    global pause
    if not pause:
        bouton.config(text= "Restart")
        pause = True
    else:
        bouton.config(text= "Pause")
        pause = False

def change_taille(event):
    global cote
    global carre
    x = event.x
    y = event.y
    if not pause:
        if 250-cote//2 <= x <= 250+cote//2 and 250-cote//2 <= y <= 250+cote//2 and cote >= 20:
            cote -= 10
            canvas.delete(carre)
            carre = canvas.create_rectangle((250-cote//2,250-cote//2),(250+cote//2,250+cote//2), fill= "red")
        elif not 250-cote//2 <= x <= 250+cote//2 and not 250-cote//2 <= y <= 250+cote//2 and cote <= 100:
            cote += 10
            canvas.delete(carre)
            carre = canvas.create_rectangle((250-cote//2,250-cote//2),(250+cote//2,250+cote//2), fill= "red")

racine = tk.Tk()

canvas = tk.Canvas(racine, height = 500, width = 500, bg ="white")
bouton = tk.Button(text = "Pause", command = bouton_pause)

carre = canvas.create_rectangle((250-cote//2,250-cote//2),(250+cote//2,250+cote//2), fill= "red")


canvas.grid(row=0)
bouton.grid(row=1)
canvas.bind("<Button-1>", change_taille)
racine.mainloop()
