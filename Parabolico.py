from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15  # Aumenta la velocidad del proyectil
        speed.y = (y + 200) / 15  # Aumenta la velocidad del proyectil

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(30) == 0:  # Aumentar la frecuencia de aparición de los balones
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2  # Aumentar la velocidad de los balones

    if inside(ball):
        speed.y -= 0.7  # Aumentar la velocidad de caída del proyectil
        ball.move(speed)

    for target in targets:
        if not inside(target):
            target.x = 200  # Reposiciona el balón a la derecha de la pantalla

    draw()
    ontimer(move, 50)  # Mantener la misma velocidad de actualización

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
