"""Bevat de klasse voor de GUI

"""

# Importeer tkinter op deze manier zodat de Frame klasse van tk en NIET van ttk wordt gebruikt.
# Deze heeft namelijk andere attributen.
import tkinter as tk
from tkinter import messagebox

# Door op deze manier (alles) te importeren zijn de functies en variabelen uit de geimporteerde modules
# te benaderen zonder eerst hun module naam op te geven.
from random import *
from nim import *


class Gui:
    """

    """
    def __init__(self, titel, breedte, hoogte, aantal_munten):
        """

        :param titel:
        :param breedte:
        :param hoogte:
        :param aantal_munten:
        """
        self.stapel = list(range(1, aantal_munten + 1))
        self.spelers = (1, 2)
        self.huidige_speler = choice(self.spelers)

        self.hoofd_scherm = tk.Tk()
        self.hoofd_scherm.minsize(breedte, hoogte)
        self.hoofd_scherm.resizable(width=False, height=False)
        self.hoofd_scherm.title(titel)

        self.speler_1_frame = tk.Frame(master=self.hoofd_scherm, bg='red')
        self.speler_1_label = tk.Label(master=self.speler_1_frame, text='Speler 1', fg='white', bg='red')
        self.speler_1_knop_pak_1 = tk.Button(master=self.speler_1_frame, text='Pak 1 steen', command=lambda: self.speel_beurt(1))
        self.speler_1_knop_pak_2 = tk.Button(master=self.speler_1_frame, text='Pak 2 stenen', command=lambda: self.speel_beurt(2))

        self.speler_2_frame = tk.Frame(master=self.hoofd_scherm, bg='blue')
        self.speler_2_label = tk.Label(master=self.speler_2_frame, text='Speler 2', fg='white', bg='blue')
        self.speler_2_knop_pak_1 = tk.Button(master=self.speler_2_frame, text='Pak 1 steen', command=lambda: self.speel_beurt(1))
        self.speler_2_knop_pak_2 = tk.Button(master=self.speler_2_frame, text='Pak 2 stenen', command=lambda: self.speel_beurt(2))

        self.stapel_frame = tk.Frame(master=self.hoofd_scherm)
        self.aantal_label = tk.Label(master=self.stapel_frame, text='Aantal munten:', font=('Arial', 18, 'bold'))
        self.stapel_cijfer_label = tk.Label(master=self.stapel_frame, text=str(len(self.stapel)), font=('Arial', 62, 'bold'), fg='green')
        self.beurt_label = tk.Label(master=self.stapel_frame, text='Speler {} is nu\n aan de beurt'.format(self.huidige_speler), font=('Helvetica', 12, 'italic'))

        self.toon_scherm()

    def toon_scherm(self):
        self.speler_1_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.speler_1_label.pack()
        self.speler_1_knop_pak_1.pack(fill=tk.BOTH, padx=5)
        self.speler_1_knop_pak_2.pack(fill=tk.BOTH, padx=5)

        self.speler_2_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.speler_2_label.pack()
        self.speler_2_knop_pak_1.pack(fill=tk.BOTH, padx=5)
        self.speler_2_knop_pak_2.pack(fill=tk.BOTH, padx=5)

        self.stapel_frame.pack(side=tk.TOP)
        self.aantal_label.pack()
        self.stapel_cijfer_label.pack(side=tk.TOP)
        self.beurt_label.pack(side=tk.BOTTOM)

        self.bepaal_knoppen_states()

        self.hoofd_scherm.mainloop()

    def bepaal_knoppen_states(self):
        if self.huidige_speler == 1:
            self.speler_1_knop_pak_1['state'] = 'normal'

            if len(self.stapel) == 1:
                self.speler_1_knop_pak_2['state'] = 'disabled'
            else:
                self.speler_1_knop_pak_2['state'] = 'normal'

            self.speler_2_knop_pak_1['state'] = 'disabled'
            self.speler_2_knop_pak_2['state'] = 'disabled'

            self.beurt_label['text'] = 'Speler {} is nu aan de beurt'.format(self.huidige_speler)
        else:
            self.speler_1_knop_pak_1['state'] = 'disabled'
            self.speler_1_knop_pak_2['state'] = 'disabled'
            self.speler_2_knop_pak_1['state'] = 'normal'

            if len(self.stapel) == 1:
                self.speler_2_knop_pak_2['state'] = 'disabled'
            else:
                self.speler_2_knop_pak_2['state'] = 'normal'

            self.beurt_label['text'] = 'Speler {} is nu aan de beurt'.format(self.huidige_speler)

    def verwissel_huidige_speler(self):
        if self.huidige_speler == 1:
            self.huidige_speler = 2
        else:
            self.huidige_speler = 1

    def speel_beurt(self, aantal_munten):
        # Pak aantal_munten munten van stapel
        gewonnen = pak_munt(self.stapel, aantal_munten)

        # update het aantal munten naar de user toe
        self.stapel_cijfer_label['text'] = str(len(self.stapel))

        if gewonnen:
            # toon de winnende speler
            messagebox.showinfo('Spel uitslag', 'Speler {} wint het spel!'.format(self.huidige_speler))

            # TODO: reset de stapel

        # verwissel de huidige speler en verander de states van de knoppen
        self.verwissel_huidige_speler()
        self.bepaal_knoppen_states()

        print('speler ' + str(self.huidige_speler))