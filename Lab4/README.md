# Laboration 4
## Laboration 4 - Från fan till gud
Det gäller att finna kortaste vägen från fan till gud genom att byta ut en bokstav i taget, till exempel så här:

```
fan -> man -> mun -> tun -> tur -> hur -> hud -> gud
```

Alla mellanliggande ord måste finnas i ordlistan [word3.txt](http://www.csc.kth.se/utbildning/kth/kurser/DD1320/tilda13/labbar/word3.txt) från förra laborationen.

Ditt program ska finna en kortare väg till gud än den här föreslagna. Lösningsprincipen gås igenom nedan och den beskrivs ofta i läroböcker för det analoga problemet att finna kortaste väg i en graf.

## Breddenförstsökning
Hur ska vi använda breddenförstsökning i det här problemet?

Problemträdets urmoder/stamfar **fan** har barnen **fin**, **man**, **far** med flera, barnbarnen **hin**, **mun**, **får** osv. Enligt kedjan ovan är **gud** barnbarnbarnbarnbarnbarnbarn till **fan**, men gud finns säkert redan tidigare i problemträdet. För att finna den första förekomsten gör man en breddenförstsökning enligt följande.
Lägg urmodern/stamfadern som första och enda post i en kö.
Gör sedan följande om och om igen:

* Plocka ut den första ur kön,
* skapa alla barn till den
* och lägg in dom sist i kön.

Första förekomsten av det sökta ordet ger kortaste lösningen.
Man kan spara in både tid och utrymme om man undviker att skapa barn som är kopior av tidigare släktingar (t ex **mans** barn **fan**), så kallade _dumbarn_. Uppgiften är så komplicerad att det är lämpligt att lösa den stegvis.

## 1. Första versionen
Låt filen fan.py utgå från förra labben, som ju har två binärträd. Nu kallar vi dom svenska (ordlistan) och gamla (dumbarnen). Huvudprogrammet ska läsa in ordlistan, fråga efter startord och slutord, och göra anropet makechildren(startord).
Denna funktion går systematiskt igenom alla sätt att byta ut en bokstav i startordet (aan, ban, ..., faö), kollar att det nya ordet finns i ordlistan men inte finns igamla och skriver i så fall ut det nya ordet på skärmen och lägger in det igamla.
Om du gjort rätt ska fan få sjutton barn.

## 2. Andra versionen
För fortsatt genomgång av fans barnbarn osv behövs den köklass som du använde i kortkonstlabben. Importera den och skapa kön q. I stället för att skriva ut barnen på skärmen lägger makechildren in dom i kön. Huvudprogrammet lägger in startordet i kön och går sedan i en slinga

```
while not q.isEmpty():
    nod = q.get()
    makechildren(nod)
```

När `makechildren()` stöter på slutordet gör den utskriften
```
    print("Det finns en väg till", slutord)
```

Provkör med lite olika start- och slutord, bland annat blå - röd, ful - gud och ute - hit.

## 3. Tredje versionen

Det tråkiga med programmet är att det bara talar om att det finns en lösning. För att programmet ska kunna skriva ut alla ord på vägen mellan fan och gud måste varje ord kunna peka på sin förälder. Det är alltså inte typen string man ska arbeta med utan en ParentNode som ser ut så här.

```
class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
```

Huvudprogrammet skapar ett sådant objekt och lägger in startordet. Det som sätts in i kön och plockas ut ur kön är nu inte längre ord utanParentNode, och det betyder att du måste ändra imakechildren.
När makechildren finner slutordet vill den skriva ut hela kedjan genom ett anrop writechain(child). Metoden writechain() ska skrivas rekursivt, så att man får ut kedjan med slutordet sist.

Om kön töms utan att någon lösning påträffats bör programmet meddela att det är omöjligt. Och när en lösning skrivits ut bör programmet avbryta körningen. Ett sätt att göra det är `sys.exit()` om man importerar modulen sys.

## Betyg
**betyg E**: Ditt program ska lösa uppgifterna ovan.
Vid redovisningen ska du också kunna

* rita upp problemträdet,
* förklara i detalj hur breddenförstsökningen fungerar,
* förklara varför breddenförstsökning ger den kortaste lösningen,
* visa hur utskriften av lösningen fungerar

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se [tidsplanering för labbar](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/laborationer-88/)).
Du ska också:

* implementera djupetförstsökning för samma problem
* kunna jämföra algoritmerna och förklara skillnaden i resultat

**betyg A**: Kraven för C uppfyllda + en av följande extrauppgifter:

* **Längst från gud**: Undersök vilket trebokstavsord som har längst väg till gud. Du måste då skriva en rekursiv countchain(child) som returnerar kedjans längd. Ledning: Om startord och slutord byter roller ändrar det inte kedjans längd.
* **Längst från varandra**: Vilka två ord är längst från varandra?

Denna labb ska du redovisa tillsammans med labb 2 och labb 3.
