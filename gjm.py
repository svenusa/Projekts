from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

# galvenais logs
logs = Tk()
logs.geometry("400x500")
logs.title("Sporta zāles rezervācija")
logs.configure(background="lightblue")

def aprekinat():
    try:
        abonements = abonements_var.get()
        trenins = trenins_var.get()
        pakalpojums = pakalpojums_var.get()
        dienas = int(dienas_var.get())

        if not abonements or not trenins or not pakalpojums:
            messagebox.showerror("Kļūda", "Lūdzu aizpildiet visus laukus!")
            return

        # Cenu noteikšana
        cenas_abon = {"Dienas": 5, "Nedēļas": 25, "Mēneša": 60}
        cenas_trenini = {"Svara zāle": 0, "Kardio": 2, "Joga": 3}
        cenas_pakalpojumi = {"Sauna": 4, "Baseins": 5, "Masāža": 10}

        cena_dienā = cenas_abon[abonements] + cenas_trenini[trenins] + cenas_pakalpojumi[pakalpojums]
        kopā = cena_dienā * dienas

        rez_label.config(text=f"Kopējā cena: {kopā} €")
    except ValueError:
        messagebox.showerror("Kļūda", "Lūdzu ievadiet pareizu dienu skaitu!")

def saglabatText():
    abonements = abonements_box.get()
    trenins = trenins_box.get()
    pakalpojums = pakalpojums_box.get()
    dienas_skaits = dienas.get()

    with open("sportazale.txt", "a", encoding="utf-8") as file:
        file.write(f"Abonements: {abonements}, Treniņš: {trenins}, Pakalpojums: {pakalpojums}, Dienas: {dienas_skaits}\n")

    messagebox.showinfo("Veiksmīgi", "Dati saglabāti!")
    abonements_box.set('')
    trenins_box.set('')
    pakalpojums_box.set('')
    dienas.delete(0, END)

def aizvert_window():
    logs.destroy()

# Mainīgie
abonements_var = StringVar()
trenins_var = StringVar()
pakalpojums_var = StringVar()
dienas_var = StringVar()

# UI elementi
ttk.Label(logs, text="Izvēlies abonementu:").grid(row=0, column=0, padx=20, pady=10)
abonements_box = ttk.Combobox(logs, textvariable=abonements_var)
abonements_box["values"] = ("Dienas", "Nedēļas", "Mēneša")
abonements_box.grid(column=1, row=0)

ttk.Label(logs, text="Izvēlies treniņu:").grid(row=1, column=0, padx=20, pady=10)
trenins_box = ttk.Combobox(logs, textvariable=trenins_var)
trenins_box["values"] = ("Svara zāle", "Kardio", "Joga")
trenins_box.grid(column=1, row=1)

ttk.Label(logs, text="Izvēlies pakalpojumu:").grid(row=2, column=0, padx=20, pady=10)
pakalpojums_box = ttk.Combobox(logs, textvariable=pakalpojums_var)
pakalpojums_box["values"] = ("Sauna", "Baseins", "Masāža")
pakalpojums_box.grid(column=1, row=2)

ttk.Label(logs, text="Dienu skaits:").grid(row=3, column=0, padx=20, pady=10)
dienas = tk.Entry(logs, textvariable=dienas_var)
dienas.grid(column=1, row=3)

# Pogas
aprekinat_button = tk.Button(logs, text="Aprēķināt", command=aprekinat)
aprekinat_button.grid(row=4, column=0, padx=10, pady=10)

saglabat_button = tk.Button(logs, text="Saglabāt", command=saglabatText)
saglabat_button.grid(row=4, column=1, padx=10, pady=10)

aizvert_button = tk.Button(logs, text="Aizvērt", command=aizvert_window)
aizvert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

rez_label = Label(logs, text="", background="lightblue")
rez_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

logs.mainloop()
