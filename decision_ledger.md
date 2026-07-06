<record id="DEC-001" kategori="Arkitektur">
  <beslut>Etablera en strikt modulär katalogstruktur med dokumentation (docs/), statiska datafiler (data/), källkod (src/) och tester (tests/), samt ett override-skyddat JSON-schema i relation_state.json.</beslut>
  <kärna>Arkitekturstruktur och override-hantering</kärna>
  <motivering>Den modulära strukturen säkerställer god kodkvalitet och separation av ansvar. Separation av computed och override-värden garanterar at manuella justeringar från djupintervjuer inte skrivs över av beräkningsmotorn vid framtida tester eller omladdningar.</motivering>
</record>

<record id="DEC-002" kategori="Utveckling">
  <beslut>Implementera den psykometriska beräkningsmotorn och retro-CLI-dashboarden med atomära skrivskyddade logiker och enhetstesta med inbyggda unittest.</beslut>
  <kärna>Genomförande av beräkningsmotor och CLI</kärna>
  <motivering>Användandet av Pythons inbyggda unittest tar bort behovet av externa paket (pytest) vilket bevarar systemets strikta isolering. Tester bekräftar att asymmetriska interaktioner detekteras korrekt och att overrides bibehålls.</motivering>
</record>

<record id="DEC-003" kategori="Refaktorisering">
  <beslut>Refaktorisera interaktionsreglerna till ett generiskt conditions-format i traits.json, implementera safe_run_analysis wrappers samt eliminera syntaxfel i fallback-objekten.</beslut>
  <kärna>Dynamisk regelmotor och kraschsäkring av CLI</kärna>
  <motivering>Genom av flytta interaktionslogiken till ett datadrivet schema med operatorer minimeras underhållsbehovet av psychometrics.py. Safe wrappers och fixade Python-literaler garanterar att manuella justeringar eller tillfälligt korrupta filer aldrig kraschar dashboarden vid hot reload.</motivering>
</record>

<record id="DEC-004" kategori="Säkerhet och Dataintegritet">
  <beslut>Implementera Single Source of Truth för externa tester via dynamisk HTML-export och strukturell fingerprinting.</beslut>
  <kärna>Hash-validering och auto-generering av HTML-test</kärna>
  <motivering>För att förhindra tyst datakorruption av oförenliga enkätversioner genereras nu en unik strukturell SHA-256 fingerprint från QUESTIONS-objektet. distans_test.html genereras direkt från CLI med frågorna och fingerprinten inbäddade. Importfunktionen validerar fingerprinten, validerar formatet med strikt Regex och hanterar Base64-padding-fel.</motivering>
</record>

<record id="DEC-005" kategori="Utveckling">
  <beslut>Implementera klientsides-dashboarden dashboard.html (Calm Sanctuary) med lokal JavaScript-klassificering, SVG-visualisering av relationskrockar, och AI-promptgenerator. Byggsteget sker via build_dashboard.py för att undvika CORS-blockering vid file:// och bibehålla traits.json som Single Source of Truth.</beslut>
  <kärna>Calm Sanctuary dashboard och inbäddad regelmotor via byggskript</kärna>
  <motivering>Löser CORS-begränsningen för lokala HTML-filer genom att baka in frågor och regler vid byggtillfället. Detta möjliggör portabel körning (både file:// och localhost) utan serverkrav för slutanvändaren, samtidigt som utvecklingen hålls DRY.</motivering>
</record>

<record id="DEC-006" kategori="Felsökning">
  <beslut>Refaktorisera JS-regelmotorn till en kapslad struktur som speglar traits.json-sökvägarna, samt införa regex-ordgränser i namnsubstitutionen och fingerprint-baserad cache-invalidering för localStorage.</beslut>
  <kärna>Fidelity-korrigering av regelmotor, namnskydd och cache-invalidering</kärna>
  <motivering>Löste problemet där 6 av 8 regler var döda i klientsides-dashboarden på grund av missmatchade JSON-sökvägar. Förhindrade dessutom korruption av löpande text via string replace samt löste risk för korrupt state vid ändringar av enkäten.</motivering>
</record>

<record id="DEC-007" kategori="UI/Layout">
  <beslut>Implementera custom-modaler (custom-alert-modal) i salvia/sand-temat för att ersätta webbläsarens inbyggda alert-popuper. Anpassa dessutom importbox-höjderna till exakt 40px samt lägg till responsivitet för relationskartan på skärmar under 600px.</beslut>
  <kärna>Temabundna modalpopuper, höjdjusteringar och mobilanpassad visualisering</kärna>
  <motivering>Browser-alerts bryter mot spa-temats premiumkänsla och blockerar trådar. Genom att bygga egna CSS-modaler säkras en enhetlig grafisk profil. Mobiljusteringar på nodes-col (42% bredd och 0.65rem font) förhindrar overflow på mindre skärmar.</motivering>
</record>
