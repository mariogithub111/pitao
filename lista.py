pares = [2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9, 11]


# Fazer uma função que receba uma lista de inteiros e devolva a soma dos seus elementos
def soma(lista):
    sum = 0
    # Exemplo: [4, 6, 2, 3, 9, 1, 10]
    for elemento in lista:  # primeira vez: 4, segunda vez: 6, ...
        sum = sum + elemento  # primeira vez: 0 + 4 = 4, segunda vez: 4 + 6 = 10, ...

    return sum

print(soma(pares))
print(soma(impares))
print(soma([4, 6, 2, 3, 9, 1, 10]))

# Exercicio 2:
# Fazer uma função que receba uma lista de inteiros e devolva o maior dos seus elementos
def maior(lista):
    max = 0  # Assumimos que o maximo e 0
    for elemento in lista:  # Vamos percorrer a lista
        if elemento > max:  # Se o elemento em que estamos e maior que o maximo
            max = elemento  # Atualizamos o maximo

    return max  # Retornamos o maximo

print(maior(pares))
print(maior(impares))
print(maior([3, 7, 11, 1, 8, 5, 19, 2, 0, 5, 6, 17]))
