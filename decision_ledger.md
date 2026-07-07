<record id="DEC-001" kategori="Arkitektur">
  <beslut>Etablera en strikt modulär katalogstruktur med dokumentation (docs/), statiska datafiler (data/), källkod (src/) och tester (tests/), samt ett override-skyddat JSON-schema i relation_state.json.</beslut>
  <kärna>Arkitekturstruktur och override-hantering</kärna>
  <motivering>Den modulära strukturen säkerställer god kodkvalitet och separation av ansvar. Separation av computed och override-värden garanterar att manuella justeringar från djupintervjuer inte skrivs över av beräkningsmotorn vid framtida tester eller omladdningar.</motivering>
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

<record id="DEC-008" kategori="Planering">
  <beslut>Lägga till draget SECURE_ATTACHMENT och 6 st attraktionsregler i traits.json, samt uppdatera beräkningslogiken (+10% poäng per synergi, max 100%) i både Python och JS.</beslut>
  <kärna>Planering av relationssynergier och poängjusteringar</kärna>
  <motivering>Möjliggör en mer balanserad relationskartläggning där par inte bara ser sina krockar i rött, utan även sina gemensamma styrkor och synergier i grönt. Synk-poängen kan justeras uppåt av synergier upp till max 100%.</motivering>
</record>

<record id="DEC-009" kategori="Implementation">
  <beslut>Implementerade synergier via traits.json och tog bort hårdkodad TKI-logik</beslut>
  <kärna>Single Source of Truth för interaktioner</kärna>
  <motivering>Enligt granskningen (FAS 2) och planeringen (FAS 6) lades SECURE_ATTACHMENT och 6 nya positiva synergier in i traits.json. Den äldre hårdkodade koden i psychometrics.py och dashboard_template.html för Collaborating/Competing plockades bort för att undvika dubbelräkning och bibehålla datadriven arkitektur (DEC-003). SVG-rendering i dashboard gjordes explicit (else if) och SwedishLabel uppdaterades. Under efterföljande audit ändrades matematiken så att synergier är kvalitativa och inte maskerar krockar i sync_score.</motivering>
</record>

<record id="DEC-010" kategori="Utveckling">
  <beslut>Implementera automatisk versionskontroll och ändringslogg (changelog) i dashboarden. Versionskontrollen använder en inbäddad build-timestamp och inaktiveras tyst vid file:// protokoll för att undvika CORS-blockeringar. Efter uppdatering triggas en automatisk omladdning med URL-parametrar som direkt presenterar nyhetsloggen för användaren.</beslut>
  <kärna>Automatisk versionskontroll med grace-degradering för lokala filer</kärna>
  <motivering>Genom att checka window.location.protocol och stoppa fetch vid file:// undviks röda felmeddelanden i konsolen vid lokal körning. Tidsstämpel och changelog-data hämtas och parsar live från en bakgrundsfetch mot servern, vilket säkerställer att användare på GitHub Pages direkt och sömlöst notifieras om nya uppdateringar.</motivering>
</record>

<record id="DEC-011" kategori="Refaktorisering">
  <beslut>Refaktorisera auto-uppdateraren så att versionskontroll sker mot en statisk version.json i stället för regex-parsning av hela dashboard.html.</beslut>
  <kärna>JSON-baserad versionskontroll och säkrad parsning</kärna>
  <motivering>Erkänt som en kritisk sårbarhet under fientlig granskning (FAS 8 / Audit) eftersom regex-parsningen skulle krascha vid förekomster av markerings- eller arraysymboler (såsom '];') i ändringsloggens fritext. Genom att dumpa en minimalistisk version.json vid byggtillfället och parsa den med JSON.parse() görs nätverkstransaktionen säker, XSS-skyddad och extremt bandbreddseffektiv.</motivering>
</record>

<record id="DEC-012" kategori="Felsökning">
  <beslut>Fixa LocalStorage-caching av beräknade drag genom att alltid räkna om profiler från råa enkätsvar på start, samt lägga till nya regler för trygg anknytningsbuffert.</beslut>
  <kärna>Eliminering av cache-låsning och utökade relationssynergier</kärna>
  <motivering>Upptäckte att tillägget av SECURE_ATTACHMENT inte visades på befintliga importerade användarprofiler i webbläsaren på grund av att localStorage returnerade förberäknade statiska drag från den äldre klientsessionen. Genom att alltid räkna om allt på load säkerställs att ändringar i traits.json direkt reflekteras. Lade dessutom till 4 nya buffert-synergier för par där den ena är trygg och den andra är ångestfylld/undvikande.</motivering>
</record>

<record id="DEC-013" kategori="Utveckling">
  <beslut>Refaktorisera relationssynergier för att vara studentligt ömsesidigt beskrivande i traits.json.</beslut>
  <kärna>Bilateralisering av synergi-beskrivningar</kärna>
  <motivering>Justerade beskrivningarna för RULE_SECURE_BUFFER och RULE_HSP_SUPPORT_SECURE så att de inte bara beskriver hur en part drar fördel av den andre, utan tydligt lyfter fram den ömsesidiga dynamiken (t.ex. hur den tryggas stabilitet frigör den ångestfylldas lyhördhet till fördel för båda, och hur stresshantering skapar hemmaro för båda).</motivering>
</record>

<record id="DEC-014" kategori="Felsökning">
  <beslut>Åtgärda namnersättnings-bugg för possessiva namn (s-ändelser) i JS, återställa traits.json-beskrivningar till D/E, samt implementera sammanslagning (konsolidering) av dubbla HSP-krockar.</beslut>
  <kärna>Possessiv grammatikjustering och sammanslagna mönsterkrockar</kärna>
  <motivering>Uppmärksammade att de nya synergitexterna inte ersatte namnen (Emmas/Davids visades fortfarande) eftersom JavaScript-ersättaren letar efter standardiserade D- och E-placeholders och \b-gränser inte matchar när s-ändelsen ligger direkt emot placeholder-namnet. Återställde därför beskrivningarna till D:s och E:s. Förbättrade dessutom formatRuleText till att generera korrekt svensk possessiv (genitiv utan kolon, t.ex. Daniels/Elises istället för Daniel:s/Elise:s). Lade även till logik i renderDetailedFindings för att slå ihop dubbla (inversa) HSP-återhämtningskrockar till en enda sammanslagen mönsterkrock-kort för ökad överskådlighet.</motivering>
</record>

<record id="DEC-015" kategori="Felsökning">
  <beslut>Konsolidera ömsesidig kritik/stonewalling krock (Gottman), samt lägga till tid-baserad cache-buster vid versionsuppdateringar.</beslut>
  <kärna>Gottman-krockskonsolidering och cache-buster vid uppdatering</kärna>
  <motivering>Löste problemet där "Uppdatering tillgänglig!" visades upprepade gånger trots uppdatering, vilket berodde på att webbläsare cachar dashboard.html aggressivt och serverade den gamla filen även vid omladdningar. Genom att lägga till &v=Date.now() vid reload tvingas webbläsaren att bypassa cachen och hämta den senaste HTML-filen. Konsoliderade även RULE_GOTTMAN_CRITICISM_STONEWALLING och dess invers till ett enskilt kort ('Ömsesidig destruktiv eskalering') om båda parter uppvisar båda beteenden.</motivering>
</record>


