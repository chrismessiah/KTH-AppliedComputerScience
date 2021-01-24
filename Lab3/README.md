# Laboration 3
## Laboration 3 - Ordträd
Laborationens tema är binära sökträd.

**Första uppgiften** är att skriva en klass för binära sökträd och testa den.
**Andra uppgiften** är att bygga upp ett sökträd från en fil med svenska ord. Alla dubbletter ska skrivas ut.
**Tredje uppgiften** är att kolla orden i en engelsk text mot det svenska sökträdet. Finns det några skenbart svenska ord ska dom skrivas ut, men bara den _första_ förekomsten av varje svenskt ord. (För att veta vilka ord man redan hittat sparar man förstås dom i ett extra sökträd.)

## Skriv en klass för binära sökträd
Först måste du implementera ett binärt sökträd.

Tänk dig först ett abstrakt binärt sökträd. Eftersom man med Python kan jämföra ord (bokstavsordning) så går det bra att lagra ord i sökträdet, t ex så här:

```
   svenska = Bintree()         # Skapa ett trädobjekt
   svenska.put("gurka")		    # Sortera in "gurka" i trädet
   - - -
   if svenska.exists("gurka"): # Kolla om "gurka" finns i trädet
      - - -
   svenska.write()             # Skriver alla ord i bokstavsordning
```

KlassenBintree ska alltså ha tre metoder:

* `put(x)` som sorterar in x i trädet
* `exists(x)` som kollar om x finns i trädet
* `write()` som skriver ut trädet

Men i filen bintreeFile.py ska du dessutom definiera tre hjälpfunktioner. När trädobjektets put("gurka") anropas skickar trädet sin rotpekare och det nya ordet till en rekursiv funktion putta som ser till att en ny nod skapas på rätt ställe. Analogt gör de övriga anropen, alltså så här.

```
class Bintree:
    def __init__(self):
        self.root=None

    def put(self,newvalue):
        self.root=putta(self.root,newvalue)

    def exists(self,value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")
```

Här är klassen slut men sedan kommer definitionerna av funktionernaputta, finns ochskriv. Trädet ska bara lagra en upplaga av varje objekt som läggs in.

Det finns förstås också enclass Node i bintreefilen som innehåller ett värde och två pekare:left ochright.

## Andra uppgiften: Bygg träd och skriv ut dubbletter

Nu ska du läsa in ett ord i taget från filen [word3.txt](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/labbar/word3.txt) och lägga in det ditt binära sökträd. Ord som förekommer flera gånger (dubbletter) ska skrivas ut.

```
from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if svenska.exists(ordet):
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")
```

Om du gjort rätt kommer dom dubblettord som spottas ut att bilda ett viktigt budskap.

## Tredje uppgiften: Två binära sökträd med ordlistor

När du nu har ett sökträd med alla svenska trebokstavsord kan du blixtsnabbt kolla om ett givet ord finns med. Du ska nu läsa filen [engelska](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/labbar/engelska.txt) ord för ord och putta in orden i ett annat sökträd. Nu vill du inte ha dubbletterna utskrivna, så kolla först if engelska.exists(...). Om ordet redan fanns gör du ingenting, men om det är nytt ska du också kolla om det råkar finnas som svenskt ord. I så fall ska det skrivas ut på skärmen.

Om du har gjort rätt kommer dom utskrivna orden att bilda ännu ett hemligt budskap!

## Redovisning
När allt fungerar som det ska bör du ta en extra titt på koden. Är den kommenterad och begriplig?

_Kontrollera att du gjort alla uppgifterna ovan. Den här labben ska redovisas tillsammans med labb 2 och 4._

## Betyg
**betyg E**: Ditt program ska lösa uppgifterna ovan.
Vid redovisningen ska du också

* kunna rita och berätta hur binärträdet byggs upp,
* förklara varför det går snabbt att söka i ett binärträd,
* förklara idén bakom att ha put som anropar putta, exists som anropar finns och write som anropar skriv

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se [tidsplanering för labbar](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/laborationer-88/)).
Du ska också:

* Kunna redogöra för vilka olika fall man bör testa för att försäkra sig om att klassens metoder fungerar.
* Testa sökningen praktiskt. Jämför tidsåtgången vid sökning i trädet med linjärsökning i en lista. Använd t ex [time.time()](http://docs.python.org/3.2/library/time.html).

**betyg A**: Kraven för C uppfyllda + en av följande extrauppgifter:

* **Söt tös**: Undersök vilka trebokstavsord som blir andra ord baklänges. Varje ordpar ska bara skrivas ut en gång och symmetriska ord inte alls.
* **Alpin pinal**: Undersök vilka fembokstavsord som blir ett annat ord när dom två första bokstäverna flyttas sist. Du kan använda ordlistan [word5.txt](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/labbar/word5.txt).
