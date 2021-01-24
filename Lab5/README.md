# Laboration 5
## Laboration 5 - Atomvikter

Ditt program ska bygga upp en hashtabell över alla grundämnens beteckningar och atomvikter så att det supersnabbt kan söka önskad information. Dialogen blir så här:

```
    Atombeteckning: Ag
    107.8682
    Atombeteckning: Au
    196.966569
    Atombeteckning: Q
    Okänd atom
    Atombeteckning:
```    
Du ska göra tre versioner av programmet:

```
1. Använd Pythons inbyggda datastruktur dictionary som hashtabell.
2. Implementera en egen hashtabell.
3. Lägg till ett grafiskt gränssnitt.
```

### 1. Hashning med Pythons inbyggda dictionary

Skriv en klass Hashtabell som använder dictionary. Den ska ha metodernaput ochget.

Programmet [hashtest.py](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/labbar/hashtest.py) innehåller data om alla atomer (namn och atomvikt). Lista ut vad det gör och hur det anropar hashtabellen. Modifiera det sedan för att kontrollera om din hashtabell fungerar.

Skriv sedan ett huvudprogramlabb5.py där man kan ge ett atomnamn och få ut atomvikten, enligt dialogexemplet ovan.

### 2. En egen implementation av hashtabellen
Nu ska du göra en ny version av klassen Hashtabell (spara den i en ny fil) där du använder en Python-lista för att implementera en egen hashtabell. Krav:

* Noderna måste innehålla både nyckel och värde
* Hashtabellen ska vara lagom stor
* Någon krockhantering måste ingå, t ex krocklistor eller probning
* AnvändKeyError för att tala om att en nyckel inte finns
* Skriv en egen hashfunktion
* Ska klara testning med hashtest.py ovan

Låt nu labb5.py använda din egen hashtabell!

### 3. Grafiken
För att få till grafiken i labb5.py importerar du klasserna Molgrafik och Ruta från filen [molgrafik.py](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/labbar/molgrafik.py).

Börja med att skapa ett Molgrafik-objekt;

```
  mg = Molgrafik()
```

Klassen Ruta har fyra attribut:
**atom** där du kan lägga in atomens namn
**num** där du kan lägga in atomens vikt
**next** och down som du kan strunta i för denna labb (dom används i labb 7).

Gör ett objekt **r** av Ruta och använd sedan metoden show så här:

```
  mg.show(r)
```

Om programmet avslutas direkt hinner man inte se grafiken blinka förbi. Lägg en slinga runt huvudprogrammet för inmatning av flera atomer.

PS Provkör gärna programmet i ett [Terminalfönster](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/labbar/terminal.html) för att undvika ev problem med IDLE.

## Betyg
**betyg E**: Ditt program ska lösa uppgifterna ovan.
Vid redovisningen ska du även kunna

* motivera ditt val av hashfunktion, krockhantering och tabellstorlek,
* skissa hashtabellen,
* förklara varför hashning ger snabb sökning

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se [tidsplanering för labbar](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/laborationer-88/)).
Du ska också:

* Provköra hashtabellen med större datamängder: I programmet [storfil.py](http://www.csc.kth.se/DD1320/tilda14/labbar/storfil.py) används en dictionary för att lagra en miljon artister och sånger.
Kopiera programmet, byt ut "songtable" mot din egen hashtabell och se till att det fungerar!
Om du kör hemma kan du ladda ner filen här: [unique_tracks.txt](http://www.csc.kth.se/~lk/unique_tracks.txt) (84MB)

**betyg A**: Kraven för C uppfyllda +

* Förbättra hashtest.py med fler testfall
* Skriv om hashtest.py med [unittest](http://docs.python.org/3.1/library/unittest.html)
