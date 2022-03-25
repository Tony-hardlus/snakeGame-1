
from random import randrange
from turtle import *
from freegames import square, vector
#VRDL: Se importó librería para su uso en la función movefood()
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        # VRDL: Se cambió el color a "black"
        square(head.x, head.y, 9, 'black')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
    # VRDL: Se cambió color de comida
        square(body.x, body.y, 9, 'green')
    square(food.x, food.y, 9, 'red')
    # VRDL: para mover la comida:
    moveFood = [10,-10]
    rand1 = random.randint(0,1) # VRDL: (x,y)
    rand2 = random.randint(0,1) #up/down right/left
    # --- Se delimitan bordes con condicionales---
    if rand1==0 and food.x>=-190 and food.x<=180: 
        food.x+=moveFood[rand2]
    elif rand1==0 and food.x<-190:
        food.x=-190
    elif rand1==0 and food.x>180:
        food.x=180

    if rand1==1 and food.y>=-190 and food.y<=180:
        food.y+=moveFood[rand2]
    elif rand1==1 and food.y<-190:
        food.y=-190
    elif rand1==1 and food.y>180:
        food.y=180

    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

