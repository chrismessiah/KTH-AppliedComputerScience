# Laboration 6
## Nyhet: Betaversion av parprogrammeringsverktyget parkour är igång!
Prova [parkour](http://parkour.csc.kth.se/), och lämna feedback till handledare eller kursledaren.

## Laboration 6 - Formelkoll
I denna labb ska du

* Lära dig att använda domaren [Kattis](https://kth.kattis.scrool.se/), ett automatiskt system för rättning av labbar.
* Skriva ett program som läser in molekylformler och kontrollerar om dom är syntaktiskt korrekta. Närmare instruktioner finns i Kattis - problemet heter [formelkoll2](https://kth.kattis.com/problems/kth%3Atilda%3Aformelkoll2).

## Registrera dig på Kattis
Gör så här:

* Följ länken: [Kattis](https://kth.kattis.scrool.se/)
* Logga in (längst upp till höger) med ditt KTH-id
* Välj "COURSES" i övre  menyn
* Välj "tilda14" (långt ner i listan)
* Klicka på "I am a student taking this course and I want to register for it on Kattis."

## Lär dig använda Kattis
**Indata**
Programmen du skickar till Kattis ska läsa indata från stdin. Det fungerar som att läsa från fil! Exempel:

```
from sys import stdin

inrad = stdin.readline()
while inrad:
    lista = inrad.split()
    tal1 = int(lista[0])
    tal2 = int(lista[1])
    ...
    inrad = stdin.readline()
```

**Utdata**
Utdata kan du skriva ut med print som vanligt.

### Öva på två problem
Arbeta igenom följande enkla uppgifter

* [Tutorial 1](https://open.kattis.com/help/tutorial1) (Hello World)
* [Tutorial 2](https://open.kattis.com/help/tutorial2) (A Different Problem)

## Formelkoll
Läs instruktionerna för problemet [formelkoll2](https://kth.kattis.com/problems/kth%3Atilda%3Aformelkoll2).

Ditt program ska läsa formeln tecken för tecken och med rekursiv medåkning kolla syntaxen. Rekursiv medåkning innebär att huvudprogrammet först gör anropet readformel(), varefter readformel() anropar readmol() som anropar readgroup() och sedan eventuellt sej själv (men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck).

Funktionen readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol() etc - allt enligt grammatiken. När ett syntaxbrott upptäcks genereras en exception (raise Syntaxfel("Saknad högerparentes")) som fångas i huvudprogrammet och där skrivs hela resten av indataraden ut.

Man måste ofta tjuvtitta på nästa tecken för att veta vilken gren man ska följa i syntaxträdet. Inför metoden peek() i din köklass, så kan du titta på nästa tecken utan att plocka ut det ur kön.

Om du har flera programfiler måste du ange vilken som innehåller main (bortse från att det står "Java only" - detta gäller även Python!)

## Betyg
**betyg E**: Ditt program ska godkännas av Kattis (och förstås av handledaren vid redovisningen).
Du även kunna

* Beskriva hur rekursiv medåkning fungerar.
* Visa hur dina funktioner speglar den givna syntaxen.
* Förklara varför man inte måste räkna antalet parenteser.

**betyg C**: Kraven för E uppfyllda + Labben inlämnad och redovisad i tid (se [tidsplanering för labbar](https://www.kth.se/social/course/DD1320/subgroup/tilda14/page/laborationer-88/)) +
Du ska också:

* Skriva en spec med namnen på alla funktioner du planerar att skriva och en kommentar för varje funktion som beskriver vad funktionen ska göra.
Se [exempelspec](https://www.kth.se/social/upload/5137a8fff276545095c4f2a0/exempelspec.pdf) från programmeringsteknikkursen.

**betyg A**: Kraven för C uppfyllda +

* Skriv ett eget testprogram som kontrollerar de exempeldata som ges i [formelkoll2](https://kth.kattis.com/problems/kth%3Atilda%3Aformelkoll2).

_Den här labben ska redovisas tillsammans med labb 7._
