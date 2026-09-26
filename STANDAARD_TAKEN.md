# Standaardtaken

## Bij de start van iedere sessie

- [ ] Lees `AGENTS.md`, `PRINCIPES.md`, `BESLUITEN.md` en `ROADMAP.md`.
- [ ] Controleer repositorystatus en onafgerond werk.
- [ ] Benoem doel, scope en relevante principes.
- [ ] Controleer of actuele externe feiten opnieuw moeten worden geverifieerd.
- [ ] Noteer aannames en benodigde besluiten.

## Bij iedere inhoudelijke wijziging

- [ ] Koppel de wijziging aan een roadmap-item of leg uit waarom deze ongepland is.
- [ ] Werk ontwerp, risico's en bronnen gelijktijdig bij waar relevant.
- [ ] Voeg of actualiseer tests en validaties.
- [ ] Controleer dat geen geheimen of persoonsgegevens zijn toegevoegd.
- [ ] Controleer dat voorbeelden geen garantie of persoonlijk advies suggereren.
- [ ] Registreer materiële keuzes in `BESLUITEN.md`.
- [ ] Registreer controles en uitkomsten in `LOGBOEK.md`.

## Bij iedere bronupdate

- [ ] Gebruik bij voorkeur de primaire officiële bron.
- [ ] Leg uitgever, URL, raadpleegdatum, jurisdictie en onderwerp vast.
- [ ] Bewaar geldigheidsdatum en zo mogelijk documentversie of hash.
- [ ] Vergelijk kritieke gegevens met een tweede officiële bron waar mogelijk.
- [ ] Markeer conflicten, verlopen gegevens en onbereikbare bronnen.
- [ ] Laat een product bij twijfel automatisch afvallen (`fail closed`).

## Bij ieder voorstel of iedere berekening

- [ ] Toon bruto-, netto- en liquiditeitseffect afzonderlijk.
- [ ] Toon gebruikte bedragen, renteconventie, looptijd, kosten en aannames.
- [ ] Aggregeer blootstelling per juridische bankentiteit, niet alleen per merk.
- [ ] Controleer noodbuffer en interne limieten.
- [ ] Toon garanties met voorwaarden en uitsluitingen.
- [ ] Toon waarom alternatieven zijn uitgesloten.
- [ ] Vereis menselijke controle van actuele officiële voorwaarden.

## Voor iedere release of faseovergang

- [ ] Alle acceptatiecriteria van de huidige roadmapfase zijn aantoonbaar gehaald.
- [ ] Geautomatiseerde tests en documentcontroles slagen.
- [ ] Dreigings- en risicoanalyse zijn bijgewerkt.
- [ ] Back-up en herstel zijn getest indien gegevens worden bewaard.
- [ ] Logging en waarschuwingen zijn getest.
- [ ] Open beperkingen zijn zichtbaar gedocumenteerd.
- [ ] Een expliciet go/no-go-besluit staat in `BESLUITEN.md`.

## Periodiek

### Wekelijks tijdens actieve ontwikkeling

- [ ] Open besluiten, aannames en roadmap controleren.
- [ ] Mislukte collectors en verouderde bronnen beoordelen.
- [ ] Documentatie op afwijkingen van de implementatie controleren.

### Maandelijks tijdens gebruik

- [ ] Vergunningen, garantiestelselgegevens en juridische entiteiten herverifiëren.
- [ ] Blootstelling, afloopmomenten en veiligheidsmarges controleren.
- [ ] Toegangsrechten, afhankelijkheden en beveiligingswaarschuwingen controleren.

### Bij incidenten

- [ ] Automatische aanbevelingen pauzeren als integriteit onzeker is.
- [ ] Impact en tijdlijn vastleggen zonder gevoelige gegevens te loggen.
- [ ] Bronoorzaak, herstel en preventieve maatregel documenteren.
- [ ] Betrokken afgeleide gegevens ongeldig markeren en opnieuw verwerken.
