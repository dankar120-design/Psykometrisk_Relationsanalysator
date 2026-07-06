# -*- coding: utf-8 -*-
import os
import sys
import json
import time
import base64
import hashlib
import re
from datetime import datetime

# Importera kärnfunktioner
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.questions import QUESTIONS
from core.psychometrics import run_analysis, load_json, save_json_atomic

# Färgkoder för Retro-estetik (Amber/Green/Red)
AMBER = "\033[38;5;214m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"
CLEAR = "\033[H\033[2J"

STATE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/relation_state.json'))
TRAITS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/traits.json'))


def safe_run_analysis(state_path, traits_path):
    try:
        return run_analysis(state_path, traits_path)
    except Exception as e:
        print(f"\n{RED}⚠ SYSTEM VARNING: Det gick inte att köra analysen.{RESET}")
        print(f"{RED}  Orsak: {e}{RESET}")
        print(f"{AMBER}  Laddar om med fallback-data...{RESET}")
        time.sleep(2)
        return False

def clear_screen():
    print(CLEAR, end="")

def print_header(title):
    print(f"{AMBER}========================================================================")
    print(f"  {title.upper()}")
    print(f"========================================================================{RESET}\n")

def load_state_with_fallback():
    try:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception:
        # Fallback till backup
        bak_file = STATE_FILE + ".bak"
        if os.path.exists(bak_file):
            try:
                with open(bak_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"{RED}⚠ SYSTEM VARNING: State-fil korrupt. Laddade reservkopia.{RESET}")
                time.sleep(2)
                return data
            except Exception:
                pass
                
    # Skapa en ny om allt misslyckas
    print(f"{RED}⚠ CRITICAL ERROR: System-state korrupt eller saknas. Initierar nytt.{RESET}")
    time.sleep(2)
    return {
        "system_meta": {
            "iteration": 1,
            "last_updated": datetime.now().isoformat(),
            "questionnaire_progress": {
                "current_subject": "D",
                "current_module": "attachment",
                "current_question_index": 0,
                "completed_modules": []
            }
        },
        "subjects": {
            "D": {
                "attachment_profile": {
                    "anxiety_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                    "avoidance_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                    "stress_response": { "computed": None, "override": None, "override_reason": None, "effective": None }
                },
                "sensory_processing": {
                    "overload_threshold_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                    "recovery_latency_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 }
                },
                "conflict_mechanisms": {
                    "primary_tki": { "computed": None, "override": None, "override_reason": None, "effective": None },
                    "gottman_flags": { "computed": [], "override": None, "override_reason": None, "effective": [] }
                },
                "identified_traits": [],
                "interview_notes": {}
            },
            "E": {
                "attachment_profile": {
                    "anxiety_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                    "avoidance_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                    "stress_response": { "computed": None, "override": None, "override_reason": None, "effective": None }
                },
                "sensory_processing": {
                    "overload_threshold_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                    "recovery_latency_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 }
                },
                "conflict_mechanisms": {
                    "primary_tki": { "computed": None, "override": None, "override_reason": None, "effective": None },
                    "gottman_flags": { "computed": [], "override": None, "override_reason": None, "effective": [] }
                },
                "identified_traits": [],
                "interview_notes": {}
            }
        },
        "compatibility_matrix": {
            "critical_warnings": [],
            "attraction_factors": [],
            "logistical_sync": 0.0,
            "mind_map": {
                "connections": []
            }
        }
    }

