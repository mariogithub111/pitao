from datetime import datetime


def dia_da_semana(num):
    if num == 0:
        return "2a feira"
    elif num == 1:
        return "3a feira"
    elif num == 2:
        return "4a feira"
    elif num == 3:
        return "5a feira"
    elif num == 4:
        return "6a feira"
    elif num == 5:
        return "sábado"
    elif num == 6:
        return "domingo"
    else:
        return "Dia da semana inválido"


dia = input('Em que dia nasceste: ')
mes = input('Em que mês: ')
ano = input('Em que ano: ')
print(f'Nasceste no dia {dia} de {mes} de {ano}')

data_nasc = datetime(day=int(dia), month=int(mes), year=int(ano))
dds_de_nasc = data_nasc.weekday()  # 0, 1, 2, 3, 4, 5, 6
dds_nome = dia_da_semana(dds_de_nasc)  # 2a feira, 3a feira, 4a feira, ...
print(f'Nasceste num(a) {dds_nome}')

# Calcula os anos
hoje = datetime.now()
idade = hoje.year - data_nasc.year
if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
    idade = idade - 1
print(f'Tens {idade} anos')

# Calcula os dias
diff = hoje - data_nasc
dias = diff.days
print(f'Tens {dias} dias')

# Calcula os segundos
segundos = dias * 86400 + diff.seconds
print(f'Tens {segundos} segundos ')

# Calcula os microssegundos?
micro_seg = segundos * 10**6 + diff.microseconds
print(f'Tens {micro_seg} microssegundos')
