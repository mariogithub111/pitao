import random
import turtle


# Preparar as turtles
burrie = turtle.Turtle()
burrie.shape("turtle")
burrie.shapesize(2, 2, 2)
burrie.color("green")
burrie.up()
coco = turtle.Turtle()
coco.shape("turtle")
coco.shapesize(2, 2, 2)
coco.color("blue")
coco.up()
leo = turtle.Turtle()
leo.shape("turtle")
leo.shapesize(2, 2, 2)
leo.color("orange")
leo.up()
clara = turtle.Turtle()
clara.shape("turtle")
clara.shapesize(2, 2, 2)
clara.color("purple")
clara.up()

# Aos seus lugares
burrie.setposition(-300, 0)
coco.setposition(-300, -60)
leo.setposition(-300, 60)
clara.setposition(-300, 120)

# Primeiro passo
burrie.forward(1)
coco.forward(1)
leo.forward(1)
clara.forward(1)

# Partida
while True:
    step = random.randrange(1, 5)
    burrie.forward(step)

    step = random.randrange(1, 5)
    coco.forward(step)

    step = random.randrange(1, 5)
    leo.forward(step)

    step = random.randrange(1, 5)
    clara.forward(step)

    if (burrie.pos() >= (300, 0) or
        coco.pos() >= (300, -40) or
        leo.pos() >= (300, 40) or
        clara.pos() >= (300, 80)
    ):
        break


breakpoint()