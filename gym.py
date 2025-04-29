from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#galvenais logs
logs = Tk()
logs.geometry("400x500") #loga izmērs
logs.title("Sporta zāle")
logs.configure(background="lime")

def aprekinat():
    abonements = abonements_var.get()
    trenins = trenins_.get()
    pakalpojums = pakalpojums_var.get()

    if abonements == "Gada":
        abonements = 365

        if trenins == "Svaru zāle":
            trenins = 5

            if pakalpojums == "Baseins":
                    pakalpojums = 3
            elif pakalpojums == "Sauna":
                    pakalpojums = 2
            elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
            elif pakalpojums == "-":
                    pakalpojums = 0


    if abonements == "Mēneša":
        abonements = 31

        if trenins == "Svaru zāle":
            trenins = 0.2

            if pakalpojums == "Baseins":
                    pakalpojums = 3
            elif pakalpojums == "Sauna":
                    pakalpojums = 2
            elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
            elif pakalpojums == "-":
                    pakalpojums = 0



            if rajons == "Jūrmala":
                rajons = 5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "-":
                    pakalpojums = 0

    if abonements == "Izmēģinājuma":
        abonements = 1

        if trenins == "Grupas treniņš":
            trenins = 5

            if rajons == "Ķengarags":
                rajons = 1

                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "-":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "-":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "-":
                    pakalpojums = 0












    kopējā_cena = cena_dienā * nomas_dienas
    rez_label.config(text=f"Jūsu kopējā cena ir {kopējā_cena}")


dzinejs_var = StringVar()
auto_markas_var = StringVar()
nomas_dienas_var = StringVar()
auto_veids_var = StringVar()

#auto markas izvēle
ttk.Label(logs, text="Izvēlēties auto marku:").grid(row=1, column=0,padx=20,pady=20)
auto_markas = ttk.Combobox(logs, textvariable = auto_markas_var)
auto_markas["values"] = ("Volvo", "Nissan", "Mercedes")
auto_markas.grid(column=1, row=1)

ttk.Label(logs, text="Izvēlēties dzinēju:").grid(row=2, column=0,padx=20,pady=20)
dzinejs= ttk.Combobox(logs, textvariable = dzinejs_var)
dzinejs["values"] = ("Dīzelis", "Koka", "Elektriskais")
dzinejs.grid(column=1, row=2)

ttk.Label(logs, text="Izvēlēties auto veidu:").grid(row=3, column=0,padx=20,pady=20)
auto_veids = ttk.Combobox(logs, textvariable = auto_veids_var)
auto_veids["values"] = ("Traktors", "Vieglais", "Smagais")
auto_veids.grid(column=1, row=3)

ttk.Label(logs, text="Izvēlēties nomas dienu:").grid(row=4, column=0,padx=20,pady=20)
nomas_dienas = tk.Entry(logs, textvariable = nomas_dienas_var)
nomas_dienas.grid(column=1, row=4)


def saglabatText():
    auto_type = auto_veids.get()
    auto_mark = auto_markas.get()
    engine = dzinejs.get()
    days = nomas_dienas.get()

    with open("autonoma.txt", "a", encoding="utf-8") as file:
        file.write(f"Veids: {auto_type}, Marka: {auto_mark}, Dzinējs: {engine}, Nomas dienas: {days}")

    messagebox.showinfo("Veiksmīgi, Dati saglabāti")
    auto_veids.delete(0, END)
    auto_markas.delete(0, END)
    dzinejs.delete(0, END)
    nomas_dienas.delete(0, END)

def aizvert_window():
    logs.destroy()

aprekinat_button = tk.Button(logs, text="Aprēķināt", command = aprekinat)
aprekinat_button.grid(row=6, columnspan=1, padx=10, pady=5)
saglabat_button = tk.Button(logs, text="Saglabāt", command = saglabatText)
saglabat_button.grid(row=5, columnspan=1, padx=10, pady=5)
aizvert_button = tk.Button(logs, text="Aizvērt", command = aizvert_window)
aizvert_button.grid(row=5, columnspan=5, padx=10, pady=5)

rez_label = Label(logs, text="")
rez_label.grid(row=7, columnspan=1, padx=10, pady=5)

logs.mainloop()

