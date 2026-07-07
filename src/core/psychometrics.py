# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_atomic(filepath, data):
    tmp_filepath = filepath + ".tmp"
    with open(tmp_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    # Validera tmp-filen
    try:
        with open(tmp_filepath, 'r', encoding='utf-8') as f:
            json.load(f)
    except Exception as e:
        if os.path.exists(tmp_filepath):
            os.remove(tmp_filepath)
        raise IOError(f"Kunde inte skriva giltig JSON: {e}")
        
    if os.path.exists(filepath):
        # Skapa en backup av originalet
        bak_filepath = filepath + ".bak"
        if os.path.exists(bak_filepath):
            os.remove(bak_filepath)
        os.rename(filepath, bak_filepath)
        
    os.rename(tmp_filepath, filepath)

def get_by_path(obj, path):
    """Hämta ett värde från ett nästlat dictionary via dot-notation (t.ex. 'attachment_profile.stress_response.effective')."""
    parts = path.split('.')
    curr = obj
    for part in parts:
        if isinstance(curr, dict) and part in curr:
            curr = curr[part]
        else:
            return None
    return curr

def evaluate_condition(sub_data, cond):
    """Utvärderar ett enskilt regelvillkor mot ett subjekts data."""
    path = cond["path"]
    operator = cond["operator"]
    value = cond["value"]
    
    actual_value = get_by_path(sub_data, path)
    if actual_value is None:
        return False
        
    if operator == "equal":
        return actual_value == value
    elif operator == "contains":
        if isinstance(actual_value, list):
            return value in actual_value
        elif isinstance(actual_value, str):
            return value in actual_value
        return False
    return False

def run_analysis(state_path, traits_path):
    state = load_json(state_path)
    traits_data = load_json(traits_path)
    if not state or not traits_data:
        return False

    subjects = state["subjects"]
    
    # 1. Genomför beräkningar för respektive subjekt
    for sub_id, sub_data in subjects.items():
        # --- Uppdatera effective-värden ---
        for profile_name, profile in sub_data.items():
            if isinstance(profile, dict):
                for var_name, var_data in profile.items():
                    if isinstance(var_data, dict) and "computed" in var_data:
                        if var_data.get("override") is not None:
                            var_data["effective"] = var_data["override"]
                        else:
                            var_data["effective"] = var_data["computed"]

        # --- Identifiera drag (traits) ---
        identified = []
        for trait in traits_data.get("traits", []):
            conditions = trait.get("conditions", {})
            match = True
            
            for var_path, cond in conditions.items():
                # Hämta variabeln dynamiskt
                val = None
                if var_path in sub_data.get("attachment_profile", {}):
                    val = sub_data["attachment_profile"][var_path]["effective"]
                elif var_path in sub_data.get("sensory_processing", {}):
                    val = sub_data["sensory_processing"][var_path]["effective"]
                elif var_path in sub_data.get("conflict_mechanisms", {}):
                    val = sub_data["conflict_mechanisms"][var_path]["effective"]
                
                if val is None:
                    match = False
                    break
                
                if "min" in cond and val < cond["min"]:
                    match = False
                if "max" in cond and val > cond["max"]:
                    match = False
            
            if match:
                identified.append(trait["id"])
        
        sub_data["identified_traits"] = identified

    # 2. Utvärdera bilaterala interaktionsregler dynamiskt
    critical_warnings = []
    attraction_factors = []
    connections = []
    
    for rule in traits_data.get("interaction_rules", []):
        conditions = rule.get("conditions", [])
        if not conditions:
            continue
            
        trigged = True
        for cond in conditions:
            subject_id = cond["subject"]
            if subject_id not in subjects:
                trigged = False
                break
            sub_data = subjects[subject_id]
            if not evaluate_condition(sub_data, cond):
                trigged = False
                break
                
        if trigged:
            # Bygg noder för relationsgrafen dynamiskt utifrån villkoren
            source_nodes = []
            target_nodes = []
            for cond in conditions:
                val = cond["value"]
                if cond["subject"] == "D":
                    source_nodes.append(f"D_{val}")
                elif cond["subject"] == "E":
                    target_nodes.append(f"E_{val}")
                    
            source_node = source_nodes[0] if source_nodes else "D_General"
            target_node = target_nodes[0] if target_nodes else "E_General"
            
            conn = {
                "source_node": source_node,
                "target_node": target_node,
                "edge_type": rule["type"],
                "evidence": rule["id"],
                "description": rule["description"]
            }
            connections.append(conn)
            
            if rule["type"] == "collision":
                critical_warnings.append(rule["description"])
            elif rule["type"] == "attraction":
                attraction_factors.append(rule["description"])

    # 3. Beräkna logistisk synk-poäng
    sync_score = 1.0
    for conn in connections:
        if conn["edge_type"] == "collision":
            sync_score -= 0.2
        elif conn["edge_type"] == "attraction":
            sync_score += 0.1
    sync_score = max(0.0, min(1.0, sync_score))
    
    # 4. Spara slutsatserna i state
    state["compatibility_matrix"]["critical_warnings"] = list(set(critical_warnings))
    state["compatibility_matrix"]["attraction_factors"] = list(set(attraction_factors))
    state["compatibility_matrix"]["logistical_sync"] = round(sync_score * 100, 1)
    state["compatibility_matrix"]["mind_map"]["connections"] = connections
    
    state["system_meta"]["last_updated"] = datetime.now().isoformat()
    # state["system_meta"]["iteration"] = state["system_meta"].get("iteration", 1) + 1 # Begränsad för att undvika runaway vid dashboard hot-reloads
    
    save_json_atomic(state_path, state)
    return True
