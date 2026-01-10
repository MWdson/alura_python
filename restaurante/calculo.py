def __calcular_gorgeta(valor, percentual):
    return valor * (percentual / 100)

def __valor_final(valor, gorgeta):
    return valor + gorgeta

def valor_comanda(valor, percentual):
    gorgeta = __calcular_gorgeta(valor, percentual)
    return {
        "Gorgeta": gorgeta,
        "Valor final": __valor_final(valor, gorgeta)
    }