def run_questionnaire():
    state = load_state_with_fallback()
    progress = state["system_meta"]["questionnaire_progress"]
    
    # Om testet redan är helt klart
    if progress["current_subject"] is None:
        clear_screen()
        print_header("Frågebatteri slutfört")
        print(f"{GREEN}Alla psykometriska moduler har redan genomförts för både D och E.{RESET}")
        choice = input(f"\n{AMBER}Vill du göra om testet från början? (J/N): {RESET}").strip().upper()
        if choice == 'J':
            progress = {
                "current_subject": "D",
                "current_module": "attachment",
                "current_question_index": 0,
                "completed_modules": []
            }
            state["system_meta"]["questionnaire_progress"] = progress
            save_json_atomic(STATE_FILE, state)
        else:
            return

    # Loopa igenom D och E, moduler och frågor
    subjects_order = ["D", "E"]
    modules_order = ["attachment", "hsp", "gottman", "tki"]
    
    # Hitta var vi ska börja
    sub_idx = subjects_order.index(progress["current_subject"])
    mod_idx = modules_order.index(progress["current_module"])
    q_idx = progress["current_question_index"]
    
    # Temporär lagring av valda svar under sessionen för poängberäkning
    # Vi kan räkna poäng dynamiskt i slutet av varje modul
    while sub_idx < len(subjects_order):
        subject = subjects_order[sub_idx]
        progress["current_subject"] = subject
        
        while mod_idx < len(modules_order):
            module = modules_order[mod_idx]
            progress["current_module"] = module
            
            questions_list = QUESTIONS[module]
            
            # Initiera tillfällig poängsamlare i state för att inte förlora data vid avbrott
            session_key = f"temp_answers_{subject}_{module}"
            if session_key not in state["system_meta"]:
                state["system_meta"][session_key] = []
            
            while q_idx < len(questions_list):
                progress["current_question_index"] = q_idx
                save_json_atomic(STATE_FILE, state)
                
                q = questions_list[q_idx]
                
                clear_screen()
                print_header(f"Modul: {module.upper()} | Subjekt: {subject} | Fråga {q_idx + 1}/{len(questions_list)}")
                
                print(f"{AMBER}{q['text']}{RESET}\n")
                for opt in q["options"]:
                    print(f"  {opt['text']}")
                print()
                
                # Validera inmatning
                valid_answers = [opt["text"][0] for opt in q["options"]] # A, B, C...
                ans = ""
                while ans not in valid_answers:
                    ans = input(f"{AMBER}Mata in ditt val ({'/'.join(valid_answers)}): {RESET}").strip().upper()
                
                # Hämta den valda optionen
                selected_opt = [opt for opt in q["options"] if opt["text"].startswith(ans)][0]
                
                # Spara svaret
                state["system_meta"][session_key].append({
                    "question_id": q["id"],
                    "answer": ans,
                    "impact": selected_opt["impact"]
                })
                
                q_idx += 1
                state["system_meta"]["questionnaire_progress"]["current_question_index"] = q_idx
                save_json_atomic(STATE_FILE, state)
                
            # Beräkna och spara modulens computed data
            answers = state["system_meta"][session_key]
            sub_ref = state["subjects"][subject]
            
            if module == "attachment":
                tot_anx = sum(a["impact"]["anxiety"] for a in answers)
                tot_av = sum(a["impact"]["avoidance"] for a in answers)
                # Beräkna maxpoäng dynamiskt
                max_anx = sum(max(opt["impact"]["anxiety"] for opt in mq["options"]) for mq in QUESTIONS["attachment"])
                max_av = sum(max(opt["impact"]["avoidance"] for opt in mq["options"]) for mq in QUESTIONS["attachment"])
                sub_ref["attachment_profile"]["anxiety_score"]["computed"] = round(tot_anx / max_anx, 2) if max_anx > 0 else 0.0
                sub_ref["attachment_profile"]["avoidance_score"]["computed"] = round(tot_av / max_av, 2) if max_av > 0 else 0.0
                
            elif module == "hsp":
                tot_thresh = 8.0 + sum(a["impact"]["threshold"] for a in answers) # Börjar på 8 timmar
                tot_lat = sum(a["impact"]["latency"] for a in answers)
                sub_ref["sensory_processing"]["overload_threshold_hrs"]["computed"] = max(1.0, min(12.0, round(tot_thresh, 1)))
                sub_ref["sensory_processing"]["recovery_latency_hrs"]["computed"] = max(0.0, min(12.0, round(tot_lat, 1)))
                
            elif module == "gottman":
                flags = []
                stress_counts = {"hyperactivation": 0, "deactivation": 0, "secure": 0}
                for a in answers:
                    flags.extend(a["impact"].get("flags", []))
                    stress = a["impact"].get("stress")
                    if stress:
                        stress_counts[stress] += 1
                
                # Unika flaggor som dyker upp mer än 1 gång
                unique_flags = list(set([f for f in flags if flags.count(f) >= 2]))
                sub_ref["conflict_mechanisms"]["gottman_flags"]["computed"] = unique_flags
                
                # Stressrespons (max count)
                primary_stress = max(stress_counts, key=stress_counts.get)
                sub_ref["attachment_profile"]["stress_response"]["computed"] = primary_stress
                
            elif module == "tki":
                tki_scores = {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}
                for a in answers:
                    for key in tki_scores:
                        tki_scores[key] += a["impact"].get(key, 0)
                
                # Hämta den med högst poäng
                primary_tki = max(tki_scores, key=tki_scores.get).capitalize()
                sub_ref["conflict_mechanisms"]["primary_tki"]["computed"] = primary_tki
            
            # Ta bort temporära svar från state
            state["system_meta"].pop(session_key, None)
            progress["completed_modules"].append(module)
            
            # Gå till nästa modul
            mod_idx += 1
            q_idx = 0
            progress["current_module"] = modules_order[mod_idx] if mod_idx < len(modules_order) else "attachment"
            progress["current_question_index"] = 0
            save_json_atomic(STATE_FILE, state)
            
        # Gå till nästa person
        sub_idx += 1
        mod_idx = 0
        progress["current_subject"] = subjects_order[sub_idx] if sub_idx < len(subjects_order) else None
        save_json_atomic(STATE_FILE, state)

    # Kör den regelbaserade utvärderingsmotorn
    safe_run_analysis(STATE_FILE, TRAITS_FILE)
    
    clear_screen()
    print_header("Testet är Slutfört!")
    print(f"{GREEN}Relationsanalys mot traits.json har exekverats framgångsrikt.{RESET}")
    print(f"{AMBER}Du kan nu öppna dashboarden för att studera resultaten.{RESET}")
    input("\nTryck [Enter] för att återgå till huvudmenyn...")

