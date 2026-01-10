from calculo import valor_comanda

try: 
    consumo = float(input("Digite o valor do consumo: R$ "))
    percentual = float(input("Digite o percentual da gorjeta (%): "))
    resultado = valor_comanda(consumo, percentual)
    print("\n## Nota Fiscal ##")
    
    print(f"Consumo:\t\t{consumo}")
    for chave, valor in resultado.items():
        print(f"{chave}:\t\t  {valor}")
    print("#################\n")
except:
    print("Valor inválido. Tente novamente.")
    