# Sub-PRD: Psykometriska Profiler & Interaktionsregler

Detta dokument beskriver de psykometriska modulerna i detalj, inklusive underkategorier och reglerna för asymmetriska relationskrockar och attraktionsfaktorer.

## 1. Anknytningsteori
Vi spårar `anxiety_score` och `avoidance_score` (0.0 till 1.0).
- **Anxious-Preoccupied (Ångestfylld):** Hög ångest (> 0.6), låg undvikande (< 0.4). Kännetecknas av starkt närhetsbehov och separationsångest. Stressrespons: Hyperaktivering (söker omedelbar kontakt/verbal bekräftelse).
- **Dismissive-Avoidant (Avfärdande-undvikande):** Låg ångest (< 0.4), högt undvikande (> 0.6). Kännetecknas av extrem självständighet och distansering. Stressrespons: Deaktivering (drar sig undan, stänger av känslor).
- **Fearful-Avoidant (Räddhågsen-undvikande/Desorganiserad):** Hög ångest (> 0.6), högt undvikande (> 0.6). Vill ha närhet men är rädd för den.
- **Secure (Trygg):** Låg ångest (< 0.4), lågt undvikande (< 0.4).

### Interaktionsregler
- **Ångest-Undvikande-fällan (Pursue-Withdraw):** Om Part A är Anxious-Preoccupied och Part B är Dismissive-Avoidant under stress. A:s hyperaktivering (jakt på närhet) triggar B:s deaktivering (flykt/ Stonewalling), vilket i sin tur ökar A:s ångest. Kritisk krock.

## 2. HSP (Highly Sensitive Person)
Vi delar upp HSP-känslighet i tre underkategorier baserat på Arons forskning:
- **LST (Low Sensory Threshold):** Känslighet för sensoriska intryck (ljus, ljud, folkmassor).
- **AES (Aesthetic Sensitivity):** Djup uppskattning för konst, musik och subtila miljöer.
- **EOE (Ease of Excitation):** Att bli snabbt överväldigad av högt tempo eller för mycket att göra samtidigt.

### Interaktionsregler
- **Sensorisk återhämtningskrock:** Om Part A har hög återhämtningstid (`recovery_latency_hrs` >= 4) och Part B har en stressrespons som kräver omedelbar verbal tröst (hyperaktivering). Vid en kris uppstår en oundviklig krock där A behöver avskildhet för att ladda ur sensoriskt, medan B upplever denna tystnad som avvisande.

## 3. Gottmans 4 Ryttare
Vi spårar förekomsten av:
- **Kritik (Criticism)**
- **Förakt (Contempt)** - Starkaste prediktorn för skilsmässa
- **Defensivitet (Defensiveness)**
- **Stonewalling (Stenmurande)**

### Interaktionsregler
- **Kritik-Stonewalling-loopen:** Om Part A uppvisar Kritik och Part B uppvisar Stonewalling under konflikt. Detta skapar en destruktiv eskalering där dialog blir omöjlig.

## 4. TKI (Thomas-Kilmann Conflict Mode Instrument)
Vi spårar den primära konfliktstrategin:
- **Competing (Konkurrerande):** Hög målmedvetenhet, låg samarbetsvilja.
- **Collaborating (Samarbetande):** Hög målmedvetenhet, hög samarbetsvilja.
- **Compromising (Kompromissande):** Måttlig målmedvetenhet, måttlig samarbetsvilja.
- **Avoiding (Undvikande):** Låg målmedvetenhet, låg samarbetsvilja.
- **Accommodating (Anpassande):** Låg målmedvetenhet, hög samarbetsvilja.

### Interaktionsregler
- **Konkurrerande Systemkollaps:** Competing vs Competing leder till en maktkamp.
- **Undvikande Stagnation:** Avoiding vs Avoiding leder till olösta problem som växer över tid.
