"""Startpunt van de applicatie

    In deze module wordt het programma gestart. Er wordt een object aan gemaakt van de Gui klasse uit de module
    gui.py. De constructor verwacht vier parameters waarmee respectievelijk de titel, breedte van het scherm, hoogte
    van het scherm en het aantal munten op de stapel worden ingesteld.
"""

from gui import *

# geef de titel, resolutie en het aantal munten op de stapel mee aan de constructor
gui = Gui('NIM-X', 400, 300, 7)