# RenteKompas — businesscase en haalbaarheid

## 1. Managementsamenvatting

De oplossing is technisch haalbaar als kleine, read-only toepassing. De belangrijkste vraag is niet of een vergelijker kan worden gebouwd, maar of de **extra netto rente** opweegt tegen ontwikkeling, periodieke broncontrole, overstapfrictie en eventuele compliancekosten.

Voor persoonlijk gebruik is de businesscase alleen aantrekkelijk wanneer:

- de gebruiker al voldoende vrij spaargeld heeft;
- het systeem aantoonbaar een relevant renteverschil vindt;
- ontwikkeling grotendeels als leerproject of tegen zeer lage kosten plaatsvindt;
- het onderhoud beperkt blijft;
- er geen vergunningplichtige of betaalinitiatiedienst wordt toegevoegd.

Voor een commerciële dienst is de businesscase nog **niet bewezen**. Personalisatie, bemiddeling, affiliatevergoedingen, klantgegevens en betaal- of rekeninginformatiediensten kunnen de juridische en operationele last sterk verhogen. Een publieke lancering mag daarom pas na een formele scopeanalyse door een Nederlandse specialist in financieel toezicht, privacy en consumentenrecht.

## 2. Grootste bedreigingen voor realisatie

### 2.1 Economische marge is waarschijnlijk klein

De jaarlijkse meerwaarde is bij benadering:

```text
incrementele bruto-opbrengst
= inzetbaar saldo × (gevonden rente − realistische referentierente)

incrementele netto-opbrengst
= incrementele bruto-opbrengst
− productkosten
− fiscale effecten
− gewaardeerde gebruikers- en beheertijd
− ontwikkel- en exploitatiekosten
```

Een hoge aangeboden rente is niet volledig incrementeel: zonder dit systeem zou het geld doorgaans ook rente ontvangen. De businesscase moet daarom het **renteverschil** gebruiken en niet de totale rente.

### 2.2 Betrouwbare brondata is arbeidsintensief

Rente is relatief eenvoudig; vergunningstructuur, merkrelaties, garantiestelsel, uitzonderingen, vervroegde opname en producttoegang zijn dat niet. PDF's en webpagina's kunnen zonder aankondiging wijzigen. Volledig automatische dekking van veel banken of landen botst daardoor met het principe “officiële bron eerst”.

### 2.3 Juridische classificatie kan het model veranderen

Een privétool die openbare feiten toont en geen geld verplaatst heeft een ander profiel dan een dienst die een individuele consument een specifiek product aanbeveelt, een aanvraag faciliteert, klantgegevens doorstuurt of daarvoor wordt betaald. De grens moet vóór commercialisering schriftelijk worden beoordeeld. De applicatie mag niet zelf aannemen dat termen als “vergelijker”, “informatie” of “read-only” een vrijstelling opleveren.

### 2.4 Vertrouwen en aansprakelijkheid

Eén fout in de koppeling tussen merk en bankvergunning kan zwaarder wegen dan jaren rentevoordeel. De kernprestatie is daarom niet “de hoogste rente vinden”, maar “aantoonbaar geen aanbeveling doen bij onzekere kritieke gegevens”. Dit verlaagt de dekking, maar is noodzakelijk voor vertrouwen.

## 3. Kritieke taken en externe eisen

