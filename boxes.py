import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(50,255)
    width = WIDTH
    heigth = HEIGHT - 200
    
    for i in range(20):
        rect_shape = Rect((0,0),(width,heigth))
        rect_shape.center = 150,150
        screen.draw.rect(rect_shape,(b,r,g))
        r -= 10
        g += 10
        width -= 10
        heigth += 10

pgzrun.go()