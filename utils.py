import json

def load_data(nome_json):
    with open(f"static/data/{nome_json}", 'r', encoding='utf-8') as arquivo:
        dados = json.loads(arquivo.read())
    return dados

def load_template(nome_template):
    with open(f"static/templates/{nome_template}", 'r', encoding='utf-8') as arquivo:
        template = arquivo.read()
    return template