| Kritieke taak | Waarom kritisch | Regeldruk bij privé/read-only | Mogelijke strengere eisen bij publieke/commerciële dienst | Vereiste uitkomst |
|---|---|---|---|---|
| Scope en gebruikersrol afbakenen | Bepaalt welke regels en aansprakelijkheid relevant zijn | Laag, zolang uitsluitend eigen gebruik en geen uitvoering | Mogelijk financieel toezicht, consumentenrecht en reclame-eisen | Schriftelijke scope en verboden functies |
| Juridische entiteiten en vergunningen koppelen | Nodig om blootstelling en garantie correct te aggregeren | Officiële registers en voorwaarden moeten worden gevolgd | Claims moeten aantoonbaar, actueel en niet-misleidend zijn | Gevalideerd entiteitenregister met bronbewijs |
| Garantiestelselvoorwaarden modelleren | “€100.000” is geen losstaand productkenmerk; voorwaarden en aggregatie tellen | Hoge inhoudelijke nauwkeurigheid vereist | Extra zorgplicht, klachten- en bewijsrisico | Regelset met limiet, valuta, rechthebbende en uitzonderingen |
| Productvoorwaarden en rente actualiseren | Verouderde data kan een verkeerd voorstel veroorzaken | Geen formele realtime-eis vastgesteld, wel eigen veiligheidsnorm | Mogelijke eisen aan juistheid, actualiteit, transparantie en commerciële communicatie | Bronleeftijd, geldigheid en blokkering bij conflict |
| Persoonlijke rangschikking ontwerpen | Kan van algemene informatie richting individueel advies bewegen | Beperk tot eigen, lokale configuratie | Juridische toets op adviseren/bemiddelen en eventuele vergunningplicht | Go/no-go-memo vóór externe gebruikers |
| Privacy en informatiebeveiliging | Saldo, woonplaats en voorkeuren kunnen gevoelig zijn | Lokale minimale opslag blijft nodig | AVG-verplichtingen, verwerkers, rechten, beveiliging en datalekproces | Gegevensinventarisatie en privacy-/dreigingsanalyse |
| Rekeninginformatie of betalingen koppelen | Vergroot fraude- en operationeel risico sterk | Buiten scope | PSD2/betaaldienstenkader, sterke authenticatie en mogelijk vergunning/registratie | Niet bouwen zonder afzonderlijk juridisch en technisch programma |
| Netto-opbrengst valideren | Voorkomt dat bruto rente als businesswaarde wordt verkocht | Transparante aannames | Reclame- en consumentenclaims moeten controleerbaar zijn | Onafhankelijke narekening en scenarioanalyse |

### Voorlopige conclusie over overheids- en bankeisen

1. **De read-only privé-MVP** heeft naar verwachting vooral te maken met correcte broninterpretatie, privacy en gebruiksvoorwaarden van websites; hij opent geen rekening, bemiddelt niet voor derden en initieert geen betaling.
2. **Een publieke gepersonaliseerde vergelijker** vereist vóór lancering een specialistische toets op de Wet op het financieel toezicht, AFM-regels, consumentenrecht, reclameclaims en AVG. Of een vergunning of vrijstelling van toepassing is hangt af van de precieze klantreis, vergoeding en productclassificatie; dit document doet daar geen definitieve uitspraak over.
3. **Open banking of automatische betaling** is een afzonderlijke zwaarteklasse. Rekeninginformatiediensten of betaalinitiatiediensten mogen niet worden toegevoegd op basis van alleen de huidige architectuur.
4. **Bankvoorwaarden** kunnen scraping, hergebruik, producttoegang, minimale inleg, tegenrekening en klantacceptatie beperken. Technische vindbaarheid betekent niet dat geautomatiseerd hergebruik of toegang tot het product is toegestaan.

## 4. Benodigde kennis

| Kennisgebied | Minimumniveau voor MVP | Wanneer specialist nodig is |
|---|---|---|
| Depositoproducten en renteconventies | Goed begrip van enkelvoudige/samengestelde rente, looptijd, vervaldag en opnamevoorwaarden | Complexe of grensoverschrijdende producten |
| Depositogarantiestelsels | Kunnen lezen van officiële dekking, vergunning en aggregatieregels | Interpretatie van uitzonderingen of commerciële claims |
| Nederlands/EU financieel toezicht | Basiskennis om verboden scope te herkennen | Vóór ieder aanbod aan derden, vergoeding, aanbeveling of aanvraagfacilitatie |
| Privacy en beveiliging | Dataminimalisatie, lokale opslag, secrets, toegangsbeheer en logging | SaaS, klantaccounts, financiële persoonsgegevens of koppelingen |
| Data engineering | HTTP/PDF-inname, schema's, provenance, hashes, validatie en idempotentie | Veel bronnen, hoge beschikbaarheid of juridisch bewijsarchief |
| Softwarekwaliteit | Unit-, integratie- en regressietests; foutafhandeling; back-up/herstel | Productiegebruik of externe gebruikers |
| Financiële modellering | Netto-opbrengst, scenario's, liquiditeit en gevoeligheidsanalyse | Fiscale personalisatie of productvergelijking over landen |
| Product/UX | Waarschuwingen, onzekerheid en uitsluitingsredenen begrijpelijk tonen | Consumentenproduct en toegankelijkheids-/gedragsonderzoek |
| Operations | Bronmonitoring, incidenten, wijzigingen en periodieke review | Service-levelafspraken of betaalde dienst |

