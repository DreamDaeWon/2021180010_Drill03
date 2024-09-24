from pico2d import *
import math


open_canvas()

# fill here

grass = load_image('grass.png')

boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def run_top():
    for x in range(50,750,10):
        draw_boy(x, 550)

    pass

def run_right():
    for y in range(550, 50, -10):
        draw_boy(750, y)

    pass

def run_bottom():
    for x in range(750, 50, -10):
        draw_boy(x, 50)

    pass

def run_left():
    for y in range(50, 550, 10):
        draw_boy(50, y)

    pass


def run_rectangle():

    run_top()
    run_right()
    run_bottom()
    run_left()


    pass


def run_circle():


    r, cx, cy  = 300, 800//2, 600//2

    for d in range(0,360):
        x = cx + r * math.cos(math.radians(d))
        y = cy + r * math.sin(math.radians(d))
        draw_boy(x, y)
    pass


def run_triangle_bottom():
    run_bottom()
    pass

def run_triangle_left_up():
    for a in range(50,300):
        draw_boy(a, a)
    pass

def run_triangle_right_down():
    print('left_down')
    pass


def run_triangle():
    run_triangle_bottom()
    run_triangle_left_up()
    run_triangle_right_down()
    pass


while True:
    #run_circle()
    #run_rectangle()
    run_triangle()
    break

close_canvas()
