pares = [2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9, 11]


# Fazer uma função que receba uma lista de inteiros e devolva a soma dos seus elementos
def soma(lista):
    soma = 0
    # Exemplo: [4, 6, 2, 3, 9, 1, 10]
    for elemento in lista:  # primeira vez: 4, segunda vez: 6, ...
        soma = soma + elemento  # primeira vez: 0 + 4 = 4, segunda vez: 4 + 6 = 10, ...

    return soma


print(soma(pares))
print(soma(impares))
print(soma([4, 6, 2, 3, 9, 1, 10]))


# Exercicio 2:
# Fazer uma função que receba uma lista de inteiros e devolva o maior dos seus elementos