def show_dashboard():
    while True:
        # Kör analysen först för att ladda eventuella färska overrides eller ändringar
        safe_run_analysis(STATE_FILE, TRAITS_FILE)
        
        state = load_state_with_fallback()
        subjects = state["subjects"]
        matrix = state["compatibility_matrix"]
        
        clear_screen()
        print_header("Relations-Dashboard")
        
        # Logistisk synkronisering (Kompatibilitetspoäng)
        sync = matrix["logistical_sync"]
        sync_color = GREEN if sync >= 70 else (AMBER if sync >= 40 else RED)
        print(f"  LOGISTISK SYNKRONISERING: {sync_color}{sync}%{RESET}\n")
        
        # D:s Profil
        print(f"{AMBER}--- SUBJEKT D ---{RESET}")
        print_subject_summary(subjects["D"])
        print()
        
        # E:s Profil
        print(f"{AMBER}--- SUBJEKT E ---{RESET}")
        print_subject_summary(subjects["E"])
        print()
        
        # Krockar och dragningskrafter
        print(f"{AMBER}--- RELATIONSANALYSE (ASYNKRONA SAMBAND) ---{RESET}")
        
        if matrix["critical_warnings"]:
            print(f"  {RED}⚠ KRITISKA KROCKAR:{RESET}")
            for warn in matrix["critical_warnings"]:
                print(f"    - {warn}")
        else:
            print(f"  {GREEN}✔ Inga kritiska krockar detekterade.{RESET}")
            
        if matrix["attraction_factors"]:
            print(f"\n  {GREEN}♥ DRAGNINGSKRAFTER:{RESET}")
            for attr in matrix["attraction_factors"]:
                print(f"    - {attr}")
        print()
        
        # Mind Map / Connections Visualisering
        print(f"{AMBER}--- RELATIONSGRAF (MIND MAP) ---{RESET}")
        connections = matrix.get("mind_map", {}).get("connections", [])
        if connections:
            for conn in connections:
                arrow = f"{RED}◄──[KROCK]──►{RESET}" if conn["edge_type"] == "collision" else f"{GREEN}◄──[SYNK]──►{RESET}"
                print(f"  {conn['source_node']} {arrow} {conn['target_node']}")
                print(f"    {conn['description']}")
        else:
            print("  Inga kopplingar genererade. Genomför testet först.")
        print()
        
        print(f"{AMBER}────────────────────────────────────────────────────────────────────────{RESET}")
        print(f"  [R] Ladda om dashboard (vid AG-justeringar) | [M] Huvudmeny")
        print(f"{AMBER}────────────────────────────────────────────────────────────────────────{RESET}")
        
        choice = input(f"{AMBER}Val: {RESET}").strip().upper()
        if choice == 'M':
            break
        elif choice == 'R':
            print("Laddar om...")
            time.sleep(0.5)

def print_subject_summary(sub):
    traits = ", ".join(sub["identified_traits"]) if sub["identified_traits"] else "Inga drag identifierade"
    print(f"  Identifierade drag: {GREEN}{traits}{RESET}")
    
    ap = sub["attachment_profile"]
    print(f"  Anknytning: Ångest {GREEN}{ap['anxiety_score']['effective']}{RESET} | Undvikande {GREEN}{ap['avoidance_score']['effective']}{RESET} | Stressrespons: {GREEN}{ap['stress_response']['effective']}{RESET}")
    
    sp = sub["sensory_processing"]
    print(f"  Sensorik: Gräns {GREEN}{sp['overload_threshold_hrs']['effective']}h{RESET} | Återhämtning {GREEN}{sp['recovery_latency_hrs']['effective']}h{RESET}")
    
    cm = sub["conflict_mechanisms"]
    flags = ", ".join(cm["gottman_flags"]["effective"]) if cm["gottman_flags"]["effective"] else "Inga"
    print(f"  Mekanismer: TKI {GREEN}{cm['primary_tki']['effective']}{RESET} | Gottman-ryttare: {RED}{flags}{RESET}")
    
    if sub.get("interview_notes"):
        print(f"  {AMBER}Djupintervju anteckningar:{RESET}")
        for k, v in sub["interview_notes"].items():
            print(f"    - {k}: {v}")

