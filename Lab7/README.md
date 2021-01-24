# Laboration 7
## Laboration 7 - Molekylgrafik

Det här programmet ska fullborda det som den föregående labben har påbörjat. Det gör formelkoll som tidigare och ritar sedan upp molekylen. På skärmen kan det se ut så här:

```
   Molekyl: Si(C3(COOH)2)4(H2O)7
   Molekyl:
```

och i molekylfönstret ritar programmet ut formelstrukturen:

![Molecular image](http://www.csc.kth.se/utbildning/kth/kurser/2D1320/gemensam/bilder/molbild.gif)

## Förberedelse: Rita syntaxträd
Plocka fram syntaxen i labb 6, och rita med hjälp av den upp syntaxträd för följande molekyler:

```
O
CO2
(CH3)2(CH2)4
```

## Låt ditt program bygga ett molekylträd
Du ska komplettera formelkollsprogrammet till att samtidigt bygga ett träd som ser ut som ovan. Varje ruta motsvaras av ett objekt:

```
class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None
```

Funktionen readgroup skapar först en sådan tomruta med

```
   rutan = Ruta()
```

och anropar readatom och readnum för att kunna sätta in rätt värden på atom och num. Om det är en parentesgrupp ska readgroups anrop till readmol returnera en delmolekyl som sätts under rutan.down.

När readgroup är klar returnerar den rutan till anropet

```
    mol = readgroup()
```

som görs allra först i readmol. Vad som ska göras med mol.next får du själv tänka ut. Slutligen returnerar readmol den färdiga strukturen till readformel som returnerar den till huvudprogrammets anrop

```
    mol = readformel()
```

där mol pekar högst upp till vänster på syntaxträdet.

## Rita molekylträdet
Huvudprogrammet ska nu rita upp den färdiga molekylen. Använd molgrafik.py från labb 5. Skapa ett objekt av den klassen:

```
   mg = molgrafik()
```

Sedan ska

```
   mg.show(mol)
```

rita upp molekylbilden i ett eget fönster. Bilden ritas förstås rekursivt, och du ska formulera den rekursiva tanke som används. Om du inte kommer på den själv kanske det hjälper att kolla molgrafikkoden. Om programmet avslutas direkt hinner man inte se grafiken blinka förbi. Se därför till att ha en slinga för inmatning av flera formler.

## Molekylvikten
**Molekylvikten** ska beräknas rekursivt med anropet weight(mol). Formulera först en mycket rekursiv tanke för vikten och programmera den sedan! Låt programmet skriva ut vikten av molekylen i terminalfönstret.

**betyg E**: Du ska ha löst uppgifterna ovan, och kunna

* Rita hur trädet byggs upp av funktionsanropen.
* Visa med ett exempel hur funktionen weight() beräknar molekylvikten.
* Förklara hur ditt anrop till molgrafikens show() fungerar (men du behöver inte kunna förklara hur Tkinter fungerar).

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se [tidsplanering för labbar](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/laborationer-88/)).

**betyg A**: Kraven för C uppfyllda +

* Modifiera molgrafiken så att vikten skrivs ut i samma fönster.
