# Besluitlog

Besluiten worden append-only toegevoegd. Een vervangen besluit blijft staan en verwijst naar zijn opvolger.

## D-001 — Depositoladder als eerste oplossingsrichting

- **Datum:** 2026-09-26
- **Status:** geaccepteerd
- **Context:** de gewenste oplossing moet weinig aandacht vragen, openbare informatie gebruiken en risico beheersbaar houden. Gegarandeerd aantrekkelijk beleggingsrendement bestaat niet.
- **Besluit:** onderzoek eerst een optimizer voor euro-spaarrekeningen en termijndeposito's met een liquiditeitsbuffer en gespreide afloopmomenten.
- **Alternatieven:** geautomatiseerde aandelenhandel, Congress-signalen, crypto en arbitrage.
- **Reden:** deposito's hebben beter uitlegbare contractvoorwaarden en risico's; marktstrategieën bieden geen gegarandeerde opbrengst.
- **Gevolgen:** markthandel en Congress-signalen vallen buiten de initiële scope.
- **Gerelateerde principes:** P1, P2, P3, P4, P13.

## D-002 — Read-only eerst, uitvoering door de mens

- **Datum:** 2026-09-26
- **Status:** geaccepteerd
- **Context:** automatische geldbeweging vergroot fraude-, authenticatie- en foutimpact.
- **Besluit:** de eerste oplossing automatiseert bronnen, validatie, berekening, voorstellen en monitoring, maar opent geen producten en verplaatst geen geld.
- **Alternatieven:** directe bank- of PSD2-betaalkoppeling.
- **Reden:** menselijke controle beperkt operationeel risico terwijl vrijwel al het terugkerende onderzoekswerk kan worden geautomatiseerd.
- **Gevolgen:** iedere aanbeveling eindigt in een goedkeuringswachtrij en handmatige actie buiten het systeem.
- **Gerelateerde principes:** P6, P7, P9.

## D-003 — Repositorydocumentatie is de bron van waarheid

- **Datum:** 2026-09-26
- **Status:** geaccepteerd
- **Context:** chatcontext is tijdelijk en toekomstige agents hebben consistente instructies nodig.
- **Besluit:** principes, besluiten, bronnen, risico's, roadmap en werkzaamheden worden in deze projectruimte bijgehouden. Chatbesluiten zijn pas duurzaam nadat ze hier zijn vastgelegd.
- **Alternatieven:** alleen chathistorie of losse notities gebruiken.
- **Reden:** versiebeheer maakt wijzigingen traceerbaar en overdraagbaar.
- **Gevolgen:** documentatie bijwerken is onderdeel van de definitie van klaar.
- **Gerelateerde principes:** P8, P14.

## D-004 — Haalbaarheidspoort vóór softwarebouw

- **Datum:** 2026-09-26
- **Status:** geaccepteerd
- **Context:** de incrementele rente kan kleiner zijn dan de kosten van bouwen, beheren, overstappen en compliance.
- **Besluit:** besteed eerst maximaal 20–40 uur aan fase 1. Bouw pas een proof of concept wanneer minimaal vijf producten betrouwbaar vergelijkbaar zijn, geen onopgeloste juridische blokker is gevonden en een realistisch scenario ten minste 0,50 procentpunt bruto verbetering of aantoonbare tijd-/risicowaarde biedt.
- **Alternatieven:** direct een volledige scraper en applicatie bouwen.
- **Reden:** een vroege economische en juridische stopproef voorkomt een technisch werkend maar onrendabel of niet verantwoord product.
- **Gevolgen:** de drempel is een expliciete projectaanname en wordt na brononderzoek herzien; geen actuele marktrente of opbrengst wordt ermee beloofd.
- **Gerelateerde principes:** P1, P5, P10, P11, P12.

## D-005 — Congress Signaling afsluiten en actieve projectruimte verplaatsen

- **Datum:** 2026-09-26
- **Status:** geaccepteerd
- **Context:** de deposito-optimizer stond als submap in een repository waarvan naam en rootinhoud nog naar het eerdere Congress Signaling-project verwezen. Daardoor was onduidelijk welk project actief was.
- **Besluit:** sluit Congress Signaling af, verplaats de historische bestanden naar het alleen-lezen archief `archive/congress-signaling/` en gebruik de repositoryroot als exclusieve actieve projectruimte voor de spaar- en deposito-optimizer.
- **Alternatieven:** de deposito-optimizer als submap behouden; historische bestanden verwijderen; een niet-gekoppelde tweede lokale Git-repository maken.
- **Reden:** één duidelijke actieve root voorkomt scopeverwarring, terwijl archivering de historie behoudt.
- **Gevolgen:** het archief is geen dependency of databron; nieuwe wijzigingen volgen de principes en werkinstructies in de root.
- **Gerelateerde principes:** P10, P13, P14.

## D-006 — Projectnaam RenteKompas

- **Datum:** 2026-09-26
- **Status:** geaccepteerd
- **Context:** de historische repositorynaam verwijst naar Congress, terwijl het actieve project uitsluitend veilige rentevergelijking en depositoplanning onderzoekt. De functionele omschrijving “deposito-optimizer” is duidelijk maar niet geschikt als herkenbare projectnaam.
- **Besluit:** gebruik **RenteKompas** als canonieke projectnaam en `rentekompas` als slug voor een toekomstige Git-remote, map of externe projectomgeving.
- **Alternatieven:** DepositoKompas, SpaarKompas, RenteWachter, Veilige Renteplanner en de functionele naam Deposito Optimizer.
- **Reden:** “Rente” dekt zowel vrij opneembaar sparen als deposito's; “Kompas” benadrukt beslisondersteuning zonder rendement of garantie te beloven. De naam is Nederlands, kort en sluit aan op de read-only menselijke besluitvorming.
- **Gevolgen:** actieve documentatie, toekomstige code, packages en externe omgevingen gebruiken RenteKompas. Historische besluiten en het alleen-lezen archief worden niet herschreven. Beschikbaarheid van handelsnaam, domein en merk is nog niet juridisch onderzocht.
- **Gerelateerde principes:** P2, P7, P8, P12, P13.

## Sjabloon

```markdown
## D-XXX — Titel

- **Datum:** JJJJ-MM-DD
- **Status:** voorgesteld | geaccepteerd | vervangen | afgewezen
- **Context:**
- **Besluit:**
- **Alternatieven:**
- **Reden:**
- **Gevolgen:**
- **Gerelateerde principes:**
- **Vervangt/vervangen door:** indien van toepassing
```
