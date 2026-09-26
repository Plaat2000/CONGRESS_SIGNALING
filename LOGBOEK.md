# Werk- en controlelog

Het log is append-only en bevat geen persoonsgegevens, rekeninggegevens, tokens of andere geheimen.

## 2026-09-26 — Projectruimte aangemaakt

- Advies voor een veilige spaar- en depositoladder vastgelegd.
- Scope, veertien leidende principes en initiële architectuur beschreven.
- Besluitlog, bronregister, risicoanalyse en gefaseerde roadmap gestart.
- Verplichte standaardtaken en agentinstructies toegevoegd.
- Vastgelegd dat automatische geldbewegingen buiten de initiële scope vallen.

### Controles

- Documentnavigatie en relatieve bestandsverwijzingen gecontroleerd.
- Gecontroleerd dat de nieuwe documenten geen wachtwoorden, tokens, rekeningnummers of persoonlijke financiële gegevens bevatten.
- Gecontroleerd dat “garantie” steeds begrensd en voorwaardelijk wordt beschreven.

## Sjabloon voor volgende registraties

```markdown
## JJJJ-MM-DD — Korte titel

- Uitgevoerd werk:
- Gewijzigde aannames:
- Besluiten (verwijs naar D-XXX):
- Bronnen (verwijs naar SRC-XXX):
- Risico-effect:
- Controles en exacte commando's:
- Resultaat en open punten:
```

## 2026-09-26 — Project hernoemd naar RenteKompas

- **RenteKompas** gekozen als canonieke naam en `rentekompas` als toekomstige repositoryslug.
- Actieve titels, README, agentinstructies en archiefgrens bijgewerkt.
- Historische besluiten en archiefbestanden bewust niet herschreven.
- Besluit D-006 toegevoegd met alternatieven, motivatie en naamsrisico.

### Controles

- Actieve Markdown-titels en naamverwijzingen gecontroleerd.
- Lokale Markdown-links en code fences gecontroleerd.
- Gecontroleerd dat de naam geen opbrengst- of garantieclaim bevat.
- Externe handelsnaam- en merkcontrole geprobeerd; de webzoekfunctie gaf HTTP 401. Beschikbaarheid blijft daarom expliciet onbevestigd en is als roadmaptaak vastgelegd.
- `git diff --check` uitgevoerd.

## 2026-09-26 — Congress Signaling afgesloten en projectroot ingericht

- Alle historische Congress Signaling-bestanden verplaatst naar `archive/congress-signaling/`.
- De documentatie van de deposito-optimizer van een submap naar de repositoryroot verplaatst.
- `ARCHIEFBELEID.md` toegevoegd met afsluitings- en heropeningsregels.
- Besluit D-005 toegevoegd en agentinstructies uitgebreid met een alleen-lezen archiefregel.
- De actieve README wijst nu eenduidig naar het nieuwe project en alle kernstukken.

### Controles

- Gecontroleerd dat alle lokale Markdown-links na de verplaatsing bestaan.
- Gecontroleerd dat actieve documenten niet meer naar de voormalige submap verwijzen.
- Gecontroleerd dat alle eerder getrackte legacybestanden in het archief aanwezig zijn.
- `git diff --check` uitgevoerd.

## 2026-09-26 — Haalbaarheid en businesscase toegevoegd

- Realisatierisico's geprioriteerd en voorzien van vroege signalen en stopmaatregelen.
- Kritieke taken afgezet tegen mogelijke bank-, toezicht-, privacy- en betaaldiensteisen.
- Benodigde kennis en een indicatieve fasering voor privé-MVP en eventuele publieke dienst beschreven.
- Financiële scenario's toegevoegd voor totale nominale rente en de relevantere incrementele rente.
- Persoonlijk, open-source, abonnements-, affiliate- en B2B-model beoordeeld.
- Besluit D-004 toegevoegd: eerst een begrensde haalbaarheidsfase, daarna pas softwarebouw.
- Externe officiële bronnen als kandidaat geregistreerd; netwerkbeperkingen en ontbrekende formele verificatie expliciet vastgelegd.

### Controles

- Scenario-tabellen onafhankelijk nagerekend met een Python-script.
- Lokale Markdown-links gecontroleerd.
- `git diff --check` uitgevoerd.
- Gecontroleerd dat ramingen als aannames en niet als actuele rente of garantie zijn gepresenteerd.
