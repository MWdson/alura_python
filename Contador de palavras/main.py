from contar_vogais import contar_vogais
from contador import contar_palavras

while True:
    frase = input("Digite uma frase (ou 'sair' para encerrar):").strip()
    if not frase:
        print("Erro: Nenhuma frase foi digitada.")
        continue
    
    resultado = contar_palavras(frase)
    resultado_vogais = contar_vogais(frase)
    if resultado:
        print("\n## Contagem de palavras ##")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}: {quantidade}")
        
        print("\n## Contagem de palavras ##")
        for vogal, qunatidade in resultado_vogais.items():
            print(f"{vogal}: {qunatidade}")

        print("#################\n")
    else:
        print("Nenhuma palavra válida encontrada na frase.")

    if frase.lower() == 'sair':
        print("Fim!")
        break