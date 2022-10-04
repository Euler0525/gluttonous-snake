# -*- coding: utf-8 -*-
from snake import *


def turn(path: list[list]):
    if path[1][0] - path[0][0] > 0:
        change(10, 0)
    elif path[1][1] - path[0][1] > 0:
        change(0, 10)
    elif path[1][0] - path[0][0] < 0:
        change(-10, 0)
    else:
        change(0, -10)
    move()


def main():
    setup(420, 420)
    title("贪吃蛇")
    hideturtle()
    tracer(False)
    mainAlgorithm()


def mainAlgorithm():
    while all_food:
        path = AStar(Grid(snake[-1][0], snake[-1][1]), Grid(food_x, food_y), snake).pathFinding()
        if path:
            path_virtual = path.copy()
            snake_virtual = snake.copy()
            moveVirtual(snake_virtual, path_virtual)

            if AStar(Grid(snake_virtual[-1][0], snake_virtual[-1][1]), Grid(snake_virtual[0][0], snake_virtual[0][1]),
                     snake_virtual).pathFinding():
                turn(path)
            else:
                path = AStar(Grid(snake[-1][0], snake[-1][1]), Grid(snake[0][0], snake[0][1]), snake).pathFinding()
                turn(path)
        else:
            path = AStar(Grid(snake[-1][0], snake[-1][1]), Grid(snake[0][0], snake[0][1]), snake).pathFinding()
            turn(path)


if __name__ == "__main__":
    main()
    # setup(420, 420)
    # title("贪吃蛇")
    # hideturtle()
    # tracer(False)
    # listen()
    # onkey(lambda: change(0, 10), "Up")
    # onkey(lambda: change(-10, 0), "Left")
    # onkey(lambda: change(0, -10), "Down")
    # onkey(lambda: change(10, 0), "Right")
    # move()
    # done()
