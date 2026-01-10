import random

def gerar_senha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    especiais = "!@#$%&*"
    todos_caracteres = maiusculas + minusculas + numeros + especiais

    senha = [ 
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]
    final = random.choices(todos_caracteres, k=8)
    senha.extend(final)
    random.shuffle(senha)
    return "".join(senha)


senha = gerar_senha()
print(senha)