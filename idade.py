from datetime import datetime

def idade(data_nasc):
    hoje = datetime.now()
    idade_anos = hoje.year - data_nasc.year
    if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
        idade_anos = idade_anos - 1

    idade = {}
    idade['anos'] = idade_anos

    # Que idade tens em dias?
    dias = hoje - data_nasc
    idade_dias = dias.days
    idade['dias'] = idade_dias

    # Que idade tens em segundos?
    idade_segundos = dias.days * 86400 + dias.seconds
    idade['segundos'] = idade_segundos

    # Que idade tens em microssegundos?
    idade_micro = dias.days * 86400 * 10**6 + dias.microseconds
    idade['micro'] = idade_micro

    return idade

print(idade(datetime(1948, 1, 23)))
print(idade(datetime(1952, 5, 7)))
print(idade(datetime(1977, 12, 18)))
print(idade(datetime(1929, 8, 9)))
print(idade(datetime(1106, 1, 1)))
print(idade(datetime(1983, 4, 1)))






































