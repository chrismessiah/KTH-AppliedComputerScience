# Laboration 2
## Laboration 2 - Kortkonst

```
"Trollkarlen tar ut de tretton spaderna ur leken, håller dem som en
kortlek med baksidan upp och lägger ut dem på följande sätt: Översta
kortet stoppas underst, nästa kort läggs ut med framsidan upp, nästa
kort stoppas underst, nästa kort läggs ut osv.  Till publikens
häpnad kommer korten upp i ordning ess, tvåa, trea...
Utförande: Man ordnar i hemlighet korten enligt följande."
```

Ja, här bryter vi citatet ur Liberg: Trolleri för alla.
I labbuppgiften ingår nämligen att ta reda på kortkonstens hemlighet! Du ska därför göra ett program där man kan simulera korttricket så här:

```
  Vilken ordning ligger korten i? 3   1   4   2   5
  De kommer ut i denna ordning: 1 2 3 5 4
```

## Uppgifter

### 1. ListQ - en kö med Pythons lista
Med den abstrakta datastrukturen kö kan man göra tre saker: stoppa in något sist, plocka ut det som står först och kolla om kön är tom. Det motsvarar anropen

* `put(x)`
* `x = get()`
* `isEmpty()`

Skriv en egen klass ListQ där du implementerar en kö med hjälp av pythons inbyggda lista. Till din hjälp har du Pythons listmetoder

### 2. Testa ListQ

Prova din kö med följande testprogram:

```
   q = ListQ()
   q.put(1)
   q.put(2)
   x = q.get()
   y = q.get()
   print(x,y)   # 1 2 ska komma ut
```
### 3. Skriv Trollkarlsprogrammet

Skriv ett program som simulerar korttricket (se exemplet överst i labben).
Inmatningstips är att användainput() för att läsa in hela raden och sensplit() för att dela upp den. Experimentera sedan med olika inmatade ordningar och lista ut i vilken ordning korten ska ligga innan man börjar trolla för att man ska få ut alla tretton i rätt ordning!

Programmet konverserar också intelligent. Mata till exempel in meningen

```
                            JAG GILLAR NÄR DU KRAMAR MEJ.
```

### 4. Skapa en ListQ-modul
Gör nu så här: klipp ut klassen från ditt program och klistra in i en ny fil listQFile.py
Importera klassen till huvudprogrammet med raden
```
from listQFile import ListQ
```
Nu går det att använda klassen utan att den syns i programmet.

### 5. LinkedQ - en kö av noder (länkad lista)
Nu ska du istället implementera kön som en länkad lista. Då behövs två klasser:Node ochLinkedQ, som kan ligga i samma fil. Noderna i listan är objekt som vardera innehåller två attribut: ett värde (value) och en referens till nästa objekt (next).
Själva LinkedQ-klassen har två attribut: _first_ som håller reda på den första noden i kön och _last_ som pekar ut den sista. [Här](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/labbar/LinkedQskelett.html) är en del av koden - resten får du fylla i själv. Använd samma gränssnitt som i uppgift 1:

* `put(x)`
* `x = get()`
* `isEmpty()`

Som inspiration kan du titta på [stack.py](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/ovn/1ovn.html) från Övning 1.

Det är extra knepigt att programmera put(x) eftersom det blir två fall, beroende på om kön är tom eller inte. Rita upp bägge fallen (lådor med pilar) innan du skriver koden!

### 6. Trollkarlsprogrammet med LinkedQ
Ändra import-satsen i trollkarlsprogrammet så att du importerar klassenLinkedQ istället förListQ. Provkör. Fungerade det? Då har du lyckats implementera den abstrakta datastrukturen kö på två olika sätt.
Testa också att rita en [blomma](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda14/labbar/blomma.py).

## Redivisning

När allt fungerar som det ska bör du ta en extra titt på koden. Är den kommenterad och begriplig? Hur har du testat programmet för att se att det fungerar
Den här labben ska redovisas tillsammans med labb 3 och 4.

## Betyg
**betyg E**: Ditt program löser uppgifterna ovan, du kan rita och förklara hur metoderna fungerar.

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se tidsplanering för labbar) + Göra labb 1 med din LinkedQ istället för listan.

**betyg A**: Kraven för C uppfyllda + en av följande extrauppgifter:

* _Bakfram kortkonst_:
Det är tidskrävande att experimentera sej fram till rätt utgångsordning på korten. En genial metod är förstås att göra kortkonsten baklänges, och det ska du programmera. Tricket här är att använda en stack som hjälp för att kunna vända på kortens ordning.
* _Misslyckad blandning_:
Korthajarnas riffelblandning går till så att leken delas på mitten och de båda halvlekarna rifflas ihop så att undre halvlekens översta kort hamnar överst och övre halvlekens understa kort hamnar underst. Ryktet säger att den här blandningen inte får göras för många gånger, för då är korten tillbaka i ursprunglig ordning. Kan det stämma?
För att programmera det här behöver du tre köer. Ditt program ska fråga efter antal kort (ett jämnt tal) och antal blandningar och skriva ut hur ordningen blir efteråt. Testa med 6 kort och tre blandningar eller 62 kort och sex blandningar. Hur många behövs för vår vanliga kortlek med 52 kort?
