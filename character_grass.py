from pico2d import *
import math


open_canvas()

# fill here

grass = load_image('grass.png')

boy = load_image('character.png')


def run_rectangle():
    print('rectangle')

    pass


def run_circle():
    print('Circle')

    r, cx, cy  = 300, 800//2, 600//2

    for d in range(0,360):
        x = cx + r * math.cos(math.radians(d))
        y = cy + r * math.sin(math.radians(d))
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.01)


    pass


while True:
    run_rectangle()
    run_circle()
    break

close_canvas()