def reset_all_data():
    clear_screen()
    print_header("Återställ all data")
    print(f"{RED}⚠ VARNING: Detta kommer att helt återställa relation_state.json till ursprungsläget!{RESET}\n")
    choice = input(f"{AMBER}Är du helt säker? (J/N): {RESET}").strip().upper()
    if choice == 'J':
        init_state = {
            "system_meta": {
                "iteration": 1,
                "last_updated": datetime.now().isoformat(),
                "questionnaire_progress": {
                    "current_subject": "D",
                    "current_module": "attachment",
                    "current_question_index": 0,
                    "completed_modules": []
                }
            },
            "subjects": {
                "D": {
                    "attachment_profile": {
                        "anxiety_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                        "avoidance_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                        "stress_response": { "computed": None, "override": None, "override_reason": None, "effective": None }
                    },
                    "sensory_processing": {
                        "overload_threshold_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                        "recovery_latency_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 }
                    },
                    "conflict_mechanisms": {
                        "primary_tki": { "computed": None, "override": None, "override_reason": None, "effective": None },
                        "gottman_flags": { "computed": [], "override": None, "override_reason": None, "effective": [] }
                    },
                    "identified_traits": [],
                    "interview_notes": {}
                },
                "E": {
                    "attachment_profile": {
                        "anxiety_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                        "avoidance_score": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                        "stress_response": { "computed": None, "override": None, "override_reason": None, "effective": None }
                    },
                    "sensory_processing": {
                        "overload_threshold_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 },
                        "recovery_latency_hrs": { "computed": 0.0, "override": None, "override_reason": None, "effective": 0.0 }
                    },
                    "conflict_mechanisms": {
                        "primary_tki": { "computed": None, "override": None, "override_reason": None, "effective": None },
                        "gottman_flags": { "computed": [], "override": None, "override_reason": None, "effective": [] }
                    },
                    "identified_traits": [],
                    "interview_notes": {}
                }
            },
            "compatibility_matrix": {
                "critical_warnings": [],
                "attraction_factors": [],
                "logistical_sync": 0.0,
                "mind_map": {
                    "connections": []
                }
            }
        }
        save_json_atomic(STATE_FILE, init_state)
        print(f"\n{GREEN}System-state har helt återställts.{RESET}")
        time.sleep(1.5)

def strip_impact(questions_obj):
    """Removes weight/impact fields to prevent users reverse-engineering answers in HTML."""
    stripped = {}
    for module, q_list in questions_obj.items():
        stripped[module] = []
        for q in q_list:
            stripped[module].append({
                "id": q["id"],
                "text": q["text"],
                "options": [{"text": opt["text"]} for opt in q["options"]]
            })
    return stripped

def questionnaire_fingerprint():
    """Generates a deterministic structural fingerprint of the questions database."""
    modules_order = ["attachment", "hsp", "gottman", "tki"]
    signature_parts = []
    for module in modules_order:
        q_list = QUESTIONS.get(module, [])
        options_counts = ",".join(str(len(q["options"])) for q in q_list)
        signature_parts.append(f"{module}:{len(q_list)}:{options_counts}")
    
    canonical_string = "|".join(signature_parts)
    return hashlib.sha256(canonical_string.encode('utf-8')).hexdigest()[:8]

