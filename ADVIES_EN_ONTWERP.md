# RenteKompas — advies en conceptueel ontwerp

## 1. Advies

Onderzoek een spaar- en depositoladder in plaats van een handelssysteem. Het beoogde systeem vergelijkt alleen producten die de vooraf ingestelde veiligheidsregels doorstaan, bewaakt de liquiditeitsbuffer en spreidt afloopmomenten. Het doet voorstellen; de gebruiker controleert voorwaarden en voert transacties uit.

Deze richting benadert “weinig kennis en aandacht” en “beheersbaar risico”, maar garandeert geen koopkracht of toekomstige rente. Een garantiestelsel heeft juridische voorwaarden en limieten. Product-, bank-, merk- en vergunningstructuren moeten daarom expliciet worden geverifieerd.

## 2. Benodigde informatie

### Product

- juridische bankentiteit en merknaam;
- vergunning, toezichthouder en garantiestelsel;
- toepasselijke garantielimiet en aggregatieregels;
- valuta, rente, rentetype en geldigheidsperiode;
- looptijd, minimum- en maximuminleg;
- opname-, verlengings- en beëindigingsvoorwaarden;
- kosten en relevante fiscale aannames;
- officiële voorwaarden, bron-URL, raadpleegdatum en documenthash.

### Gebruiker

- jurisdictie en fiscale woonplaats;
- beschikbaar bedrag en periodieke inleg;
- minimale vrij opneembare noodbuffer;
- tijdshorizon en maximale vastzettermijn;
- maximale blootstelling per juridische bankentiteit;
- toegestane landen, valuta en garantiestelsels;
- gewenste veiligheidsmarge onder een wettelijke limiet.

Persoons- en financiële gegevens worden niet in deze repository opgeslagen.

## 3. Componenten

1. **Bronregister** — catalogiseert officiële bronnen en hun geldigheid.
2. **Collector** — haalt openbare documenten en productgegevens op en archiveert metadata.
3. **Parser/normalisator** — zet brongegevens om in een uniform productschema.
4. **Validator** — controleert volledigheid, actualiteit, onderlinge consistentie en herkomst.
5. **Entiteitenregister** — koppelt merknaam aan juridische bank, vergunning en garantiestelsel.
6. **Risico-engine** — past harde uitsluitingen en blootstellingslimieten toe.
7. **Rekenmodule** — berekent nominale bruto- en nettoresultaten en liquiditeitsscenario's.
8. **Ladderplanner** — maakt voorstellen met gespreide afloopdata.
9. **Rapportage en meldingen** — toont aanbeveling, onzekerheid, bron en benodigde actie.
10. **Goedkeuringswachtrij** — registreert menselijke acceptatie of afwijzing; voert geen betaling uit.
11. **Positie- en afloopregister** — bewaakt verwachte rente, einddatum en herbeoordeling.
12. **Auditlog** — legt invoer, regelversie, resultaat, controle en fouten append-only vast.

## 4. Informatiestroom

```text
Officiële bronnen
      |
      v
Collector ---> ongewijzigde bronmetadata + hash
      |
      v
Normalisator ---> gevalideerde productrecords
      |                       |
      v                       v
Entiteitenregister       bron-/kwaliteitsstatus
      |                       |
      +----------+------------+
                 v
           Risico-engine ----> uitgesloten + reden
                 |
                 v
           Rekenmodule
                 |
                 v
           Ladderplanner
                 |
                 v
        Rapport + menselijke goedkeuring
                 |
      handmatige uitvoering buiten systeem
                 |
                 v
        Positie-/afloopmonitor
```

Componenten wisselen versieerbare records uit. Ieder afgeleid record verwijst naar bron-ID, raadpleegmoment, parser-/regelversie en validatiestatus.

## 5. Initiële harde regels

- alleen EUR;
- alleen verifieerbare juridische bankentiteiten en garantiestelsels;
- geen onduidelijke of verlopen brongegevens;
- totaal per bankentiteit blijft onder de ingestelde interne limiet;
- noodbuffer blijft direct beschikbaar;
- geen automatische verlenging tenzij expliciet gewenst en tijdig herbeoordeeld;
- geen automatische geldbeweging;
- geen productselectie uitsluitend op het hoogste rentepercentage.

De concrete bedragen, ouderdomsgrenzen en toegestane jurisdicties worden pas na onderzoek als besluit vastgelegd.

## 6. Technische uitgangspunten

Een minimale eerste implementatie kan bestaan uit Python, SQLite, periodieke jobs en e-mailmeldingen. PostgreSQL of cloudinfrastructuur wordt pas toegevoegd als schaal, samenwerking of operationele eisen dat rechtvaardigen.

Beoogde interfaces:

- collector naar normalisator: versieerbaar bronrecord;
- normalisator naar validator: uniform productrecord;
- validator naar risico-engine: alleen gevalideerde records;
- risico-engine naar planner: toegestane producten plus limieten;
- planner naar gebruiker: leesbaar voorstel met volledige onderbouwing;
- monitor naar gebruiker: waarschuwing, nooit zelfstandig financieel handelen.

## 7. Niet-functionele eisen

- herleidbaarheid van ieder getoond getal;
- idempotente gegevensverwerking;
- expliciete tijdzones en geldigheidsintervallen;
- append-only auditgebeurtenissen;
- versleuteling van gevoelige lokale gegevens;
- least privilege en read-only waar mogelijk;
- back-up- en hersteltest vóór productiegebruik;
- toegankelijke foutmeldingen en zichtbare onzekerheid.
