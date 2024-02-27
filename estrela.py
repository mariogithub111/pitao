from turtle import color, fillcolor, begin_fill, forward, left, end_fill, pos, bgcolor, title, pensize, shape


def estrela(cor: str, fundo: str, tamanho: int):
    bgcolor("yellow")
    title("Estrela")
    pensize(5)
    shape("turtle")

    color(cor)
    fillcolor(fundo)

    begin_fill()

    while True:
        forward(tamanho)
        left(170)

        # Como parar o while True? Com a instrucao break
        if abs(pos()) < 0.5:  # A tartaruga esta na posicao 0, 0
            break

    end_fill()


cor = input("Cor da linha: ")
fundo = input("Cor do fundo: ")
tamanho = int(input("Tamanho da linha: "))

estrela(cor, fundo, tamanho)

breakpoint()
