def limpar_texto(texto):
    """
    Docstring for limpar_texto
        Recebe um texto, colocar em minúsculo e remove caracteres especiais.
    :param texto: Texto a ser limpo
    :return: Texto limpo
    """
    texto = texto.lower()
    caracteres = """,.;:?<>}{[]()`^/"'|@#$%¨&*-_=+´~°ºª§¬¢£¹²³*\\"""
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto

def contar_palavras(frase):

    frase = limpar_texto(frase)

    if not frase.strip():
        return {}
    
    lista_palavras = frase.split()
    palavras = {}
    for palavra in lista_palavras:
        palavras[palavra] = palavras.get(palavra, 0) + 1

    return palavras 
