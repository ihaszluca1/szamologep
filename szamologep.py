from tkinter import *

# Funkciók a műveletekhez
def button_click(value):
    current = entry.get()
    entry.delete(0, END)  # Töröljük az aktuális bejegyzést
    entry.insert(END, current + value)  # Hozzáadjuk a következő számot/műveletet

def clear():
    entry.delete(0, END)  # Töröljük a beviteli mezőt

def calculate():
    try:
        result = eval(entry.get())  # Kiértékeljük a matematikai kifejezést
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Hiba")

# Ablak létrehozása
root = Tk()
root.title("Számológép")

# Beviteli mező
entry = Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Gombok elrendezése
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Gombok hozzáadása a tkinter ablakhoz
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, bg="#edffd3",width=5, height=2, font=("Arial", 18), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        Button(root, text=text, bg="#edffd3", width=5, height=2, font=("Arial", 18), command=clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, bg="#edffd3", width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value)).grid(row=row, column=col, padx=5, pady=5)

# Futtatás
root.mainloop()















#Utasítás cimke
#cimke = Label(root, text="Tippelj egy számot")
#cimke.pack()


#Bekérés
#bemenet = Entry(root)
#bemenet.pack()




# Event loop létrehozása
root.mainloop()