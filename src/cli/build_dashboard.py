# -*- coding: utf-8 -*-
import os
import sys
import json

# Adjust path to import from core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.questions import QUESTIONS

def build():
    # File paths
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    template_path = os.path.join(base_dir, 'src/cli/dashboard_template.html')
    output_path = os.path.join(base_dir, 'dashboard.html')
    traits_path = os.path.join(base_dir, 'data/traits.json')

    print("Building dashboard...")

    # Load traits.json
    if not os.path.exists(traits_path):
        print(f"Error: {traits_path} not found.")
        sys.exit(1)
        
    with open(traits_path, 'r', encoding='utf-8') as f:
        traits_data = json.load(f)

    # Load template
    if not os.path.exists(template_path):
        print(f"Error: {template_path} not found.")
        sys.exit(1)

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Generate JSON structures
    questions_json = json.dumps(QUESTIONS, ensure_ascii=False)
    traits_json = json.dumps(traits_data, ensure_ascii=False)

    # Calculate questions fingerprint
    import hashlib
    modules_order = ["attachment", "hsp", "gottman", "tki"]
    signature_parts = []
    for module in modules_order:
        q_list = QUESTIONS.get(module, [])
        options_counts = ",".join(str(len(q["options"])) for q in q_list)
        signature_parts.append(f"{module}:{len(q_list)}:{options_counts}")
    canonical_string = "|".join(signature_parts)
    fingerprint = hashlib.sha256(canonical_string.encode('utf-8')).hexdigest()[:8]

    # Replace placeholders
    compiled_content = template_content
    compiled_content = compiled_content.replace('/*{{QUESTIONS}}*/', f'const QUESTIONS_DB = {questions_json};')
    compiled_content = compiled_content.replace('/*{{TRAITS}}*/', f'const TRAITS_DB = {traits_json};')
    compiled_content = compiled_content.replace('/*{{FINGERPRINT}}*/', f'const SYSTEM_FINGERPRINT = "{fingerprint}";')

    # Save to root folder
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(compiled_content)

    print(f"Successfully generated standalone dashboard: {output_path} (Fingerprint: {fingerprint})")

if __name__ == '__main__':
    build()
