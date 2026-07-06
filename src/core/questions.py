# -*- coding: utf-8 -*-

QUESTIONS = {
    "attachment": [
        {
            "id": "att_1",
            "text": "Hur reagerar du oftast när din partner inte svarar på meddelanden under en längre tid?",
            "options": [
                {"text": "A) Jag blir orolig och undrar om jag gjort något fel.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Jag tänker inte så mycket på det, jag är upptagen med mitt.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag känner mig stressad men försöker verka oberörd.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Jag känner mig trygg med att partnern svarar när hen har tid.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_2",
            "text": "Hur ser du på att dela dina djupaste rädslor och känslor med din partner?",
            "options": [
                {"text": "A) Jag vill göra det omedelbart men är rädd att skrämma iväg partnern.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Jag föredrar att hålla mina djupaste känslor för mig själv.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag vill dela dem, men jag har svårt att lita på att partnern inte använder det mot mig.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Det känns naturligt och tryggt att dela mina tankar och känslor.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_3",
            "text": "När din partner söker närhet och intimitet, hur reagerar du?",
            "options": [
                {"text": "A) Jag blir jätteglad och vill ha ännu mer närhet.", "impact": {"anxiety": 0.1, "avoidance": 0.0}},
                {"text": "B) Jag känner mig ibland trängd och vill ta ett steg tillbaka.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag vill ha närhet men är rädd att den plötsligt ska dras undan.", "impact": {"anxiety": 0.2, "avoidance": 0.1}},
                {"text": "D) Jag uppskattar det och besvarar närheten på ett avslappnat sätt.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_4",
            "text": "Oroar du dig ofta för att din partner ska sluta älska dig?",
            "options": [
                {"text": "A) Ja, det är en ständigt återkommande rädsla.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Nej, jag oroar mig sällan för sådant.", "impact": {"anxiety": 0.0, "avoidance": 0.0}},
                {"text": "C) Jag oroar mig, men döljer det genom att låtsas vara oberoende.", "impact": {"anxiety": 0.1, "avoidance": 0.2}},
                {"text": "D) Nej, jag känner mig trygg i relationens stabilitet.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_5",
            "text": "När en konflikt uppstår, vad är din omedelbara impuls?",
            "options": [
                {"text": "A) Jag vill prata ut omedelbart och lösa det direkt.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Jag vill gå undan och få vara i fred för att lugna mig.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag blir defensiv och drar mig undan fast jag kokar inombords.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Jag försöker boka en tid för att prata lugnt när båda har landat.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_6",
            "text": "Hur ser du på självständighet i relationen?",
            "options": [
                {"text": "A) Jag är rädd att för mycket självständighet ska leda till att vi glider isär.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Självständighet är absolut nödvändigt för att jag ska kunna andas.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag vill ha självständighet men är rädd att partnern lämnar mig om jag tar utrymme.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Jag tycker självständighet och samhörighet kan balanseras väl.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_7",
            "text": "Hur reagerar du om din partner föreslår att resa ensam med vänner?",
            "options": [
                {"text": "A) Jag känner mig hotad och övergiven, fast jag kanske säger ja.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Jag tycker det är skönt, då får jag tid för mig själv.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag blir misstänksam och drar mig undan emotionellt.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Det är helt okej, jag unnar partnern att ha kul.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_8",
            "text": "När du mår dåligt, hur söker du tröst?",
            "options": [
                {"text": "A) Jag vill att min partner ska hålla om mig och bekräfta mig omedelbart.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Jag vill vara helt i fred och lösa mina problem själv.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag vill ha tröst men drar mig undan för att se om partnern söker upp mig.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Jag berättar vad jag behöver och tar gärna emot en kram.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_9",
            "text": "Upplever du ofta att du älskar din partner mer än vad hen älskar dig?",
            "options": [
                {"text": "A) Ja, det är en vanlig känsla hos mig.", "impact": {"anxiety": 0.2, "avoidance": 0.0}},
                {"text": "B) Nej, snarare tvärtom eller så tänker jag inte på det.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag känner så men döljer det bakom en kylig fasad.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Nej, vi har en balanserad och ömsesidig kärlek.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        },
        {
            "id": "att_10",
            "text": "Hur bekväm är du med att lita på din partner i svåra situationer?",
            "options": [
                {"text": "A) Jag litar på hen, men dubbelkollar ändå för att känna mig trygg.", "impact": {"anxiety": 0.1, "avoidance": 0.0}},
                {"text": "B) Jag litar bara på mig själv när det verkligen gäller.", "impact": {"anxiety": 0.0, "avoidance": 0.2}},
                {"text": "C) Jag vill lita på hen, men är alltid förberedd på att bli besviken.", "impact": {"anxiety": 0.1, "avoidance": 0.1}},
                {"text": "D) Jag känner mig helt trygg med att lita på min partner.", "impact": {"anxiety": 0.0, "avoidance": 0.0}}
            ]
        }
    ],
    "hsp": [
        {
            "id": "hsp_1",
            "text": "Efter en intensiv arbetsdag i en miljö med mycket ljud och rörelse, hur mycket ensamtid behöver du för att återhämta dig?",
            "options": [
                {"text": "A) Ingen speciell, jag får energi av att träffa människor direkt.", "impact": {"threshold": 2.0, "latency": 0.5}},
                {"text": "B) Kanske 1 timme av lugn hemma.", "impact": {"threshold": 1.0, "latency": 1.0}},
                {"text": "C) Minst 2-3 timmar i total tystnad och avskildhet.", "impact": {"threshold": -1.0, "latency": 3.0}},
                {"text": "D) Jag behöver stänga in mig i ett mörkt rum resten av kvällen (4+ timmar).", "impact": {"threshold": -2.0, "latency": 5.0}}
            ]
        },
        {
            "id": "hsp_2",
            "text": "Hur påverkas du av starka sinnesintryck som skarpt ljus, starka dofter eller bakgrundsbuller?",
            "options": [
                {"text": "A) Det stör mig sällan, jag kan lätt koppla bort det.", "impact": {"threshold": 2.0, "latency": 0.0}},
                {"text": "B) Jag märker det men blir inte särskilt stressad.", "impact": {"threshold": 1.0, "latency": 0.5}},
                {"text": "C) Det gör mig snabbt trött och irriterad.", "impact": {"threshold": -1.0, "latency": 1.5}},
                {"text": "D) Det orsakar kognitiv överbelastning och fysiskt obehag ganska snabbt.", "impact": {"threshold": -2.0, "latency": 3.0}}
            ]
        },
        {
            "id": "hsp_3",
            "text": "Hur reagerar du när du har mycket att göra på kort tid och upplever tidspress?",
            "options": [
                {"text": "A) Jag blir stimulerad och jobbar mer effektivt.", "impact": {"threshold": 2.0, "latency": 0.0}},
                {"text": "B) Jag hanterar det okej, men gillar det inte.", "impact": {"threshold": 0.5, "latency": 0.5}},
                {"text": "C) Jag känner mig skakad och min kognitiva förmåga sjunker drastiskt.", "impact": {"threshold": -1.0, "latency": 2.0}},
                {"text": "D) Jag blir helt blockerad och behöver dra mig undan omedelbart.", "impact": {"threshold": -2.0, "latency": 4.0}}
            ]
        },
        {
            "id": "hsp_4",
            "text": "Hur djupt påverkas du av andras stämningar eller stämningen i ett rum?",
            "options": [
                {"text": "A) Inte mycket, jag påverkas bara av mitt eget mående.", "impact": {"threshold": 1.0, "latency": 0.0}},
                {"text": "B) Jag kan känna av det men låter det inte styra mig.", "impact": {"threshold": 0.5, "latency": 0.5}},
                {"text": "C) Jag suger åt mig stämningar som en svamp och blir dränerad om de är negativa.", "impact": {"threshold": -1.0, "latency": 2.5}},
                {"text": "D) Det är så överväldigande att jag fysiskt måste lämna rummet.", "impact": {"threshold": -2.0, "latency": 4.5}}
            ]
        },
        {
            "id": "hsp_5",
            "text": "Hur reagerar du på konst, musik eller vackra miljöer?",
            "options": [
                {"text": "A) Trevligt, men inget som påverkar mig på djupet.", "impact": {"threshold": 0.0, "latency": 0.0}},
                {"text": "B) Jag uppskattar det och blir på gott humör.", "impact": {"threshold": 0.0, "latency": 0.0}},
                {"text": "C) Det kan väcka starka känslor och ge mig djup inspiration.", "impact": {"threshold": 0.0, "latency": 0.5}},
                {"text": "D) Jag upplever en nästan transcendent/fysisk reaktion av djup skönhet.", "impact": {"threshold": 0.0, "latency": 1.0}}
            ]
        },
        {
            "id": "hsp_6",
            "text": "När du blir överstimulerad, vad är ditt primära behov?",
            "options": [
                {"text": "A) Jag vill distrahera mig genom att göra något kul eller prata med någon.", "impact": {"threshold": 1.5, "latency": 0.0}},
                {"text": "B) Jag vill vila en stund framför TV:n eller läsa.", "impact": {"threshold": 0.5, "latency": 1.0}},
                {"text": "C) Jag behöver total tystnad och att ingen pratar med mig under några timmar.", "impact": {"threshold": -1.0, "latency": 3.0}},
                {"text": "D) Jag måste ligga i ett släckt rum utan några intryck alls.", "impact": {"threshold": -2.0, "latency": 5.0}}
            ]
        },
        {
            "id": "hsp_7",
            "text": "Hur känslig är du för koffein, hunger eller fysisk smärta?",
            "options": [
                {"text": "A) Inte särskilt, jag kan ignorera hunger eller smärta ganska bra.", "impact": {"threshold": 1.0, "latency": 0.0}},
                {"text": "B) Som folk är mest.", "impact": {"threshold": 0.0, "latency": 0.5}},
                {"text": "C) Väldigt känslig; om jag är hungrig blir jag helt dysfunktionell.", "impact": {"threshold": -1.0, "latency": 1.5}},
                {"text": "D) Extremt känslig; fysiska obehag tar över hela mitt medvetande direkt.", "impact": {"threshold": -2.0, "latency": 3.0}}
            ]
        },
        {
            "id": "hsp_8",
            "text": "Försöker du aktivt strukturera ditt liv för att undvika överväldigande situationer?",
            "options": [
                {"text": "A) Nej, jag tar saker som de kommer och gillar fart.", "impact": {"threshold": 2.0, "latency": 0.0}},
                {"text": "B) Ibland, men jag begränsar mig inte.", "impact": {"threshold": 0.5, "latency": 0.5}},
                {"text": "C) Ja, jag planerar noga mina sociala aktiviteter med återhämtningsdagar emellan.", "impact": {"threshold": -1.0, "latency": 2.5}},
                {"text": "D) Ja, mitt liv är hårt strukturerat för att undvika kaos och stimulansöverskott.", "impact": {"threshold": -2.0, "latency": 4.0}}
            ]
        },
        {
            "id": "hsp_9",
            "text": "Upplever du att du har ett rikt och komplext inre liv?",
            "options": [
                {"text": "A) Nej, jag lever i nuet och tänker inte så djupt på mitt inre.", "impact": {"threshold": 0.5, "latency": 0.0}},
                {"text": "B) Ja, jag har mina tankar men inget märkvärdigt.", "impact": {"threshold": 0.0, "latency": 0.5}},
                {"text": "C) Ja, jag analyserar mycket och drömmer livfullt.", "impact": {"threshold": -0.5, "latency": 1.5}},
                {"text": "D) Ja, mitt inre liv är extremt djupt, reflekterande och ständigt aktivt.", "impact": {"threshold": -1.0, "latency": 3.0}}
            ]
        },
        {
            "id": "hsp_10",
            "text": "Hur reagerar du på förändringar i din livssituation eller miljö?",
            "options": [
                {"text": "A) Jag älskar förändring, det ger mig spänning.", "impact": {"threshold": 2.0, "latency": 0.0}},
                {"text": "B) Jag anpassar mig snabbt och enkelt.", "impact": {"threshold": 1.0, "latency": 0.5}},
                {"text": "C) Det tar tid för mig att ställa om och jag känner mig stressad under tiden.", "impact": {"threshold": -1.0, "latency": 2.0}},
                {"text": "D) Även små förändringar skakar om min grundtrygghet och kräver stor återhämtning.", "impact": {"threshold": -2.0, "latency": 4.0}}
            ]
        }
    ],
    "gottman": [
        {
            "id": "got_1",
            "text": "När du tar upp ett problem med din partner, hur formulerar du dig oftast?",
            "options": [
                {"text": "A) Jag påpekar vad partnern gör för fel i allmänhet ('Du glömmer alltid...').", "impact": {"flags": ["Kritik"], "stress": "hyperactivation"}},
                {"text": "B) Jag uttrycker mina egna känslor och behov ('Jag känner mig stressad när det är stökigt').", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Jag använder ironi, sarkasm eller suckar för att visa mitt missnöje.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "D) Jag säger ingenting, det är ingen idé ändå.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_2",
            "text": "När din partner kritiserar dig för något, vad gör du då?",
            "options": [
                {"text": "A) Jag slår tillbaka direkt med partnerns egna fel ('Det säger du som aldrig...').", "impact": {"flags": ["Defensivitet"], "stress": "hyperactivation"}},
                {"text": "B) Jag lyssnar och försöker hitta den del av kritiken som jag kan ta ansvar för.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Jag himlar med ögonen och förklarar hur löjlig kritiken är.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "D) Jag stänger av, undviker ögonkontakt och svarar inte.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_3",
            "text": "När ett gräl blir för intensivt och dina känslor stormar, hur agerar du?",
            "options": [
                {"text": "A) Jag fortsätter argumentera och kräver att vi pratar färdigt NU.", "impact": {"flags": [], "stress": "hyperactivation"}},
                {"text": "B) Jag föreslår en paus på 20 minuter för att lugna ner oss.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Jag lämnar rummet i ilska eller sätter på mig hörlurar och ignorerar partnern helt.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}},
                {"text": "D) Jag blir cynisk och förklarar hur hopplös vår relation är.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_4",
            "text": "Brukar du känna att du är den mogna eller moraliskt överlägsna i relationen?",
            "options": [
                {"text": "A) Ja, jag känner ofta att jag bär det vuxna ansvaret medan partnern är barnslig.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "B) Nej, vi är två jämbördiga partners med olika brister.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Jag känner mig underlägsen och kritiserad hela tiden.", "impact": {"flags": ["Defensivitet"], "stress": "hyperactivation"}},
                {"text": "D) Jag har gett upp att jämföra, jag bryr mig bara inte längre.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_5",
            "text": "När partnern ber om ursäkt efter en konflikt, hur reagerar du?",
            "options": [
                {"text": "A) Jag accepterar ursäkten, men lägger till en pik om vad hen måste ändra på.", "impact": {"flags": ["Kritik"], "stress": "hyperactivation"}},
                {"text": "B) Jag tar emot den, förlåter och vi försöker mötas.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Jag avfärdar ursäkten som falsk eller otillräcklig.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "D) Jag låtsas inte höra eller ger ett kallt 'okej' utan att titta upp.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_6",
            "text": "Hur ofta upplever du att du eller din partner går i försvarsställning under ett samtal?",
            "options": [
                {"text": "A) Väldigt ofta, nästan varje diskussion blir en försvarsstrid.", "impact": {"flags": ["Defensivitet"], "stress": "hyperactivation"}},
                {"text": "B) Sällan, vi kan oftast prata utan att skydda oss.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Partnern går alltid i försvar, så jag måste tala om för hen hur fel det är.", "impact": {"flags": ["Kritik"], "stress": "hyperactivation"}},
                {"text": "D) Det spelar ingen roll, jag försvarar mig inte ens längre, jag bara håller med tyst.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_7",
            "text": "När din partner uttrycker sorg eller besvikelse, vad känner du då?",
            "options": [
                {"text": "A) Jag känner skuld och vill fixa det direkt genom att förklara mitt agerande.", "impact": {"flags": ["Defensivitet"], "stress": "hyperactivation"}},
                {"text": "B) Jag känner empati och vill lyssna på hens upplevelse.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Jag känner irritation över hens känslighet eller drama.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "D) Jag känner mig avstängd och tom, vill bara slippa höra på det.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_8",
            "text": "Använder du personangrepp under konflikter?",
            "options": [
                {"text": "A) Ja, ibland slinker det ut elaka kommentarer om partnerns personlighet.", "impact": {"flags": ["Kritik"], "stress": "hyperactivation"}},
                {"text": "B) Nej, jag försöker hålla mig strikt till den specifika saken.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Ja, jag förlöjligar hens brister eller härmar hen sarkastiskt.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "D) Nej, jag säger ingenting elakt, jag säger överhuvudtaget ingenting.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_9",
            "text": "Hur löser ni oftast konflikter?",
            "options": [
                {"text": "A) Vi diskuterar högljutt tills en vinner eller båda blir utmattade.", "impact": {"flags": ["Defensivitet"], "stress": "hyperactivation"}},
                {"text": "B) Vi pratar, lyssnar, kompromissar och känner oss oftast hörda.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Det blir oftast kallt krig och tystnad i flera dagar.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}},
                {"text": "D) Den ena parten ger upp helt och hållet för att undvika bråk.", "impact": {"flags": [], "stress": "deactivation"}}
            ]
        },
        {
            "id": "got_10",
            "text": "Känner du att din partner respekterar dina åsikter även när ni tycker olika?",
            "options": [
                {"text": "A) Ibland, men hen försöker nästan alltid bevisa att jag har fel.", "impact": {"flags": ["Kritik"], "stress": "hyperactivation"}},
                {"text": "B) Ja, jag känner mig respekterad och lyssnad på.", "impact": {"flags": [], "stress": "secure"}},
                {"text": "C) Nej, hen visar öppet förakt för mina åsikter.", "impact": {"flags": ["Förakt"], "stress": "deactivation"}},
                {"text": "D) Jag vet inte, vi pratar aldrig om djupare saker.", "impact": {"flags": ["Stonewalling"], "stress": "deactivation"}}
            ]
        }
    ],
    "tki": [
        {
            "id": "tki_1",
            "text": "När en intressekonflikt uppstår gällande resurser eller tid, vad prioriterar du?",
            "options": [
                {"text": "A) Att jag får min vilja igenom, jag backar inte.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Att vi hittar en lösning som gör båda helt nöjda, även om det tar tid.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Att vi båda möts halvvägs och ger upp lite av våra krav.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Att vi skjuter upp beslutet eller undviker att prata om det.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Att min partner blir nöjd, jag kan anpassa mig efter hens önskemål.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_2",
            "text": "Hur brukar du hantera att partnern vill göra något du absolut inte vill göra?",
            "options": [
                {"text": "A) Jag förklarar bestämt varför det inte går och står på mig.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Vi sätter oss ner och diskuterar tills vi hittar ett tredje alternativ som passar båda.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Vi gör det denna gång om jag får bestämma nästa gång.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Jag låtsas som ingenting och hoppas att partnern glömmer bort det.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Jag ger efter och gör det för att hålla stämningen god.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_3",
            "text": "När diskussionen hettar till gällande semesterplaneringen, vad är ditt fokus?",
            "options": [
                {"text": "A) Att vinna diskussionen med bra argument.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Att förstå partnerns perspektiv fullt ut och bygga en gemensam drömresa.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Att dela upp dagarna så att vi gör hälften av mitt och hälften av hens.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Att strunta i att planera helt och hållet och stanna hemma.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Att låta partnern planera allt, jag följer bara med.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_4",
            "text": "När du vet att du har rätt i en sakfråga, hur agerar du?",
            "options": [
                {"text": "A) Jag insisterar tills partnern håller med mig.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Jag visar mina källor och bjuder in till en djupare gemensam diskussion.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Jag föreslår att vi 'enats om att tycka olika' och släpper det.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Jag håller tyst för att inte starta ett onödigt gräl.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Jag låter partnern tro att hen har rätt för att slippa tjafs.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_5",
            "text": "När det uppstår ett missförstånd kring hushållssysslor, hur hanterar du det?",
            "options": [
                {"text": "A) Jag blir arg och kräver att partnern gör sin del omedelbart.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Vi gör ett schema tillsammans där vi kartlägger allas önskemål och tider.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Vi delar upp sysslorna 50/50 rakt av utan diskussion.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Jag låter disken stå och låtsas inte se den.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Jag gör allt själv för att slippa be partnern eller tjata.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_6",
            "text": "Om din partner är mycket upprörd över något du gjort, vad gör du?",
            "options": [
                {"text": "A) Jag förklarar varför mitt agerande var logiskt och försvarar min position.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Jag bjuder in till ett samtal för att förstå hens ilska och hitta en lösning.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Jag föreslår en snabb kompromiss för att lugna ner situationen.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Jag drar mig undan och väntar tills hen har lugnat ner sig.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Jag ber om ursäkt direkt och gör vad som helst för att göra hen nöjd igen.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_7",
            "text": "Hur ser du generellt på konflikter i en relation?",
            "options": [
                {"text": "A) Det är en kamp som man måste vinna för att inte bli överkörd.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Det är en möjlighet att lära känna varandra djupare och utvecklas ihop.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Det är ett nödvändigt ont som bäst löses genom att ge och ta.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Det är skadligt och bör undvikas så långt det går.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Det är bäst att bara hålla med så att harmonin bevaras.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_8",
            "text": "När ni fattar stora ekonomiska beslut, hur gör ni då?",
            "options": [
                {"text": "A) Jag fattar besluten själv eftersom jag har bäst koll.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Vi gör en komplett analys av bådas ekonomi och skapar en gemensam långsiktig plan.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Vi delar kostnaderna rakt av eller kompromissar om vad vi har råd med.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Vi skjuter upp beslutet och låtsas som att ekonomin löser sig själv.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Jag låter partnern bestämma hur vi ska spendera eller spara.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_9",
            "text": "När ni ska bestämma vad ni ska äta till middag, hur slutar det oftast?",
            "options": [
                {"text": "A) Vi äter det jag är sugen på, jag är väldigt bestämd.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Vi lagar något nytt spännande som båda vill prova tillsammans.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Vi kompromissar (t.ex. köper hämtmat från två olika ställen).", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Ingen orkar bestämma, så vi struntar i det eller äter rester själva.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Vi äter det min partner vill ha, det spelar ingen roll för mig.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        },
        {
            "id": "tki_10",
            "text": "Om ni är oense om fostran av era husdjur (eller barn), vad gör du?",
            "options": [
                {"text": "A) Jag kör min linje när jag har hand om dem, oavsett vad partnern tycker.", "impact": {"competing": 2, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "B) Vi pratar igenom vår filosofi grundligt för att enas om gemensamma regler.", "impact": {"competing": 0, "collaborating": 2, "compromising": 0, "avoiding": 0, "accommodating": 0}},
                {"text": "C) Vi hittar en medelväg där båda får ge med sig på vissa punkter.", "impact": {"competing": 0, "collaborating": 0, "compromising": 2, "avoiding": 0, "accommodating": 0}},
                {"text": "D) Jag låter partnern sköta allt och lägger mig inte i regelfrågor.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 2, "accommodating": 0}},
                {"text": "E) Jag följer partnerns regler helt och hållet för att det ska bli konsekvent.", "impact": {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 2}}
            ]
        }
    ]
}
