# RenteKompas — roadmap en acceptatiepoorten

## Fase 0 — Projectkader

**Status:** voltooid op 2026-09-26.

- doel, scope en leidende principes vastleggen;
- initiële architectuur, risico's en standaardtaken documenteren;
- besluit- en werklog starten;
- instructies voor toekomstige agents vastleggen.

**Acceptatiepoort:** documenten zijn onderling consistent, vindbaar en versieerbaar.

## Fase 1 — Vereisten en juridisch brononderzoek

**Status:** eerstvolgend.

- gebruikersprofiel en liquiditeitsregels definiëren zonder persoonsgegevens op te slaan;
- initiële jurisdictie en toegestane garantiestelsels besluiten;
- officiële bronnen, voorwaarden en aggregatieregels verifiëren;
- datavelden, actualiteitsdrempels en foutbeleid vastleggen;
- meetbare veiligheids- en bruikbaarheidscriteria vaststellen.
- businesscase doorrekenen met incrementele rente, tijdswaarde en beheerlast;
- juridische triage uitvoeren voor privégebruik, personalisatie, bemiddeling, privacy en betaaldiensten;
- minimaal vijf producten handmatig end-to-end valideren.
- vóór publiek of commercieel gebruik de beschikbaarheid van handelsnaam, merk, domein en relevante package-/accountnamen voor `RenteKompas` controleren.

**Acceptatiepoort:** iedere kritieke regel is herleidbaar naar een geverifieerde bron of expliciete gebruikerskeuze; open juridische onzekerheden blokkeren automatisch advies. Daarnaast geldt besluit D-004: pas door naar fase 2 bij betrouwbare vergelijkbaarheid en voldoende economische of aantoonbare tijd-/risicowaarde.

## Fase 2 — Handmatig proof of concept

- klein, handmatig geverifieerd productbestand maken;
- uniform schema en validator implementeren;
- blootstelling, rente en ladder handmatig narekenen;
- rapport met uitsluitingsredenen genereren.

**Acceptatiepoort:** testvoorbeelden zijn reproduceerbaar en een onafhankelijke handberekening komt overeen.

## Fase 3 — Read-only automatisering

- collectors voor goedgekeurde bronnen bouwen;
- bronversies, hashes en geldigheid opslaan;
- monitoring, foutmeldingen en auditlog implementeren;
- regressie-, integratie- en beveiligingstests toevoegen.

**Acceptatiepoort:** bronfouten leiden aantoonbaar tot blokkering; geen component kan geld verplaatsen.

## Fase 4 — Persoonlijke planning zonder uitvoering

- lokale, beschermde gebruikersconfiguratie toevoegen;
- scenario's en laddervoorstellen genereren;
- menselijke goedkeuringsworkflow en afloopmeldingen testen;
- privacy-, dreigings- en herstelreview uitvoeren.

**Acceptatiepoort:** expliciet go/no-go-besluit na proefgebruik; beperkingen zijn zichtbaar in ieder rapport.

## Niet gepland zonder nieuw besluit

- autonome productopening of geldbeweging;
- broker- of handelsfunctionaliteit;
- uitbreiding naar niet-EUR of niet-deposito-activa;
- productiegebruik met gevoelige gegevens.
