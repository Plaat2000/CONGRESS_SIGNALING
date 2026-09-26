# RenteKompas — leidende principes

Deze principes sturen onderzoek, ontwerp, implementatie en aanbevelingen. Afwijking vereist een expliciet besluit in `BESLUITEN.md` met motivatie, risicoanalyse en eigenaar.

## P1 — Veiligheid vóór rendement

Producten worden eerst getoetst aan harde veiligheids- en geschiktheidsregels. Pas daarna worden toegestane producten op netto-opbrengst gerangschikt.

## P2 — Geen onbegrensde garantieclaim

Het systeem zegt nooit alleen “gegarandeerd”. Het vermeldt steeds:

- de garant of contractpartij;
- de beschermde gebeurtenis;
- bedrag en valuta;
- juridische entiteit en vergunning;
- voorwaarden, uitsluitingen en looptijd;
- wat niet is beschermd, waaronder koopkrachtverlies.

## P3 — Nominaal is niet reëel

Nominale hoofdsom, nominale rente en koopkracht worden afzonderlijk gerapporteerd. Inflatie, belasting en kosten kunnen een positief nominaal resultaat reëel negatief maken.

## P4 — Liquiditeit is een harde randvoorwaarde

Een vastgestelde noodbuffer blijft vrij opneembaar. Het systeem zet nooit geld vast dat binnen de gekozen horizon nodig kan zijn.

## P5 — Officiële bron eerst

Juridische voorwaarden, rente, vergunning en garantie worden bevestigd met actuele primaire bronnen. Vergelijkingssites mogen alleen producten helpen ontdekken.

## P6 — Fail closed

Ontbrekende, tegenstrijdige, oude of niet-verifieerbare gegevens leiden tot uitsluiting of menselijke beoordeling, nooit tot een stilzwijgende aanname.

## P7 — Mens beslist over geldbewegingen

Onderzoek, vergelijking en monitoring mogen worden geautomatiseerd. Een storting, opname, productopening of wijziging van tegenrekening vereist standaard expliciete menselijke goedkeuring.

## P8 — Uitlegbaar en reproduceerbaar

Iedere selectie toont gebruikte bronnen, regels, aannames, berekening en uitsluitingsreden. Deterministische regels hebben de voorkeur boven machine learning.

## P9 — Minimale gegevens en minimale rechten

Het systeem verwerkt alleen noodzakelijke gegevens, bewaart geen bankgeheimen in Git en gebruikt waar mogelijk read-only toegang. Geheimen horen in een daarvoor bedoelde secret store.

## P10 — Scheiding van onderzoek en productie

Onderzoek, simulatie, testdata en productiegegevens blijven gescheiden. Een faseovergang vereist dat de acceptatiepoort in `ROADMAP.md` aantoonbaar is gehaald.

## P11 — Kosten en frictie tellen mee

Vergelijkingen gebruiken nettoresultaten en verwerken voor zover relevant kosten, belastingaannames, minimuminleg, looptijd en operationele inspanning.

## P12 — Geen prestatiebelofte

Historische of berekende opbrengst is geen toezegging over toekomstige rente. Onzekerheid en scenario's worden zichtbaar gemaakt.

## P13 — Beperkte scope

De standaard scope bestaat uit euro-spaarrekeningen en termijndeposito's bij verifieerbare instellingen. Nieuwe activaklassen vereisen een apart scopebesluit en mogen de veilige kern niet impliciet wijzigen.

## P14 — Audit en herstelbaarheid

Invoer, bronversie, beslisregels, uitvoertijd en uitkomst moeten herleidbaar zijn. Fouten moeten detecteerbaar en herstelbaar zijn zonder historische gegevens te overschrijven.