Machine learning is niet nodig. De moeilijkste kennis zit in broninterpretatie, juridische afbakening, dataprovenance en foutveilige productlogica.

## 5. Indicatieve tijdlijn

De raming veronderstelt één technisch vaardige maker, parttime 8–12 uur per week, een Nederlandse gebruiker, alleen EUR, maximaal 5–10 banken en geen bankkoppelingen.

| Fase | Doorlooptijd | Inspanning | Resultaat | Beslismoment |
|---|---:|---:|---|---|
| 1. Vereisten en bron-/juridische verkenning | 2–4 weken | 20–40 uur | Scope, gebruikersregels, bronnen, entiteiten en juridische vragen | Stop als garantie of producttoegang niet betrouwbaar te modelleren is |
| 2. Handmatig proof of concept | 2–3 weken | 20–35 uur | Gevalideerde dataset, berekening en voorbeeldladder | Stop als extra rente de beheerlast niet plausibel dekt |
| 3. Read-only MVP | 4–8 weken | 60–120 uur | Collectors, validator, planner, rapport en auditlog | Alleen pilot als foutscenario's fail closed werken |
| 4. Privépilot | 8–12 weken kalenderduur | 15–30 uur beheer/evaluatie | Werkelijke onderhoudstijd, datakwaliteit en voorstellen gemeten | Go/no-go op feitelijke netto waarde |
| 5. Eventuele publieke dienst | minimaal 3–6 maanden extra | sterk variabel | Juridische toets, privacy, security, operatie en klantproces | Afzonderlijke investeringsbeslissing |

Een bruikbare privé-MVP vraagt daarmee naar schatting **2–4 maanden**. Een betrouwbare publieke dienst is geen logische directe vervolgstap en vraagt waarschijnlijk **6–12 maanden totaal**, exclusief vertraging door juridische beoordeling, bankvoorwaarden of toegang tot bronnen.

## 6. Financiële scenario's

Deze bedragen zijn **rekenvoorbeelden, geen actuele marktrentes of voorspellingen**. Alle percentages zijn bruto per jaar. Belastingen, inflatie, productkosten en tijdswaarde zijn niet inbegrepen tenzij genoemd.

### Totale nominale rente

| Inzetbaar saldo | 2,0% | 2,5% | 3,0% |
|---:|---:|---:|---:|
| €5.000 | €100 | €125 | €150 |
| €10.000 | €200 | €250 | €300 |
| €25.000 | €500 | €625 | €750 |
| €50.000 | €1.000 | €1.250 | €1.500 |
| €100.000 | €2.000 | €2.500 | €3.000 |

### Waarde van optimalisatie boven een bestaande rekening

| Saldo | +0,25 procentpunt | +0,50 procentpunt | +1,00 procentpunt |
|---:|---:|---:|---:|
| €5.000 | €12,50 | €25 | €50 |
| €10.000 | €25 | €50 | €100 |
| €25.000 | €62,50 | €125 | €250 |
| €50.000 | €125 | €250 | €500 |
| €100.000 | €250 | €500 | €1.000 |

De tweede tabel is bepalend voor de businesscase. Bij €10.000 saldo en 0,50 procentpunt verbetering is de incrementele bruto-opbrengst slechts €50 per jaar. Zelfs een goedkope softwareontwikkeling verdient zich dan financieel niet terug. Bij €100.000 en 1,00 procentpunt is dat €1.000 per jaar, maar spreiding, interne veiligheidsmarge en persoonlijke belasting kunnen de benutbare waarde verlagen.

### Indicatieve kosten

| Kostencategorie | Privé/zelfbouw | Publieke dienst |
|---|---:|---:|
| Hosting en monitoring | circa €0–€300 per jaar | circa €1.000–€10.000+ per jaar |
| Ontwikkeling | 100–225 uur eigen tijd tot en met pilot | meerdere disciplines en doorlopend onderhoud |
| Brononderhoud | aanvankelijk 1–4 uur per maand | afhankelijk van dekking mogelijk structurele operatie |
| Juridische/privacyreview | optioneel voor strikt privégebruik | waarschijnlijk noodzakelijk; vooraf offerte aanvragen |
| Security en incidentproces | basismaatregelen | professionele toetsing en permanente operatie |

