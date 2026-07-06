# -*- coding: utf-8 -*-
import os
import sys
import json
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.psychometrics import run_analysis, save_json_atomic

TEST_STATE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_relation_state.json'))
TEST_TRAITS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_traits.json'))

class TestPsychometrics(unittest.TestCase):

    def setUp(self):
        # Skapa temporär state-fil
        self.state_data = {
            "system_meta": {
                "iteration": 1,
                "last_updated": "ISO8601"
            },
            "subjects": {
                "D": {
                    "attachment_profile": {
                        "anxiety_score": { "computed": 0.8, "override": None, "override_reason": None, "effective": 0.8 },
                        "avoidance_score": { "computed": 0.1, "override": None, "override_reason": None, "effective": 0.1 },
                        "stress_response": { "computed": "hyperactivation", "override": None, "override_reason": None, "effective": "hyperactivation" }
                    },
                    "sensory_processing": {
                        "overload_threshold_hrs": { "computed": 2.0, "override": None, "override_reason": None, "effective": 2.0 },
                        "recovery_latency_hrs": { "computed": 5.0, "override": None, "override_reason": None, "effective": 5.0 }
                    },
                    "conflict_mechanisms": {
                        "primary_tki": { "computed": "Competing", "override": None, "override_reason": None, "effective": "Competing" },
                        "gottman_flags": { "computed": ["Kritik"], "override": None, "override_reason": None, "effective": ["Kritik"] }
                    },
                    "identified_traits": [],
                    "interview_notes": {}
                },
                "E": {
                    "attachment_profile": {
                        "anxiety_score": { "computed": 0.2, "override": None, "override_reason": None, "effective": 0.2 },
                        "avoidance_score": { "computed": 0.9, "override": None, "override_reason": None, "effective": 0.9 },
                        "stress_response": { "computed": "deactivation", "override": None, "override_reason": None, "effective": "deactivation" }
                    },
                    "sensory_processing": {
                        "overload_threshold_hrs": { "computed": 8.0, "override": None, "override_reason": None, "effective": 8.0 },
                        "recovery_latency_hrs": { "computed": 1.0, "override": None, "override_reason": None, "effective": 1.0 }
                    },
                    "conflict_mechanisms": {
                        "primary_tki": { "computed": "Avoiding", "override": None, "override_reason": None, "effective": "Avoiding" },
                        "gottman_flags": { "computed": ["Stonewalling"], "override": None, "override_reason": None, "effective": ["Stonewalling"] }
                    },
                    "identified_traits": [],
                    "interview_notes": {}
                }
            },
            "compatibility_matrix": {
                "critical_warnings": [],
                "attraction_factors": [],
                "logistical_sync": 0.0,
                "mind_map": { "connections": [] }
            }
        }
        
        # Skapa temporär traits-fil
        self.traits_data = {
            "traits": [
                {
                    "id": "ANXIOUS_PREOCCUPIED",
                    "module": "attachment",
                    "name": "Ångestfylld",
                    "conditions": {
                        "anxiety_score": { "min": 0.6 },
                        "avoidance_score": { "max": 0.4 }
                    }
                },
                {
                    "id": "DISMISSIVE_AVOIDANT",
                    "module": "attachment",
                    "name": "Avfärdande-undvikande",
                    "conditions": {
                        "anxiety_score": { "max": 0.4 },
                        "avoidance_score": { "min": 0.6 }
                    }
                },
                {
                    "id": "HSP_EOE",
                    "module": "hsp",
                    "name": "HSP-EOE",
                    "conditions": {
                        "recovery_latency_hrs": { "min": 4.0 }
                    }
                }
            ],
            "interaction_rules": [
                {
                    "id": "RULE_ANXIOUS_AVOIDANT_TRAP",
                    "conditions": [
                        { "subject": "D", "path": "identified_traits", "operator": "contains", "value": "ANXIOUS_PREOCCUPIED" },
                        { "subject": "E", "path": "identified_traits", "operator": "contains", "value": "DISMISSIVE_AVOIDANT" }
                    ],
                    "type": "collision",
                    "severity": "critical",
                    "description": "Ångest-Undvikande-fällan aktiv."
                },
                {
                    "id": "RULE_HSP_RECOVERY_COLLISION",
                    "conditions": [
                        { "subject": "D", "path": "identified_traits", "operator": "contains", "value": "HSP_EOE" },
                        { "subject": "E", "path": "attachment_profile.stress_response.effective", "operator": "equal", "value": "hyperactivation" }
                    ],
                    "type": "collision",
                    "severity": "high",
                    "description": "Sensorisk återhämtningskrock."
                }
            ]
        }
        
        save_json_atomic(TEST_STATE_FILE, self.state_data)
        save_json_atomic(TEST_TRAITS_FILE, self.traits_data)

    def tearDown(self):
        # Städa upp filer efter testet
        for f in [TEST_STATE_FILE, TEST_TRAITS_FILE, TEST_STATE_FILE + ".bak", TEST_TRAITS_FILE + ".bak"]:
            if os.path.exists(f):
                os.remove(f)

    def test_analysis_computations(self):
        # Kör analysen
        success = run_analysis(TEST_STATE_FILE, TEST_TRAITS_FILE)
        self.assertTrue(success)
        
        # Läs resultatet
        with open(TEST_STATE_FILE, 'r', encoding='utf-8') as f:
            result = json.load(f)
            
        # Kontrollera att D har klassificerats som ANXIOUS_PREOCCUPIED och HSP_EOE
        self.assertIn("ANXIOUS_PREOCCUPIED", result["subjects"]["D"]["identified_traits"])
        self.assertIn("HSP_EOE", result["subjects"]["D"]["identified_traits"])
        
        # Kontrollera att E har klassificerats som DISMISSIVE_AVOIDANT
        self.assertIn("DISMISSIVE_AVOIDANT", result["subjects"]["E"]["identified_traits"])
        
        # Kontrollera att Ångest-Undvikande-fällan har triggats
        warnings = result["compatibility_matrix"]["critical_warnings"]
        self.assertTrue(any("Ångest-Undvikande-fällan" in w for w in warnings))
        
        # Kontrollera logistisk synk-poäng
        self.assertLess(result["compatibility_matrix"]["logistical_sync"], 100.0)

    def test_override_protection(self):
        # Läs state och lägg till en override för D:s anxiety_score
        with open(TEST_STATE_FILE, 'r', encoding='utf-8') as f:
            state = json.load(f)
        
        # Operatören sätter en override som sänker D:s ångestpoäng från 0.8 till 0.3
        state["subjects"]["D"]["attachment_profile"]["anxiety_score"]["override"] = 0.3
        state["subjects"]["D"]["attachment_profile"]["anxiety_score"]["override_reason"] = "Djupintervju justering"
        save_json_atomic(TEST_STATE_FILE, state)
        
        # Kör analysen på nytt
        run_analysis(TEST_STATE_FILE, TEST_TRAITS_FILE)
        
        # Läs det uppdaterade tillståndet
        with open(TEST_STATE_FILE, 'r', encoding='utf-8') as f:
            updated = json.load(f)
            
        # Kontrollera att computed fortfarande är 0.8 men effective är 0.3
        d_anx = updated["subjects"]["D"]["attachment_profile"]["anxiety_score"]
        self.assertEqual(d_anx["computed"], 0.8)
        self.assertEqual(d_anx["override"], 0.3)
        self.assertEqual(d_anx["effective"], 0.3)
        
        # Eftersom effective nu är 0.3 ska D inte längre klassificeras som ANXIOUS_PREOCCUPIED
        self.assertNotIn("ANXIOUS_PREOCCUPIED", updated["subjects"]["D"]["identified_traits"])

if __name__ == "__main__":
    unittest.main()
