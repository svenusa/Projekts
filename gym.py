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
    trenins = trenins_var.get()
    pakalpojums = pakalpojums_var.get()
    rajons = rajons_var.get()

    if abonements == "Gada":
        abonements = 365

        if trenins == "Svaru zāle":
            trenins = 1.2

            if rajons == "Ķengarags":
                rajons = 0.1

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 0.3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 0.5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

        if trenins == "Grupas treniņš":
            trenins = 1.4

            if rajons == "Ķengarags":
                rajons = 0.1

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 0.3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 0.5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

        if trenins == "Kardio":
            trenins = 0.8

            if rajons == "Ķengarags":
                rajons = 0.1

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 0.5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

    if abonements == "Mēneša":
        abonements = 31

        if trenins == "Svaru zāle":
            trenins = 1.3

            if rajons == "Ķengarags":
                rajons = 0.1

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 0.3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 0.5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

        if trenins == "Grupas treniņš":
            trenins = 1.5

            if rajons == "Ķengarags":
                rajons = 0.1

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 0.3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 0.5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if trenins == "Kardio":
                 trenins = 0.9

            if rajons == "Ķengarags":
                rajons = 0.1

                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 0.3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 0.5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 0.3
                elif pakalpojums == "Sauna":
                    pakalpojums = 0.2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 0.1
                elif pakalpojums == "Nav":
                    pakalpojums = 0



    if abonements == "Izmēģinājuma":
            abonements = 1

            if trenins == "Svaru zāle":
                trenins = 5

            if rajons == "Ķengarags":
                rajons = 1

                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if trenins == "Grupas treniņš":
                trenins = 7

            if rajons == "Ķengarags":
                rajons = 1

                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if trenins == "Kardio":
                 trenins = 4

            if rajons == "Ķengarags":
                rajons = 1

                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jēkabpils":
                rajons = 3
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0

            if rajons == "Jūrmala":
                rajons = 5
                
                if pakalpojums == "Baseins":
                    pakalpojums = 3
                elif pakalpojums == "Sauna":
                    pakalpojums = 2
                elif pakalpojums == "Masāžas krēsls":
                    pakalpojums = 1
                elif pakalpojums == "Nav":
                    pakalpojums = 0


    kopējā_cena = abonements*(trenins + pakalpojums + rajons)
    rez_label.config(text=f"Jūsu kopējā cena ir {kopējā_cena}€")


abonements_var = StringVar()
trenins_var = StringVar()
pakalpojums_var = StringVar()
rajons_var = StringVar()

#auto markas izvēle
ttk.Label(logs, text="Izvēlēties abonementa veidu:").grid(row=1, column=0,padx=20,pady=20)
abonements = ttk.Combobox(logs, textvariable = abonements_var)
abonements["values"] = ("Gada", "Mēneša", "Izmēģinājuma")
abonements.grid(column=1, row=1)

ttk.Label(logs, text="Izvēlēties treniņa veidu:").grid(row=2, column=0,padx=20,pady=20)
trenins= ttk.Combobox(logs, textvariable = trenins_var)
trenins["values"] = ("Svaru zāle", "Grupas treniņš", "Kardio")
trenins.grid(column=1, row=2)

ttk.Label(logs, text="Izvēlēties pakalpojumu:").grid(row=3, column=0,padx=20,pady=20)
pakalpojums = ttk.Combobox(logs, textvariable = pakalpojums_var)
pakalpojums["values"] = ("Baseins", "Sauna", "Masāžas krēsls", "Nav")
pakalpojums.grid(column=1, row=3)

ttk.Label(logs, text="Izvēlēties rajonu:").grid(row=4, column=0,padx=20,pady=20)
rajons = ttk.Combobox(logs, textvariable = rajons_var)
rajons["values"] = ("Jūrmala", "Jēkabpils", "Ķengarags")
rajons.grid(column=1, row=4)


def saglabatText():
    subs = abonements.get()
    training = trenins.get()
    services = pakalpojums.get()
    region = rajons.get()

    with open("sportazale.txt", "a", encoding="utf-8") as file:
        file.write(f"Abonementa veids: {subs}, Treniņa veids: {training}, Pakalpojums: {services}, Rajons: {region}")

    messagebox.showinfo("Veiksmīgi, Dati saglabāti")
    abonements.delete(0, END)
    trenins.delete(0, END)
    pakalpojums.delete(0, END)
    rajons.delete(0, END)

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