Kosten zijn orde-grootteramingen en geen offertes. De waarde van eigen tijd moet expliciet worden gekozen. Bij €25 per uur vertegenwoordigt 100–225 uur bijvoorbeeld €2.500–€5.625 aan opportuniteitskosten.

## 7. Businessmodellen

### A. Persoonlijk hulpmiddel — voorlopig meest logisch

- **Waarde:** hogere rente, minder zoektijd, betere spreiding en minder gemiste afloopdata.
- **Inkomsten:** geen; voordeel bestaat uit incrementele rente en tijdwinst.
- **Kosten:** eigen ontwikkeling, beperkt onderhoud en eventueel hosting.
- **Go/no-go:** doorgaan als leerwaarde plus driejarige netto financiële waarde groter is dan bouw- en beheerkosten.

### B. Open-source hulpmiddel

- **Waarde:** gedeeld bron- en regelwerk en transparantie.
- **Inkomsten:** geen of vrijwillige sponsoring.
- **Risico:** bijdragen en aansprakelijkheidsverwachtingen zonder stabiele inkomsten.
- **Go/no-go:** alleen met duidelijke governance, disclaimers en bronlicenties.

### C. Consumentenabonnement

- **Waardepropositie:** betrouwbare monitoring, gepersonaliseerde ladder en afloopmeldingen.
- **Inkomstenvoorbeeld:** €2–€5 per maand per betalende gebruiker.
- **Probleem:** de jaarlijkse optimalisatiewaarde voor kleine saldi kan lager zijn dan het abonnement; acquisitie, support, juridische toetsing en security drukken de marge.
- **Go/no-go:** pas na interviews, bereidheid-tot-betalenonderzoek en complianceanalyse.

### D. Affiliate- of leadmodel

- **Voordeel:** gebruiker betaalt mogelijk niets.
- **Kernrisico:** belangenconflict; vergoeding kan rangschikking beïnvloeden en bemiddelings-/transparantievragen oproepen.
- **Go/no-go:** niet opnemen in de MVP; vereist expliciet nieuw besluit en juridische toets.

### E. B2B-datadienst

- **Waarde:** gevalideerde product-, entiteits- en garantiestelseldata.
- **Probleem:** hoge eisen aan actualiteit, licenties, aansprakelijkheid en servicelevels.
- **Go/no-go:** alleen als bronrechten en datakwaliteit aantoonbaar schaalbaar zijn.

## 8. Voorlopige businesscaseconclusie

1. **Bouw geen volledige commerciële toepassing op speculatie.** Valideer eerst handmatig of de renteverschillen en tijdsbesparing materieel zijn.
2. **De privétool is vooral een leer-, controle- en beslisondersteuningsproject.** Bij een klein saldo is de zuiver financiële terugverdientijd waarschijnlijk ongunstig.
3. **Schaal helpt, maar verhoogt tegelijk toezicht-, privacy-, security- en onderhoudskosten.** Een groter beheerd of beïnvloed saldo is niet gratis rendement.
4. **De eerstvolgende investering moet 20–40 uur onderzoek zijn**, niet 100+ uur softwarebouw.
5. **Go/no-go na fase 1:** alleen een proof of concept bouwen wanneer minimaal vijf toegankelijke producten betrouwbaar vergelijkbaar zijn, juridische blokkers ontbreken en een realistisch gebruikersscenario ten minste 0,50 procentpunt bruto verbetering of aantoonbare tijd-/risicowaarde laat zien. De drempel van 0,50 procentpunt is een projectaanname, geen marktfeit, en moet na onderzoek worden herzien.

## 9. Onzekerheden die eerst moeten worden opgelost

- Is het uitsluitend een privétool, of is gebruik door derden beoogd?
- Wat zijn jurisdictie, fiscaal kader, saldo, noodbuffer en maximale looptijd?
- Welke banken en landen zijn toegestaan?
- Kan vergunning- en merkaggregatie uit officiële bronnen betrouwbaar worden bijgehouden?
- Welke bronvoorwaarden staan geautomatiseerd ophalen en bewaren toe?
- Welke tijdswaarde gebruikt de businesscase?
- Is een betaalde dienst wenselijk, en zo ja: abonnement, open source of B2B?

Zonder antwoorden hierop blijven opbrengst, planning en commerciële haalbaarheid scenario's en geen prognose.
