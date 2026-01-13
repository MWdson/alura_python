import json
try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)["listBoxesWithSomeClientOffline"]

    quantidade = sum(x["offline"] for x in conteudo)

    print(quantidade)

except Exception as e:
    print(f"Ero encontrado: \n{e}")