def generate_html_template(subject, fingerprint, questions_obj):
    import json
    q_json = json.dumps(questions_obj).replace("</", "<\\/")
    
    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Psykometrisk Relationsanalysator - Extern Panel ({subject})</title>
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{
            --amber: #ffb000;
            --amber-dim: #cca000;
            --green: #00ff66;
            --green-dim: #00cc55;
            --bg-color: #0d0f0e;
            --terminal-bg: #141816;
            --border-color: #ffb000;
            --text-color: #ffb000;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Share Tech Mono', monospace;
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 15px;
            overflow-x: hidden;
        }}

        body::before {{
            content: " ";
            display: block;
            position: fixed;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            z-index: 9999;
            background-size: 100% 4px, 6px 100%;
            pointer-events: none;
        }}

        .container {{
            width: 100%;
            max-width: 500px;
            background-color: var(--terminal-bg);
            border: 2px solid var(--border-color);
            box-shadow: 0 0 20px rgba(255, 176, 0, 0.15);
            padding: 20px;
            position: relative;
            border-radius: 4px;
        }}

        .header {{
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-align: center;
        }}

        .header h1 {{
            font-size: 1.5rem;
            letter-spacing: 2px;
            text-shadow: 0 0 5px var(--amber);
        }}

        .progress-bar-container {{
            width: 100%;
            height: 10px;
            border: 1px solid var(--border-color);
            margin-top: 10px;
            position: relative;
            background-color: #000;
        }}

        .progress-bar {{
            height: 100%;
            background-color: var(--green);
            box-shadow: 0 0 8px var(--green);
            width: 0%;
            transition: width 0.3s ease;
        }}

        .meta-info {{
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            margin-top: 5px;
            color: var(--green);
        }}

        .screen {{
            display: none;
        }}

        .screen.active {{
            display: block;
            animation: fadeIn 0.4s ease;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .intro-text, .result-text {{
            line-height: 1.6;
            margin-bottom: 20px;
            font-size: 0.95rem;
        }}

        .intro-text span {{
            color: var(--green);
        }}

        .btn {{
            font-family: 'Share Tech Mono', monospace;
            background-color: transparent;
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 12px 20px;
            font-size: 1rem;
            cursor: pointer;
            width: 100%;
            transition: all 0.2s ease;
            text-align: center;
            border-radius: 3px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 10px;
            box-shadow: inset 0 0 5px rgba(255, 176, 0, 0.1);
        }}

        .btn:hover {{
            background-color: var(--amber);
            color: #000;
            box-shadow: 0 0 10px var(--amber);
            font-weight: bold;
        }}

        .btn-green {{
            border-color: var(--green);
            color: var(--green);
        }}

        .btn-green:hover {{
            background-color: var(--green);
            color: #000;
            box-shadow: 0 0 10px var(--green);
        }}

        .question-box {{
            margin-bottom: 20px;
        }}

        .question-text {{
            font-size: 1.1rem;
            line-height: 1.5;
            margin-bottom: 20px;
            color: #fff;
            min-height: 80px;
        }}

        .options-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}

        .option-btn {{
            font-family: 'Share Tech Mono', monospace;
            background-color: rgba(255, 176, 0, 0.03);
            border: 1px solid rgba(255, 176, 0, 0.4);
            color: var(--text-color);
            padding: 14px 18px;
            font-size: 0.95rem;
            text-align: left;
            cursor: pointer;
            border-radius: 4px;
            transition: all 0.15s ease;
            line-height: 1.4;
        }}

        .option-btn:hover {{
            border-color: var(--green);
            color: var(--green);
            background-color: rgba(0, 255, 102, 0.05);
            box-shadow: 0 0 8px rgba(0, 255, 102, 0.1);
            transform: translateX(3px);
        }}

        .option-btn:active {{
            transform: scale(0.98);
        }}

        .hash-display {{
            background-color: #000;
            border: 1px dashed var(--green);
            color: var(--green);
            padding: 15px;
            font-size: 0.9rem;
            word-break: break-all;
            margin: 20px 0;
            border-radius: 4px;
            text-align: center;
            box-shadow: 0 0 10px rgba(0, 255, 102, 0.05);
        }}

        .copied-msg {{
            color: var(--green);
            text-align: center;
            font-size: 0.85rem;
            margin-top: 5px;
            min-height: 20px;
            opacity: 0;
            transition: opacity 0.3s ease;
        }}

        .glitch-text {{
            position: relative;
        }}
        
        .pulse {{
            animation: pulse-animation 2s infinite;
        }}
        
        @keyframes pulse-animation {{
            0% {{ opacity: 0.6; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.6; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1 id="header-title">RELATIONSANALYSATOR</h1>
        <div id="prog-wrapper" style="display: none;">
            <div class="progress-bar-container">
                <div id="progress-bar" class="progress-bar"></div>
            </div>
            <div class="meta-info">
                <span id="progress-text">FRÅGA 1</span>
                <span id="module-text">MODUL: LADDAR</span>
            </div>
        </div>
    </div>

    <!-- SKÄRM 1: INTRO -->
    <div id="screen-intro" class="screen active">
        <div class="intro-text">
            <p>VÄLKOMMEN TILL SYSTEMPANELEN FÖR SUBJEKT {subject}.</p>
            <br>
            <p>Du har blivit inbjuden att delta i en anonym relationsevaluering. Systemet kommer att samla in dina svar på korta frågor fördelade över fyra psykometriska områden:</p>
            <br>
            <p>- Anknytningsteori<br>- Sensorisk känslighet (HSP)<br>- Konfliktmönster (Gottman)<br>- Konflikthanteringsstil (TKI)</p>
            <br>
            <p>Ingen data sparas på internet. Dina svar krypteras till en lokal, anonym teckensträng som du kan skicka tillbaka till din partner.</p>
            <br>
            <p style="font-size:0.75rem; color:var(--amber-dim);">[SYS_FINGERPRINT: {fingerprint}]</p>
        </div>
        <button class="btn btn-green pulse" onclick="startQuestionnaire()">STARTA ANALYS</button>
    </div>

    <!-- SKÄRM 2: FRÅGA -->
    <div id="screen-question" class="screen">
        <div class="question-box">
            <div id="question-text" class="question-text">Laddar fråga...</div>
            <div id="options-list" class="options-list">
                <!-- Genereras dynamiskt -->
            </div>
        </div>
    </div>

    <!-- SKÄRM 3: RESULTAT -->
    <div id="screen-result" class="screen">
        <div class="result-text">
            <p style="color: var(--green); font-size: 1.2rem; text-shadow: 0 0 5px var(--green);">EVALUERING SLUTFÖRD.</p>
            <br>
            <p>Dina svar har framgångsrikt komprimerats till en anonym checksumma. Kopiera koden nedan och skicka den till din partner på Messenger eller SMS.</p>
        </div>
        
        <div id="hash-box" class="hash-display">Genererar checksumma...</div>
        
        <button class="btn btn-green" onclick="copyHash()">KOPIERA CHECKSUMMA</button>
        <div id="copied-notification" class="copied-msg">KOPIERAD TILL URKLIPP!</div>
    </div>
</div>

<script>
    const QUESTIONS_DB = {q_json};
    const FP = "{fingerprint}";
    const SUBJ = "{subject}";
    const modulesOrder = ["attachment", "hsp", "gottman", "tki"];
    
    let currentModuleIndex = 0;
    let currentQuestionIndex = 0;
    let userAnswers = [];
    
    let totalQuestions = 0;
    modulesOrder.forEach(m => totalQuestions += (QUESTIONS_DB[m] ? QUESTIONS_DB[m].length : 0));

    function startQuestionnaire() {{
        document.getElementById("screen-intro").classList.remove("active");
        document.getElementById("screen-question").classList.add("active");
        document.getElementById("prog-wrapper").style.display = "block";
        document.getElementById("header-title").textContent = "ANALYS PÅGÅR";
        loadQuestion();
    }}

    function loadQuestion() {{
        const currentModule = modulesOrder[currentModuleIndex];
        const questionsList = QUESTIONS_DB[currentModule];
        const question = questionsList[currentQuestionIndex];
        
        const totalCompleted = userAnswers.length;
        const progressPercent = (totalCompleted / totalQuestions) * 100;
        document.getElementById("progress-bar").style.width = `${{progressPercent}}%`;
        document.getElementById("progress-text").textContent = `FRÅGA ${{totalCompleted + 1}}/${{totalQuestions}}`;
        document.getElementById("module-text").textContent = `MODUL: ${{currentModule.toUpperCase()}}`;

        document.getElementById("question-text").textContent = question.text;

        const optionsList = document.getElementById("options-list");
        optionsList.innerHTML = "";
        question.options.forEach((opt, idx) => {{
            const btn = document.createElement("button");
            btn.className = "option-btn";
            btn.textContent = opt.text;
            btn.onclick = () => selectOption(idx);
            optionsList.appendChild(btn);
        }});
    }}

    function selectOption(index) {{
        userAnswers.push(index);
        
        const currentModule = modulesOrder[currentModuleIndex];
        const questionsList = QUESTIONS_DB[currentModule];
        currentQuestionIndex++;
        
        if (currentQuestionIndex >= questionsList.length) {{
            currentModuleIndex++;
            currentQuestionIndex = 0;
        }}

        if (currentModuleIndex >= modulesOrder.length) {{
            showResult();
        }} else {{
            const qBox = document.getElementById("screen-question");
            qBox.style.opacity = 0;
            setTimeout(() => {{
                loadQuestion();
                qBox.style.opacity = 1;
            }}, 100);
        }}
    }}

    function showResult() {{
        document.getElementById("screen-question").classList.remove("active");
        document.getElementById("screen-result").classList.add("active");
        document.getElementById("prog-wrapper").style.display = "none";
        document.getElementById("header-title").textContent = "EVALUERING KLAR";

        const answerString = userAnswers.join("");
        const b64 = btoa(answerString);
        const checksum = `PRA-${{SUBJ}}-${{FP}}-${{b64}}`;

        document.getElementById("hash-box").textContent = checksum;
    }}

    function copyHash() {{
        const hashText = document.getElementById("hash-box").textContent;
        navigator.clipboard.writeText(hashText).then(() => {{
            const notif = document.getElementById("copied-notification");
            notif.style.opacity = 1;
            setTimeout(() => {{
                notif.style.opacity = 0;
            }}, 2000);
        }});
    }}
</script>
</body>
</html>"""

def export_remote_test():
    clear_screen()
    print_header("Exportera Distanstest")
    print(f"{AMBER}Detta skapar en självkörande HTML-fil som du kan skicka till en specifik partner.{RESET}\n")
    
    subject = ""
    while subject not in ["D", "E"]:
        subject = input(f"{AMBER}Vem ska genomföra testet (D/E)?: {RESET}").strip().upper()
        
    fingerprint = questionnaire_fingerprint()
    stripped_q = strip_impact(QUESTIONS)
    html_content = generate_html_template(subject, fingerprint, stripped_q)
    
    filename = f"distans_test_{subject}.html"
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../' + filename))
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"\n{GREEN}✔ Distanstest genererat: {filename}{RESET}")
    print(f"{AMBER}Skicka filen till person {subject}. När de är klara ger de dig en kod som du importerar här.{RESET}")
    time.sleep(3)

def import_hash_data():
    clear_screen()
    print_header("Importera extern checksumma")
    print(f"{AMBER}Klistra in checksumman som du fick från din partner:{RESET}\n")
    
    raw_input = input(f"{AMBER}Kod: {RESET}")
    # Rensa allt whitespace (inklusive eventuella radbrytningar vid Messenger-kopiering)
    hash_str = re.sub(r'\s+', '', raw_input)
    
    # Validera mot Regex
    match = re.match(r'^PRA-([a-f0-9]{8})-([A-Za-z0-9+/=]+)$', hash_str)
    if not match:
        print(f"\n{RED}⚠ FEL: Ogiltigt kodformat. Koden är skadad eller felaktig.{RESET}")
        time.sleep(2)
        return
        
    fp, encoded = match.groups()
    
    # Validera Fingerprint
    current_fp = questionnaire_fingerprint()
    if fp != current_fp:
        print(f"\n{RED}⚠ FEL: Versionskonflikt! Koden skapades med ett äldre frågebatteri.{RESET}")
        print(f"{AMBER}Din nuvarande version: {current_fp}{RESET}")
        print(f"{AMBER}Filens version: {fp}{RESET}")
        print(f"{AMBER}Vänligen uppdatera webbsidan och gör om testet.{RESET}")
        time.sleep(5)
        return
        
    # Fråga vem svaren tillhör
    print()
    subject = ""
    while subject not in ["D", "E"]:
        subject = input(f"{AMBER}Vem tillhör dessa svar (D/E)?: {RESET}").strip().upper()
        
    # Normalisera Base64-padding
    padding_needed = (4 - len(encoded) % 4) % 4
    encoded += "=" * padding_needed
    try:
        decoded_bytes = base64.b64decode(encoded)
        answers_str = decoded_bytes.decode('utf-8')
    except Exception as e:
        print(f"\n{RED}⚠ FEL: Kunde inte avkoda Base64. ({e}){RESET}")
        time.sleep(2)
        return
        
    modules_order = ["attachment", "hsp", "gottman", "tki"]
    expected_len = sum(len(QUESTIONS[m]) for m in modules_order)
    
    if len(answers_str) != expected_len:
        print(f"\n{RED}⚠ FEL: Ogiltig längd på svar ({len(answers_str)} tecken istället för {expected_len}).{RESET}")
        time.sleep(2)
        return
        
    state = load_state_with_fallback()
    
    if subject not in state["subjects"]:
        print(f"\n{RED}⚠ FEL: Ogiltigt subjekt ({subject}).{RESET}")
        time.sleep(2)
        return

    char_idx = 0
    sub_ref = state["subjects"][subject]
    
    try:
        for module in modules_order:
            questions_list = QUESTIONS[module]
            module_answers = []
            
            for q in questions_list:
                ans_char = answers_str[char_idx]
                if not ans_char.isdigit():
                    raise ValueError(f"Svarsvärde måste vara numeriskt, hittade '{ans_char}'.")
                    
                ans_idx = int(ans_char)
                if ans_idx < 0 or ans_idx >= len(q["options"]):
                    raise ValueError(f"Ogiltigt svarsindex {ans_idx} för fråga {q['id']}")
                    
                ans_char_mapped = chr(65 + ans_idx) # 0 -> 'A', 1 -> 'B'...
                selected_opt = q["options"][ans_idx]
                
                module_answers.append({
                    "question_id": q["id"],
                    "answer": ans_char_mapped,
                    "impact": selected_opt["impact"]
                })
                char_idx += 1
                
            # Beräkna modulen
            if module == "attachment":
                tot_anx = sum(a["impact"]["anxiety"] for a in module_answers)
                tot_av = sum(a["impact"]["avoidance"] for a in module_answers)
                max_anx = sum(max(opt["impact"]["anxiety"] for opt in mq["options"]) for mq in QUESTIONS["attachment"])
                max_av = sum(max(opt["impact"]["avoidance"] for opt in mq["options"]) for mq in QUESTIONS["attachment"])
                sub_ref["attachment_profile"]["anxiety_score"]["computed"] = round(tot_anx / max_anx, 2) if max_anx > 0 else 0.0
                sub_ref["attachment_profile"]["avoidance_score"]["computed"] = round(tot_av / max_av, 2) if max_av > 0 else 0.0
                
            elif module == "hsp":
                tot_thresh = 8.0 + sum(a["impact"]["threshold"] for a in module_answers)
                tot_lat = sum(a["impact"]["latency"] for a in module_answers)
                sub_ref["sensory_processing"]["overload_threshold_hrs"]["computed"] = max(1.0, min(12.0, round(tot_thresh, 1)))
                sub_ref["sensory_processing"]["recovery_latency_hrs"]["computed"] = max(0.0, min(12.0, round(tot_lat, 1)))
                
            elif module == "gottman":
                flags = []
                stress_counts = {"hyperactivation": 0, "deactivation": 0, "secure": 0}
                for a in module_answers:
                    flags.extend(a["impact"].get("flags", []))
                    stress = a["impact"].get("stress")
                    if stress:
                        stress_counts[stress] += 1
                
                unique_flags = list(set([f for f in flags if flags.count(f) >= 2]))
                sub_ref["conflict_mechanisms"]["gottman_flags"]["computed"] = unique_flags
                primary_stress = max(stress_counts, key=stress_counts.get)
                sub_ref["attachment_profile"]["stress_response"]["computed"] = primary_stress
                
            elif module == "tki":
                tki_scores = {"competing": 0, "collaborating": 0, "compromising": 0, "avoiding": 0, "accommodating": 0}
                for a in module_answers:
                    for key in tki_scores:
                        tki_scores[key] += a["impact"].get(key, 0)
                
                primary_tki = max(tki_scores, key=tki_scores.get).capitalize()
                sub_ref["conflict_mechanisms"]["primary_tki"]["computed"] = primary_tki
                
    except Exception as e:
        print(f"\n{RED}⚠ FEL: Dataavvikelse under parsning: {e}{RESET}")
        time.sleep(3)
        return

    # Spara state
    save_json_atomic(STATE_FILE, state)
    
    # Kör analysen
    safe_run_analysis(STATE_FILE, TRAITS_FILE)
    
    print(f"\n{GREEN}✔ LYCKAD IMPORT! Svar för subjekt {subject} har registrerats och utvärderats.{RESET}")
    time.sleep(2)

def main_menu():
    # Gör en initierande körning för att säkerställa att allt är uppdaterat
    if os.path.exists(STATE_FILE) and os.path.exists(TRAITS_FILE):
        safe_run_analysis(STATE_FILE, TRAITS_FILE)
        
    while True:
        clear_screen()
        print(f"{AMBER}")
        print("  ===============================================================")
        print("   ██████╗ ███████╗████████╗██████╗  ██████╗     ██████╗██╗     ██╗")
        print("   ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗   ██╔════╝██║     ██║")
        print("   ██████╔╝█████╗     ██║   ██████╔╝██║   ██║   ██║     ██║     ██║")
        print("   ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║   ██║     ██║     ██║")
        print("   ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝   ╚██████╗███████╗██║")
        print("   ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚═════╝╚══════╝╚═╝")
        print("       P S Y K O M E T R I S K   R E L A T I O N S A N A L Y S")
        print("  ===============================================================")
        print(f"{RESET}")
        
        print(f"  {GREEN}[1] Starta/Återuppta Psykometriskt Frågebatteri{RESET}")
        print(f"  {GREEN}[2] Öppna Relations-Dashboard & Graf (Mind Map){RESET}")
        print(f"  {GREEN}[3] Importera svar via extern checksumma (hasch-kod){RESET}")
        print(f"  {GREEN}[4] Återställ All Insamlad Data{RESET}")
        print(f"  {GREEN}[5] Exportera Distanstest (HTML){RESET}")
        print(f"  {GREEN}[6] Avsluta Systemet{RESET}\n")
        
        choice = input(f"{AMBER}Välj alternativ (1-6): {RESET}").strip()
        if choice == '1':
            run_questionnaire()
        elif choice == '2':
            show_dashboard()
        elif choice == '3':
            import_hash_data()
        elif choice == '4':
            reset_all_data()
        elif choice == '5':
            export_remote_test()
        elif choice == '6':
            clear_screen()
            print(f"{AMBER}Avslutar retro-terminalen. Hejdå!{RESET}")
            sys.exit(0)

if __name__ == "__main__":
    # Aktivera ANSI färger för Windows-konsol
    os.system("")
    
    # Null / False / True fix för JSON-läsning från Python
    null = None
    true = True
    false = False
    
    main_menu()
