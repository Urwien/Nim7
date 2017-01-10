##Nim-7 Spel applicatie

Nim-7 is een python programma waarmee het spel Nim gespeeld kan worden.

###Spelregels

Het spel wordt gespeeld met twee spelers. Er wordt willekeurig bepaalt wie als eerste aan de beurt is. De speler die
de beurt heeft kan één of twee munten van een stapel van zeven munten pakken. Daarna gaat de beurt naar de andere speler.
De speler die de laatste munt weet te pakken wint het spel.

###Gebruikshandleinding

Het programma is te starten door **main.py** uit te voeren. Hierdoor verschijnt het venster. Op het venster zijn aan de
linkerkant de knoppen voor speler 1 te zien en aan de rechterkant die van speler 2. Speler 1 heeft een rode achtergrond
en speler 2 een blauwe. In het midden van het venster is te zien hoeveel munten er op de stapel liggen en welke speler er
aan de beurt is.

Met de knoppen _pak één munt_ en _pak twee munten_ zijn respectievelijk één of twee munten van de stapel af te halen. Nadat
de speler munten heeft gepakt gaat de beurt naar de volgende speler. Een speler kan tijdens zijn of haar eigen beurt alleen
op zijn eigen knoppen klikken. Indien er nog maar één munt op de stapel ligt kan de speler er alleen voor kiezen om één munt
te pakken.

Wanneer een speler de laatse munt heeft gepakt wordt er getoont wie er heeft gewonnen en wordt de stapel opnieuw gevuld.

###Code

Het programma is geschreven in **Python 3** en maakt gebruik van de _tkinter_ module voor de gebruikersinterface. _Tkinter_
wordt standaard meegeleverd met **Python**.

De resolutie en het aantal munten op de stapel zijn in de code te wijzigen maar hebben respectiefelijk standaard de waarden
_400x300_ en _7_. Het aanpassen van deze waarden moet gebeuren in de **main.py** module. Dit gaat gemakkelijk door de
waarde aan te passen die worden meegegeven aan de constructor van het Gui object.