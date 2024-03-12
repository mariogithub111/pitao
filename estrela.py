from turtle import *


def estrela(cor: str, fundo: str, tamanho: int, angulo: int):
    title("Estrela")
    speed(1)
    shape("turtle")

    color(cor)
    #fillcolor(fundo)

    #begin_fill()

    while True:
        forward(tamanho)
        left(angulo)

        # Como parar o while True? Com a instrucao break
        if abs(pos()) < 1:  # A tartaruga esta na posicao 0, 0
            break

    #end_fill()


# cor = input("Cor da linha: ")
# fundo = input("Cor do fundo: ")
# tamanho = int(input("Tamanho da linha: "))
# angulo = int(input("Ângulo: "))
#
# estrela(cor, fundo, tamanho, angulo)
#
# breakpoint()
