# RenteKompas — initiële risicoanalyse

| Risico | Initiële impact | Beheersmaatregel |
|---|---:|---|
| Bankmerken worden ten onrechte als afzonderlijke banken gezien | Hoog | Aggregeer altijd op juridische entiteit en vergunning |
| Garantievoorwaarden zijn verkeerd of verouderd | Hoog | Officiële bron, geldigheidscontrole, tweede controle en fail closed |
| Rente is gewijzigd sinds verzameling | Middel | Geldigheidsinterval, maximale bronleeftijd en controle vóór uitvoering |
| Geld is nodig vóór einde looptijd | Hoog | Harde noodbuffer en maximale looptijd; scenarioanalyse |
| Inflatie overstijgt nominale rente | Middel | Rapporteer nominale en reële scenario's afzonderlijk |
| Kosten of belasting maken nettoresultaat lager | Middel | Nettovergelijking en expliciete fiscale aannames |
| Vreemde-valutaverlies | Hoog | Alleen EUR in initiële scope |
| Foutieve scraping of parsing | Hoog | Schema-validatie, bronhash, regressietests en menselijke controle |
| Kwaadaardige bronwijziging of supply-chainaanval | Hoog | Domeinallowlist, TLS, dependencybeheer en onafhankelijke controles |
| Ongeautoriseerde geldbeweging | Kritiek | Geen betaalfunctionaliteit; handmatige uitvoering en goedkeuring |
| Gevoelige gegevens lekken via Git of logs | Hoog | Dataminimalisatie, secret scanning en redactiebeleid |
| Stilzwijgende automatische verlenging | Middel | Vooraf melden en herbeoordeling vóór afloop |
| Systeem wordt als persoonlijk advies geïnterpreteerd | Middel | Scope, aannames, onzekerheid en menselijke verantwoordelijkheid tonen |
| Operationele afhankelijkheid van één bron | Middel | Bronstatus bewaken, alternatieve officiële bron en geen stil fallbackgedrag |

Risicoscores, eigenaren en concrete drempelwaarden worden in fase 1 vastgesteld. Tot die tijd geldt de meest conservatieve interpretatie.

## Risico's voor realisatie van het plan

Onderstaande risico's gaan niet alleen over financiële schade, maar over de kans dat het project geen betrouwbaar of economisch zinvol resultaat oplevert.

| Prioriteit | Realisatierisico | Kans | Impact | Vroeg signaal | Stop- of beheersmaatregel |
|---|---|---:|---:|---|---|
| 1 | Officiële productvoorwaarden zijn niet stabiel, volledig of machineleesbaar beschikbaar | Hoog | Hoog | Veel handmatige PDF's, anti-botmaatregelen of frequente paginawijzigingen | Begin met een klein handmatig bronbestand; automatiseer alleen stabiele bronnen; stop brede dekking als onderhoud structureel te groot wordt |
| 2 | De extra renteopbrengst is kleiner dan ontwikkel-, beheer- en overstapkosten | Hoog | Hoog | Renteverschil na kosten is minder dan circa 0,5 procentpunt | Gebruik de scenarioformule uit `BUSINESSCASE_EN_HAALBAARHEID.md`; bouw alleen verder bij een positieve persoonlijke of commerciële businesscase |
| 3 | Merk, bankvergunning en garantiestelsel worden verkeerd geaggregeerd | Middel | Kritiek | Eén vergunning is niet eenduidig aan alle merken te koppelen | Geen aanbeveling zonder juridisch-entiteitsrecord en officiële registercontrole |
| 4 | Het product wordt feitelijk persoonlijk advies of bemiddeling en valt onder vergunning- of gedragsregels | Middel | Hoog | Persoonlijke rangschikking, affiliatevergoeding, aanvraagknop of overdracht van klantgegevens | Laat vóór publieke/commerciële lancering een Nederlandse financieel-juridische scopeanalyse uitvoeren; houd de eerste versie privé en read-only |
| 5 | Scope groeit naar open banking of automatische uitvoering | Middel | Kritiek | Verzoek om bankcredentials, rekeningdata of betaalinitiatie | Apart go/no-go-besluit, juridische toets en beveiligingsarchitectuur; niet toevoegen aan de MVP |
| 6 | Gebruikers vertrouwen te sterk op schijnzekerheid | Middel | Hoog | Alleen het hoogste rentepercentage wordt gevolgd of waarschuwingen worden genegeerd | Toon beperkingen, bronouderdom, liquiditeit en uitsluitingen even prominent als opbrengst; menselijke bevestiging verplicht |
| 7 | Onderhoud en bronverificatie vragen meer aandacht dan beoogd | Hoog | Middel | Meer dan twee uur handwerk per maand voor een kleine productset | Beperk landen en banken; meet onderhoudstijd; beëindig automatisering die geen netto tijdwinst oplevert |
| 8 | Persoonsgegevens of financiële profielen creëren privacy- en beveiligingsverplichtingen | Middel | Hoog | Centrale opslag van saldo, fiscale woonplaats of rekeninggegevens | Lokale configuratie, dataminimalisatie, geen productiegegevens in Git; privacytoets vóór opslag of SaaS |
| 9 | Fiscaliteit of grensoverschrijdende voorwaarden maken nettovergelijkingen onjuist | Middel | Hoog | Buitenlandse bronheffing, afwijkende aangifte of verschillende producttoegang | Start met één jurisdictie en EUR; laat fiscale aannames expliciet bevestigen; geen individueel belastingadvies |
| 10 | Sleutelkennis of motivatie ontbreekt | Middel | Middel | Open bronconflicten en roadmaptaken blijven meerdere cycli liggen | Klein proof of concept, duidelijke eigenaar per risico en maandelijkse go/no-go-review |

De top drie blokkers zijn daarmee **datakwaliteit**, **een te kleine economische marge** en **onjuiste juridische-entiteits- of garantiestelselclassificatie**. Zonder oplossing voor alle drie heeft implementatie geen verantwoord vervolg.
