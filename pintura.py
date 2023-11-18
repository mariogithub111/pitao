#programa que calcula áreas e tinta necessária para as pintar
altura = float(input('Qual é a altura em metros: '))
largura = float(input('Qual é a largura em metros: '))

# Calcula o produto entre ambos
area = altura * largura
# divide por dois porque é necessário um litro de tinta para 2 m2.
tinta = area / 2

print(f'a área da parede é o produto entre {altura} e {largura} igual a: {area} metros2')
print(f'a tinta precisa é metade de {area} m2 e vale: {tinta} litros')






























