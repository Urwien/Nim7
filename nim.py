"""Nim-7 spel logica module

    Deze module heeft één methode (pak_munt) die er voor zorgt dat er
    een munt van de stapel wordt afgehaald. Als de methode een return waarde
    van true heeft, zijn de munten op en is het spel voorbij.
"""


def pak_munt(stapel, aantal_munten=1):
    """Pakt één of twee munten van de stapel en bepaalt de winnaar

        Argumenten:
        stapel        -- is van het type list en stelt de stapel van munten voor
        aantal_munten -- het aantal munten dat de speler van de stapel pakt als int (default 1)

        Return waarde:
        True          -- als de stapel gelijk en nul is (spel is voorbij)
        False         -- als de stapel groter dan nul is (spel is niet voorbij)
    """

    # controleer hoeveel munten op de stapel zitten, als er nog maar één is,
    # wint de speler die de munt pakt
    if len(stapel) == 1:
        stapel.pop()

        # Het spel is voorbij dus de methode returned True
        return True
    # als de speler de laatste twee munten pakt
    elif aantal_munten == 2 and len(stapel) == 2:
        stapel.pop()
        stapel.pop()

        return True
    else:
        # pak aantal_munten munten van de stapel
        for i in range(aantal_munten):
            stapel.pop()

        # Het spel nog niet is voorbij dus de methode returned False
        return False




