# Fazer um algoritmo que leia o preco de 1 produto
# e mostre o seu novo preço com desconto.
preco = float(input('Qual é o preco? '))
desconto = int(input('Qual é o desconto? '))
preco_final = preco - (preco * desconto / 100)
print(f'O preço com desconto é {preco_final}')


