import json
with open("dados.json", "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)["listBoxesWithSomeClientOffline"]

quantidade = sum(x["offline"] for x in conteudo)

print(quantidade)


