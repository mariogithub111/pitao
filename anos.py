from datetime import datetime
dia = input('Em que dia nasceste: ')
mes = input('Em que mês: ')
ano = input('Em que ano: ')
print(f'Nasceste no dia {dia} de {mes} de {ano} ')
data = datetime(day=int(dia), month=int(mes), year=int(ano))
hoje = datetime.now()
idade = hoje.year - data.year
if (hoje.month, hoje.day) < (data.month, data.day):
    idade = idade-1
print(f'Tens {idade} anos')
# Que idade tens em dias?
dias = hoje - data
print(f'Tens {dias.days} dias')
# Que idade tens em segundos?
print(f'Tens {dias.days * 86400 + dias.seconds} segundos ')
# Que idade tens em microssegundos?
print(f'Tens {dias.days * 86400 * 10**6} microssegundos')


































