import os
import re
import random
import string
import sys
import json
import tokenize
from io import StringIO

def obfuscate_code(code, mapping):
    result = []
    tokens = tokenize.generate_tokens(StringIO(code).readline)
    for toknum, tokval, _, _, _ in tokens:
        if toknum == tokenize.NAME and tokval in mapping:
            result.append((toknum, mapping[tokval]))
        else:
            result.append((toknum, tokval))
    return tokenize.untokenize(result)
    return tokenize.untokenize(result)
def generate_obfuscated_name(length=8):
    return random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits, k=length - 1))

def extract_identifiers(code):
    tokens = tokenize.generate_tokens(StringIO(code).readline)
    identifiers = set()
    imported_names = set()
    for toknum, tokval, _, _, _ in tokens:
        if toknum == tokenize.NAME and tokval not in keyword_set:
            identifiers.add(tokval)
    # Imports erkennen und ausschließen
    import_lines = re.findall(r'^\s*(?:from|import)\s+[^\n]+', code, re.MULTILINE)
    for line in import_lines:
        parts = re.split(r'[ ,]+|as ', line)
        for part in parts:
            if part.isidentifier():
                imported_names.add(part)
    return identifiers - keyword_set - imported_names, import_lines

keyword_set = set([
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
    "print", "input", "len", "range", "open", "int", "str", "float", "list", "dict", "set", "tuple", "type",
    "dir", "help", "map", "filter", "zip", "enumerate", "super", "self", "__name__", "__main__"
])

def safe_replace(code, name, obf_name, import_lines):
    lines = code.split('\n')
    for i, line in enumerate(lines):
        if any(line.strip().startswith(imp.strip()) for imp in import_lines):
            continue
        lines[i] = re.sub(rf'\b{name}\b', obf_name, line)
    return '\n'.join(lines)

def obfuscate_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        code = f.read()

    identifiers, import_lines = extract_identifiers(code)

    mapping = {}
    for name in identifiers:
        obf_name = generate_obfuscated_name()
        mapping[name] = obf_name

    code = obfuscate_code(code, mapping)

    # Deobfuscation-Check einfügen
    deobfuscate_check = '''
###DEOBFUSCATE_START###
import sys
import json
import tempfile
import os
import subprocess
import urllib.request

def load_mapping(source_type, source_value):
    if source_type == "path":
        with open(source_value, "r", encoding="utf-8") as f:
            return json.load(f)
    elif source_type == "url":
        with urllib.request.urlopen(source_value) as response:
            return json.loads(response.read().decode("utf-8"))
    else:
        raise ValueError("Ungültiger Typ für --deobfuscate: 'path' oder 'url' erwartet.")

# Argumente prüfen
if "--deobfuscate" in sys.argv:
    try:
        idx = sys.argv.index("--deobfuscate")
        source_type = sys.argv[idx + 1]
        source_value = sys.argv[idx + 2]
        mapping = load_mapping(source_type, source_value)
    except Exception as e:
        print("❌ Fehler beim Laden der Mapping-Datei:", e)
        sys.exit(1)
else:
    # Fallback: GitHub verwenden
    try:
        github_url = "https://raw.githubusercontent.com/Gymnasium-Freiham/LATIN-AI/refs/heads/main/deobfuscation_mappings.txt"
        mapping = load_mapping("url", github_url)
        print("ℹ️ Mapping von GitHub geladen.")
    except Exception as e:
        print("❌ Fehler beim Laden der GitHub-Mapping-Datei:", e)
        sys.exit(1)

# Originalcode laden
with open(__file__, "r", encoding="utf-8") as f:
    original_code = f.read()

start_marker = "###DEOBFUSCATE_START###"
end_marker = "###DEOBFUSCATE_END###"
if start_marker in original_code and end_marker in original_code:
    stripped_code = original_code.split(start_marker)[0] + original_code.split(end_marker)[-1]
else:
    stripped_code = original_code

# Deobfuscation anwenden
for k, v in mapping.items():
    stripped_code = stripped_code.replace(v, k)

# Temporäre Datei ausführen
with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py", encoding="utf-8") as temp:
    temp.write(stripped_code)
    temp_path = temp.name

exit_code = subprocess.run([sys.executable, temp_path]).returncode

try:
    os.remove(temp_path)
except Exception:
    pass

sys.exit(exit_code)
###DEOBFUSCATE_END###
'''

    code = deobfuscate_check + "\n" + code

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code)

    with open("main_obfuscation_mappings.txt", 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2)

    print("✅ Obfuskation abgeschlossen. Mapping gespeichert in deobfuscation_mappings.txt")

if __name__ == "__main__":
    target = "main.py"
    if not os.path.exists(target):
        print("Datei main.py nicht gefunden.")
        sys.exit(1)
    obfuscate_file(target)