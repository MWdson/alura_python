def contar_vogais(texto):
    """
    Docstring for contar_vogais
        Recebe um texto e conta a quantidade de vogais.
    :param texto: Texto a ser analisado
    :return: Dicionário com a contagem de vogais
    """
    texto = texto.lower()
    vogais = "aeiou"
    contagem = {}
    for char in vogais:
        contagem[char] = texto.count(char)
    
    return contagem