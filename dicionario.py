from datetime import datetime

from datas import idade  # Estamos a importar a funcao idade do ficheiro datas

# Fazer um dicionario com nomes e a respetiva data de nascimento
familia = {
    "mario": datetime(1948, 1, 23),
    "margarida": datetime(1952, 5, 7),
    "filipa": datetime(1977, 12, 18),
    "mariana": datetime(1983, 4, 1),
    "carolina": datetime(2013, 6, 20),
    "leo": datetime(2014, 3, 7),
    "clara": datetime(2017, 2, 13),
    "olivia": datetime(2018, 11, 15),
    "avo ermelinda": datetime(1892, 11, 3),
    "avo carmo": datetime(1923, 12, 30),
    "avo sao": datetime(1924, 9, 28),
}

# Imprimir as idades de todas as pessoas no dicionario
for chave, valor in familia.items():
    print(chave, valor)
    print(idade(valor))


# Como aceder a um elemento do dicionario
# Forma 1 em 2 linhas
dn_mario = familia["mario"]  # dn_mario = date(1948, 1, 23)
print(idade(dn_mario))

# Forma 2 numa linha
print(idade(familia["mario"]))


# Outro exemplo de um dicionario
livro = {
    "capitulo 1": 3,
    "capitulo 2": 16,
    "capitulo 3": 30,
    "capitulo 4": 42,
}

print(livro["capitulo 4"])
