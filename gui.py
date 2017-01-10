"""Bevat de klasse voor de GUI

    Deze module bevat de klasse die verantwoordelijk voor de opbouw en de functionaliteiten van de gui. Door op deze
    manier een klasse te gebruiken is het makkelijk om bij de verschillende elementen op de gui te komen. Het scherm is
    verdeelt m.b.v. drie frames. Één voor speler 1, één voor speler 2 en een frame waarop het aantal munten op de stapel
    te zien is. De module maakt gebruik van de functie pak_munt uit de module nim.py om een munt van de stapel te pakken.
    Verder wordt er gebruik gemaakt van de module random om willekeurig een speler te kiezen die het spel mag starten.
"""

# Importeer tkinter op deze manier zodat de Frame klasse van tk en NIET van ttk wordt gebruikt.
# Deze heeft namelijk andere attributen. De import voor de messagebox wordt gebruikt om de om aan te tonen welke speler
# het spel heeft gewonnen.
import tkinter as tk
from tkinter import messagebox

# Door op deze manier (alles) te importeren zijn de functies en variabelen uit de geimporteerde modules
# te benaderen zonder eerst hun module naam op te geven.
from random import *
from nim import *


class Gui:
    """Creëert de user interface en bijbehordende functionaliteit.

    De klasse Gui heeft alle user interface elementen als attributen aan zijn klasse waardoor ze makkelijk te benaderen
    zijn. Ook de stapel munten en de lijst van spelers zijn als attributen aan de klasse toegevoegd. De klasse is erg
    simpel in gebruik. Bij het aanmaken van een object hoeft de programmeur alleen maar vier parameters mee te geven
    voor de titel, breedte van het scherm, hoogte van het scherm en het aantal munten op de stapel.

    Methoden:

    __init__(titel, breedte, hoogte, aantal_munten) - Klasse contructor, intialiseert de attributten met de juiste waarden
    toon_scherm()                                   - Verantwoordelijk voor het zichtbaar maken en plaatsen van de elementen
    bepaal_knoppen_states()                         - Zorgt ervoor dat alleen de juiste knoppen beschikbaar zijn
    verwissel_huidige_speler()                      - Geeft de beurt aan de volgende speler
    speel_beurt()                                   - Verantwoordelijk voor een spelers beurt, pak munt, update stapel, toon winnaar
    reset_spel()                                    - Reset de stapel en score
    """
    def __init__(self, titel, breedte, hoogte, aantal_munten):
        """Klasse contructor

        De contructor zorgt ervoor dat alle gui elementen worden gecreëerd met de juiste waarden (tekst, positie enz).
        De programmeur geeft de vier waarden mee aan de constructor en de klasse zorgt voor de rest. Het scherm is als
        het ware opgedeeld in drie frames. Links voor speler 1, in het midden voor het aantal munten op de stapel en om
        te zien wie er aan de beurt is en rechts voor speler 2.

        :param titel: de titel van het venster
        :param breedte: de breedte in pixels van het venster
        :param hoogte: de hoogte in pixels van het venster
        :param aantal_munten: het aantal munten dat in het begin van het spel op de stapel ligt
        """

        # de stapel kan tussen de 5 en 50 munten bevatten
        if aantal_munten >= 5 and aantal_munten <= 50:
            self.stapel = list(range(1, aantal_munten + 1))
        else:
            self.stapel = list(range(1, 7 + 1))
        self.aantal_munten = aantal_munten
        self.spelers = (1, 2)
        self.huidige_speler = choice(self.spelers)

        self.hoofd_scherm = tk.Tk()

        # zorg ervoor dat er niet te kleine of te groote waarde worden op gegeven
        if (breedte >= 250 and breedte <= 1280) and (breedte >= 250 and breedte <= 1280):
            self.hoofd_scherm.minsize(breedte, hoogte)
        else:
            self.hoofd_scherm.minsize(400, 300)

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

        # maak de elementen zichtbaar en positioneer ze op de juiste plek
        self.toon_scherm()

    def toon_scherm(self):
        """Posisioneert en maakt de gui elementen zichtbaar.

        Deze methode zorgt ervoor dat per frame de elementen op de juiste plek worden geplaats. Tevens wordt in deze
        methode ook de mainloop van tkinter gestart zodat de gui events kan afhandelen.

        :return: None
        """
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

        # zorg ervoor dat speler 1 niet op de knoppen van speler 2 kan klikken en vice versa
        self.bepaal_knoppen_states()

        # tkinter event loop
        self.hoofd_scherm.mainloop()

    def bepaal_knoppen_states(self):
        """Maakt de juiste knoppen op het juiste moment beschikbaar.

        Deze methode maakt de beschikbaar en niet beschikbaar afhankelijk van welke speler er aan de beurt is. Speler 1
        kan in zijn beurt dus niet op de knoppen van speler 2 klikken. Deze methode zorgt er ook voor dat als er nog maar
        één munt op de stapel ligt, de speler er niet twee kan pakken.

        :return: None
        """
        # beurt van speler 1
        if self.huidige_speler == 1:
            self.speler_1_knop_pak_1['state'] = 'normal'

            # alleen beschikbaar als er twee of meer munten op de stapel zijn
            if len(self.stapel) == 1:
                self.speler_1_knop_pak_2['state'] = 'disabled'
            else:
                self.speler_1_knop_pak_2['state'] = 'normal'

            self.speler_2_knop_pak_1['state'] = 'disabled'
            self.speler_2_knop_pak_2['state'] = 'disabled'

            self.beurt_label['text'] = 'Speler {} is nu aan de beurt'.format(self.huidige_speler)
        # beurt van speler 2
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
        """Wisselt de speler beurt

            Deze methode wisselt de beurt van de spelers en toont welke speler er aan de beurt is.

            :return: None
        """
        if self.huidige_speler == 1:
            self.huidige_speler = 2
        else:
            self.huidige_speler = 1

    def speel_beurt(self, aantal_munten):
        """Methode voor de afhandeling van een beurt van één speler

        Deze methode maakt gebruik van de methode pak_munt uit de module nim.py. De module verwijdert munten van de stapel
        en update het aantal munten dat op de stapel ligt naar de gebruiker toe. Als het spel wordt gewonnen door een speler
        dan wordt er op een messagebox getoont welke speler heeft gewonnen en word het spel gereset m.b.v. de methode
        reset_spel().

        :param aantal_munten: het aantal munten(1 of 2) dat de speler van de stapel pakt.
        :return: None
        """
        # Pak aantal_munten munten van stapel
        gewonnen = pak_munt(self.stapel, aantal_munten)

        # update het aantal munten naar de user toe
        self.stapel_cijfer_label['text'] = str(len(self.stapel))

        if gewonnen:
            # toon de winnende speler
            messagebox.showinfo('Spel uitslag', 'Speler {} wint het spel!'.format(self.huidige_speler))

            # reset de stapel en score
            self.reset_spel()

        # verwissel de huidige speler en verander de states van de knoppen
        self.verwissel_huidige_speler()
        self.bepaal_knoppen_states()

    def reset_spel(self):
        """Reset het spel

        Zodra er een winnaar is, is deze methode verantwoordelijk voor het reseten van de stapel en dit visueel weer te
        geven aan de gebruiker.

        :return: None
        """
        self.stapel = list(range(self.aantal_munten))

        # update het aantal munten naar de user toe
        self.stapel_cijfer_label['text'] = str(len(self.stapel))