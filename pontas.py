from estrela import estrela


def calcula_angulo(pontas: int):
    # pontas * angulo = 360 * int
    # 5 * 144 = 360 * 2
    # angulo = 360 * int / pontas

    angulos = []
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        angulo = 360 * i / pontas  # exemplo 5, angulo = 72
        # Decidir se o angulo e bom ou nao
        if angulo >= 360:
            continue
        else:
            angulos.append(angulo)  # pontas = 5 e i = 1 angulos = [72]
            # i = 2 angulos = [72, 144]
            # i = 3 angulos = [72, 144, 216]
            # i = 4 angulos = [72, 144, 216, 288]

    return angulos


print(calcula_angulo(5))

# estrela("blue", "white", 200, 72)
# estrela("green", "white", 200, 144)
# estrela("red", "white", 200, 216)
# estrela("black", "white", 200, 288)

#breakpoint()
