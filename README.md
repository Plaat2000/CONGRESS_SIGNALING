# RenteKompas

**Veilige rentevergelijking en depositoplanning**

> **Actief project:** dit repositoryniveau is de projectruimte voor
> **RenteKompas**. Het voormalige Congress Signaling-project is
> afgesloten en alleen ter historische referentie opgeslagen onder
> [`archive/congress-signaling/`](archive/congress-signaling/).

## Doel

Deze projectruimte onderzoekt hoe een gebruiker met weinig beheer en een beperkte inleg de **nominale renteopbrengst** op spaargeld kan optimaliseren, met behoud van vooraf vastgelegde grenzen voor veiligheid en liquiditeit.

RenteKompas is in de eerste fase een read-only **spaar- en deposito-optimizer**. Het verzamelt openbare informatie, verifieert product- en garantiestelselvoorwaarden, past uitsluitingsregels toe en stelt een depositoladder voor. De gebruiker controleert de officiële voorwaarden en voert iedere geldbeweging zelf uit.

Dit project belooft geen risicoloos of gegarandeerd reëel rendement. Een vaste rente kan contractueel zijn vastgelegd en een erkend depositogarantiestelsel kan onder voorwaarden bescherming bieden, maar inflatie, belasting, liquiditeit, fraude, operationele fouten en wijzigingen na afloop blijven risico's.

## Status en scope

**Status:** onderzoeks- en ontwerpfase; geen productiegebruik en geen automatische geldbewegingen.

- **Canonieke projectnaam:** `RenteKompas`
- **Beoogde repositoryslug:** `rentekompas`

**Binnen scope:**

- euro-spaarrekeningen en termijndeposito's;
- officiële bank-, vergunning- en garantiestelselgegevens;
- uitlegbare vergelijking, risicofilters en laddervoorstellen;
- read-only monitoring, meldingen en auditinformatie;
- handmatige, expliciet bevestigde uitvoering.

**Buiten scope:**

- Congress-signalen of transacties van politici;
- aandelen, ETF's, obligatiehandel, crypto en derivaten;
- leverage, arbitrage, copy trading en koersvoorspelling;
- autonoom openen van producten of verplaatsen van geld;
- persoonlijk financieel of fiscaal advies.

## Documenten

| Document | Functie |
|---|---|
| [`PRINCIPES.md`](PRINCIPES.md) | Niet-onderhandelbare leidende principes en risicogrenzen |
| [`ADVIES_EN_ONTWERP.md`](ADVIES_EN_ONTWERP.md) | Vastgelegd advies, oplossingsontwerp en informatiestromen |
| [`STANDAARD_TAKEN.md`](STANDAARD_TAKEN.md) | Terugkerende werk- en kwaliteitschecklists |
| [`BESLUITEN.md`](BESLUITEN.md) | Besluitlog met redenen, alternatieven en gevolgen |
| [`BRONNEN.md`](BRONNEN.md) | Bronregister en eisen voor actualiteit en herleidbaarheid |
| [`RISICOS.md`](RISICOS.md) | Initiële risicoanalyse en beheersmaatregelen |
| [`BUSINESSCASE_EN_HAALBAARHEID.md`](BUSINESSCASE_EN_HAALBAARHEID.md) | Realisatie­risico's, kritieke taken, kennis, planning en financiële scenario's |
| [`ROADMAP.md`](ROADMAP.md) | Gefaseerd onderzoeksplan en acceptatiepoorten |
| [`LOGBOEK.md`](LOGBOEK.md) | Chronologisch werk-, test- en incidentlog |
| [`AGENTS.md`](AGENTS.md) | Verplichte instructies voor toekomstige agents en automatisering |
| [`ARCHIEFBELEID.md`](ARCHIEFBELEID.md) | Formele afsluiting en isolatie van het voormalige Congress Signaling-project |

## Gebruik in toekomstige interacties

Iedere nieuwe werksessie in deze map begint met het lezen van `AGENTS.md`, `PRINCIPES.md`, `BESLUITEN.md` en `ROADMAP.md`. Besluiten worden niet alleen in chat gemaakt: een materieel besluit wordt in dezelfde wijziging duurzaam vastgelegd in `BESLUITEN.md`.

De documenten in Git zijn de blijvende bron van waarheid. Chatcontext kan verdwijnen of onvolledig zijn en geldt daarom niet als duurzaam geheugen.

## Projectgrens en archief

Alle actieve projectdocumentatie en toekomstige broncode staan vanaf de root
van deze repository. Nieuwe werkzaamheden worden niet aan het voormalige
Congress Signaling-project toegevoegd. Het archief is geen dependency, geen
databron en geen basis voor de nieuwe oplossing. Zie
[`ARCHIEFBELEID.md`](ARCHIEFBELEID.md) voor de afsluiting en heropeningsregels.

De lokale werkruimtemap kan door de uitvoeromgeving nog een historische naam
hebben. Die infrastructuurnaam definieert het project niet. Zodra een Git-remote
of externe projectomgeving wordt aangemaakt, moet deze de slug `rentekompas`
gebruiken.

## Eerstvolgende stap

Voer fase 1 van `ROADMAP.md` uit: definieer gebruikersprofiel, jurisdictie, liquiditeitsbehoefte, toegestane garantiestelsels en meetbare acceptatiecriteria. Er wordt nog geen scraper of transactiekoppeling gebouwd.
