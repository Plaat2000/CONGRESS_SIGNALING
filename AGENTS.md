# Werkinstructies voor mens en agent

De canonieke projectnaam is **RenteKompas** en de beoogde repositoryslug is
`rentekompas`. Gebruik geen historische repository- of Congress-naam voor het
actieve project.

Deze instructies gelden voor de volledige projectrepository. De map
`archive/congress-signaling/` is alleen-lezen erfgoed: wijzig of activeer de
inhoud daarvan niet, behalve wanneer een expliciete archiefcorrectie wordt
gevraagd.

## Verplichte start van iedere werksessie

1. Lees `README.md`, `PRINCIPES.md` en `BESLUITEN.md`.
2. Controleer de openstaande punten in `ROADMAP.md`.
3. Bevestig dat het voorgenomen werk binnen de scope en risicogrenzen valt.
4. Stop en documenteer het conflict wanneer een opdracht strijdig is met een leidend principe. Een principe mag alleen via een expliciet, gemotiveerd besluit worden gewijzigd.

## Definitie van klaar

Een taak is pas klaar als:

- relevante feiten een bron, raadpleegdatum en geldigheidsstatus hebben;
- aannames expliciet zijn gemaakt;
- risico's en uitzonderingen zijn beschreven;
- relevante documentatie tegelijk met de wijziging is bijgewerkt;
- een materieel besluit in `BESLUITEN.md` staat;
- uitgevoerde controles en hun uitkomst in `LOGBOEK.md` staan;
- gevoelige gegevens niet zijn vastgelegd;
- duidelijk is of menselijke goedkeuring nodig blijft.

## Gedragsregels

- Gebruik primaire, officiële en actuele bronnen voor financiële voorwaarden, vergunningen en garantiestelsels.
- Presenteer geen opbrengst als gegarandeerd zonder exact te benoemen wie wat, onder welke voorwaarden en tot welke grens garandeert.
- Automatiseer onderzoek en monitoring vóór uitvoering. Geldbewegingen zijn standaard handmatig en vereisen expliciete goedkeuring.
- Optimaliseer nooit alleen op rente; pas eerst alle veiligheids-, liquiditeits- en geschiktheidsregels toe.
- Gebruik transparante, reproduceerbare regels boven niet-uitlegbare modellen.
- Scheid feiten, aannames, berekeningen, aanbevelingen en besluiten.
- Bewaar geen wachtwoorden, API-sleutels, persoonsgegevens, rekeningnummers of banksaldi in Git of logs.
- Voeg geen aandelen-, crypto-, derivaten-, leverage- of copy-tradingstrategie toe zonder een expliciet scopebesluit. Zulke strategieën zijn standaard uitgesloten.

## Vaste onderhoudstaken

Voer bij iedere materiële wijziging de checklist in `STANDAARD_TAKEN.md` uit. Werk nooit alleen code bij wanneer daardoor documentatie, bronnen, risico's, tests of besluiten verouderen.
