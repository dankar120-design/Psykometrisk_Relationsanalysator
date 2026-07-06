# PRD: Psykometrisk Relationsanalysator
Operativ Status: Arkitekturfas

## 1. Systemarkitektur
Detta system byggs i Google Antigravity för strikt logisk isolering från chatthistorikens brus. Målet är att samla in, komprimera och utvärdera relationsdynamik mellan två parter (D och E) via en state machine-arkitektur sparad i JSON-format.
- **Frontend/CLI:** Interaktivt frågebatteri med retro-terminal-estetik (amber/green).
- **Backend:** Lokal state machine (Python) som övervakar och iterativt uppdaterar JSON-noder.
- **Analysmotor:** Regelbaserad korsutvärdering av D och E:s asymmetriska datamängder.

## 2. Psykometriska Moduler
- **Anknytningsteori:** Närhetsbehov, Distansering, Autonomibehov. Prediktion av separationsångest kontra undvikande mekanismer.
- **HSP (Aron):** Sensorisk tröskel, Fysisk återhämtningstid. Kvantifiering av kognitiv överbelastning i timmar.
- **Gottmans 4 Ryttare:** Kritik, Förakt, Defensivitet, Stonewalling. Matematisk identifiering av interpersonell systemkollaps.
- **Big Five / TKI:** Samvetsgrannhet (C), Konfliktstrategi. Logistisk kompatibilitet gällande tid, resurser och krishantering.

## 3. Datastruktur
Applikationens kärna är filen `relation_state.json`. Inmatad rådata komprimeras strikt till denna struktur.

## 4. Exekveringslogik för Analysatorn
Logiken bygger på att identifiera anomalier och krockar mellan D och E:s parametrar enligt fysiska lagar för beteende.
1. **Inläsning:** Parsern laddar `relation_state.json`.
2. **Beräkning av Delta:** Scriptet jämför asymmetriska variabler.
3. **Utdata:** Motorn renderar en binär terminal-utskrift med röda flaggor (kinetiska/emotionella risker) och gröna ljus (kompatibla domäner). Ingen subjektiv rådgivning adderas.
