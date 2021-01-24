# Laboration 1 - Python: Klasser, filer och listor
## SimaManager
Under _Applications_ och sedan _CSC_ hittar du _SimaManager_. I fönstret som öppnas kan du välja kursen _tilda_. Denna kö använder du när det är full rulle under labbarna och du vill få tag på en assistent. Är det lugnt så är det bara att vifta så kommer vi!

Vid redovisningar går vi istället efter bokningslistan (som sätts upp på tavlan i salen).

## Parprogrammering
Laborationerna görs i grupper om två. Under denna kursomgång är parprogrammering obligatoriskt.

1. Läs på om parprogrammering på sidan [http://www.csc.kth.se/tcs/projects/cerise/parprogrammering/riktlinjer.html](http://www.csc.kth.se/tcs/projects/cerise/parprogrammering/riktlinjer.html)
2. Byt roller ungefär var 20:e minut. Senare kommer ni att kunna använda parprogrammeringsverktyget parkour (men det fungerar inte idag).
  * (Se till att båda i paret har loggat in på [http://parkour.csc.kth.se](http://parkour.csc.kth.se/) (en i taget eller båda samtidigt).
  * Låt en i paret logga in i verktyget och mata in sin labbkompis, kurs och labbnamn i sina respektive fält. Klicka skapa.
  * Klicka på timer. Här kan ni starta en timer för den person som är förare, byta förare eller stoppa timern när ni behöver en paus eller när det är dags att gå hem.)

Att tänka på inför redovisning:

1. Se till att ni har koll på vad parprogrammering är och vad de olika rollerna innebär.
  * (Ha en logg redo att visa upp på [http://parkour.csc.kth.se](http://parkour.csc.kth.se/))

## Hederskodex
* Läs igenom hederskodexen.
* Skriv en kommentar [här](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/bekrafta-att-du-last-hederskodex/) där du bekräftar att du läst hederskodexen ((ska göras av varje kursdeltagare).

## Arbetsmiljön på Ubuntu-datorerna

* **Öppna ett terminalfönster**.
Under Applications hittar du Accessories och därunder Terminal. Prova att skriva whoami i terminalfönstret för att se vilken av er som är inloggad just nu.

* **Gör en gemensam labbkatalog där du och din labbkamrat kan jobba**.
Fysiskt skapas katalogen med [mkdir](http://en.wikipedia.org/wiki/Mkdir) hos en av er. Denne måste också sätta [accessrättigheter](http://en.wikipedia.org/wiki/Andrew_File_System) med
  [fs sa KATALOGNAMN LABBKAMRAT rlidwk](fs sa KATALOGNAMN LABBKAMRAT rlidwk )
Allt som återstår är att labbkamraten nu loggar in och skapar en symbolisk länk med
  [ln -s ~LABBKOMPIS/KATALOG](http://en.wikipedia.org/wiki/Symbolic_link#POSIX_and_Unix-like_operating_systems)
till den gemensamma katalogen.

Vid redovisning ska du kunna förklara hur en symbolisk länk fungerar.

* **Starta Python**.
Vi rekommenderar att du använder: _Emacs + Terminal_
Under _Applications_ hittar du _Accesories_ och därunder _GNU Emacs_ och _Terminal_. Skriv programmet i Emacs och kör det i Terminalen med kommandot: python3 programmet.py. Du kan också mjukstarta med IDLE (rekommenderas dock inte ihop med Tkinter). Under Applications hittar du Programming och därunder _IDLE (using Python-3.2)_

## Uppgifter
Spara filen [geodataSW.txt](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/labbar/geodataSW.txt) på er gemensamma katalog. Där finns geografiska data för platser i Sverige. Varje plats beskrivs av fem rader, följt av en tomrad. Överst i filen förklaras formatet.

1. Skriv en egen klass som representerar en plats. Klassen ska ha attribut för alla data i filen. Klassen ska ha minst fem metoder, bland dem metoden `__str__`
2. Skriv en funktion som läser in data från filen, skapar objekt, och lagrar objekten i en lista. (lista = []).
3. Skriv ett huvudprogram där man kan söka i listan.

Vid redovisning ska du kunna förklara hur klasser/objekt/listor/filhantering fungerar i Python.

## Betyg
**betyg E**: Du kan svara tillfredsställande på frågor om labben, ditt program löser uppgiften.

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se [tidsplanering för labbar](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/laborationer-88/)) + lägg in tidtagning i programmet  (se modulen [time](https://docs.python.org/3/library/time.html)).

**betyg A**: Kraven för C uppfyllda + lägg till en funktion som hittar den sydligaste platsen. Provkör även ditt program med [/misc/info/DD1320/www-csc/tilda14/labbar/geodataCH.txt](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/labbar/geodataCH.txt) och jämför körtiden.

## Redovisning
Labben lämnas in (se inlämning i vänstermenyn) och redovisas muntligt av bägge gruppmedlemmarna.
