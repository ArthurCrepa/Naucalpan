from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
# Usar letras del alfabeto en lugar de dígitos
tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') * 2
state = {'mark': None}
hide = [True] * 64
taps = 0  # Contador de taps

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global taps
    spot = index(x, y)
    mark = state['mark']
    
    if hide[spot]:
        taps += 1  # Incrementar contador de taps
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Mostrar contador de taps
    up()
    goto(0, 180)
    color('black')
    write(f'Taps: {taps}', align='center', font=('Arial', 24, 'normal'))

    # Dibujar los cuadros y los símbolos o números
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
        else:
            x, y = xy(count)
            up()
            goto(x + 25, y + 8)  # Centrando el texto
            color('black')
            write(tiles[count], align='center', font=('Arial', 30, 'normal'))

    # Dibujar el marco seleccionado
    mark = state['mark']
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 8)  # Centrando el texto
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    # Verificar si el juego está completo
    if all(not hidden for hidden in hide):
        goto(0, 0)
        color('green')
        write('¡Juego completado!', align='center', font=('Arial', 36, 'bold'))

    update()
    ontimer(draw, 100)

# Inicialización del juego
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
