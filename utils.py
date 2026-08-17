import json

def load_data(name_json):
    with open(f"static/data/{name_json}", 'r', encoding='utf-8') as arquivo:
        dados = json.loads(arquivo.read())
    return dados

def load_template(name_template):
    with open(f"static/templates/{name_template}", 'r', encoding='utf-8') as arquivo:
        template = arquivo.read()
    return template

def add_data(new_note):
    dados = load_data('notes.json')
    dados.append(new_note)
    with open("static/data/notes.json","w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo)