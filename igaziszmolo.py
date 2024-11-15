#importáljuk a tkintert
from tkinter import *


#ablak létrehozása
root = Tk()
#ablak elnevezése
root.title("Számológép")


#a számolós függvény létrehozás
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)    # törli a beviteli mezőt a 0.elemtől az utolsóig
        entry.insert(END, str(result))  
    except Exception as e:      # hiba esetén kiírja hogy "Hiba"
        entry.delete(0, END)
        entry.insert(END, "Hiba")



#a törlés függvény létrehozás
def clear():
    entry.delete(0, END)



#az értékek megjegyzés függvény létrehozás
def buttonclick(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + value)



#háttér szín beállítása
root.config(bg="#cce3de")



#bekérő mező megcsinálása
entry = Entry(root, bg="#a4c3b2", width=20, font=("Arial", 24), borderwidth=2, relief= "solid", justify="right")
entry.grid(column=0, row=0, columnspan=4, padx=10, pady=10)



#gombok elkészítése és elhelyezése
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0),
]
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, bg="#a4c3b2", width=5, height=2, font=("Arial", 18), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        Button(root, text=text, bg="#a4c3b2", width=5, height=2, font=("Arial", 18), command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, bg="#a4c3b2", width=5, height=2, font=("Arial", 18), command=lambda value=text: buttonclick(value)).grid(row=row, column=col, padx=5, pady=5)


#futattás
root.mainloop()