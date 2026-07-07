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

<record id="DEC-016" kategori="Felsökning">
  <beslut>Lösa versionskontrollens loop-fel genom att committa version.json, samt införa strikt datumjämförelse i JavaScript.</beslut>
  <kärna>Driftsättning av version.json och striktare datumlogik</kärna>
  <motivering>Upptäckte att version.json inte fanns med i git add i föregående commit och därför låg kvar i ett gammalt läge på servern, vilket orsakade en mismatch mot den lokalt kompilerade källkoden. Lade även till en striktare datumjämförelse (new Date(remote) > new Date(local)) i JavaScript för att säkerställa att en äldre version på servern aldrig kan trigga falska uppdaterings-notiser i frontend.</motivering>
</record>

<record id="DEC-017" kategori="Utveckling">
  <beslut>Avveckla oanvända CLI-filer, korrigera namn-placeholders i traits.json, samt implementera tema-baserad poängberäkning och status-badges i dashboarden.</beslut>
  <kärna>CLI-avveckling, tema-baserade krockavdrag och relationsstatus</kärna>
  <motivering>Genom byta ut src/cli/analysator.py, src/core/psychometrics.py och tests/test_psychometrics.py rensas oanvänd kod. Korrigering av RULE_TKI_CONSTRUCTIVE_MATCH i traits.json till D/E placeholders möjliggör dynamisk namnsubstitution. Att gruppera krockar per övergripande tema (t.ex. HSP-återhämtning, Gottman-eskalering) förhindrar dubbelräkning av komplementära krockar, vilket vetenskapligt motverkar onödigt låga betyg. Status-badges ger konstruktiv och icke-dömande guidning för par.</motivering>
</record>

<record id="DEC-018" kategori="Felsökning">
  <beslut>Refaktorera krockvisningen till generisk dynamic sammanslagning, samt införa defensiva guards i poängberäkningen.</beslut>
  <kärna>Generisk reciprok sammanslagning och kraschsäkring</kärna>
  <motivering>Efter fientlig granskning (FAS 2) upptäcktes att poängmotorn grupperar alla _REV-krockar generellt medan gränssnittet hade hårdkodad logik för endast HSP och Gottman. Genom att göra renderDetailedFindings helt generisk grupperas nu alla reciproka krockar (t.ex. ångest-undvikande-fällan) dynamiskt under ett ömsesidigt varningskort om båda riktningar är aktiva. Detta synkroniserar gränssnittets varningskort med poängmotorns avdrag. Dessutom lades defensiva kontroller till för att förhindra type-errors om regel-id:n saknas.</motivering>
</record>

<record id="DEC-019" kategori="Varumärke och UI">
  <beslut>Byta namn på applikationens frontend från Psykometrisk Relationsanalysator till Relia samt integrera den nya logotypen "Safe Haven" (Koncept 3) som en interaktiv och responsiv SVG i dashboard-headern.</beslut>
  <kärna>Rebranding till Relia och integration av interaktiv logotyp</kärna>
  <motivering>Det nya namnet Relia valdes för att underlätta framtida kommersiell skalning på App Store/Google Play genom att erbjuda ett mjukare, kortare och mer wellness-orienterat namn utan religiösa associationer. Logotypen (Safe Haven) visualiserar en trygg bas (en vagga som håller en svävande part) och stämmer överens med anknytningsteorins principer. Subtila CSS-hover-animationer har lagts till som mjukt vaggar logotypen för att förstärka premiumkänslan i Calm Sanctuary-temat.</motivering>
</record>

<record id="DEC-020" kategori="Felsökning">
  <beslut>Strama upp defensiva guards med typ-kontroll samt åtgärda skiljetecken i genererade krocktexter.</beslut>
  <kärna>Typkontroll i guards och borttagning av dubbla punkter i text</kärna>
  <motivering>Genomförde finjusteringar efter den andra audit-granskningen. Uppdaterade filterlogiken till typeof theme !== 'string' istället för enbart sanningstest (!theme) för att förhindra fatala javascript-krascher på .endsWith() om ett id skulle vara ett tal. Dessutom lades en .replace-trimning till för att ta bort avslutande punkter från beskrivningar i traits.json före sammanslagning med texten ", och vice versa", vilket förhindrar dubbla punkter i gränssnittet.</motivering>
</record>


<record id="DEC-021" kategori="Utveckling">
  <beslut>Implementera dynamisk tab-namngivning för prompt-generatorns knappar baserat på användarinmatning, integrera en klinisk hybrid-tipsruta för kontextförfining, samt lägga till exakta och stoppsäkra följdfrågor i de genererade prompterna.</beslut>
  <kärna>Dynamisk prompt-UX och interaktiva AI-följdfrågor</kärna>
  <motivering>Löser problemet med tråkiga standardnamn på promptknapparna genom att styra textContent i updateNames(). Tipsrutan kombinerar nu instruktioner om AI-frågor med förslag på hur användaren kan addera egen kontext (särbo, livsfas). Promptarna har utrustats med strikta stopp-regler ("exakt 3 följdfrågor under separat rubrik", "Skriv ingenting efter frågorna") för att garantera att AI:n väntar på svar utan att hallucinera.</motivering>
</record>

<record id="DEC-022" kategori="UI/Layout">
  <beslut>Implementera utskriftsstilar (@media print) anpassade för A4-porträtt och PDF-export, samt tillämpa display: block-bypass för WebKit-motorns fragmentationsbugg på grid- och flexkort.</beslut>
  <kärna>Utskriftsstilar, döljning av gränssnittsbrus och Chromium page-break-bypass</kärna>
  <motivering>Löser problemet med att utskrifter/PDF:er ser trasiga ut genom att dölja interaktivt brus (AI-kort, modal, knappar, status-badges) och placera profilkort A och B sida vid sida i två rena kolumner. Genom att dölja .visualizer-card slipper vi dessutom trasiga koordinatlinjer från SVG. För att kringgå Chrome/Edges fragmentationsbugg (där break-inside: avoid ignoreras i flex/grid) konverteras layouten till display: block inuti column-count: 2 vid utskrift.</motivering>
</record>
