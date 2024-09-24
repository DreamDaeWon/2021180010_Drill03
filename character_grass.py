from pico2d import *
import math


open_canvas()

# fill here

grass = load_image('grass.png')

boy = load_image('character.png')


def run_top():
    print('Top')
    pass

def run_right():
    print('Right')

    pass

def run_bottom():
    print('Bottom')

    pass

def run_left():
    print('Left')

    pass



def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()


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
    #run_circle()
    break

close_canvas()
