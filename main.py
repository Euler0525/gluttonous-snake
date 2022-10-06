# -*- coding: utf-8 -*-

"""
pathfinding -> 起点到终点的最短路径
moveVirtual -> 能否找到蛇尾
# if 能吃到食物
     # 派虚拟蛇去吃，
            # if吃完能跟着蛇尾走 真蛇去吃
            # if吃完不能跟着蛇尾 真蛇跟着蛇尾走
# else
    # 真蛇跟着蛇尾
"""

from snake import *
from copy import deepcopy


def mainAlgorithm():
    food_path = AStar(Grid(snake[-1][0], snake[-1][1]), Grid(food_x, food_y), snake).pathFinding()
    tail_path = AStar(Grid(snake[-1][0], snake[-1][1]), Grid(snake[0][0] + 10, snake[0][1] + 10), snake).pathFinding()

    if len(food_path) != 0:
        tmp = moveVirtual(snake, food_path)
        if len(tmp) != 0:
            moveOneStep(snake, food_path)
        else:
            moveOneStep(snake, tail_path)
    else:
        moveOneStep(snake, tail_path)


def moveVirtual(snake, path) -> list[list]:
    snake_virtual = deepcopy(snake)
    path_virtual = deepcopy(path)
    snake_virtual.reverse()
    path_virtual.reverse()
    length_snake = len(snake_virtual)
    length_path = len(path_virtual)

    if length_snake > length_path:
        snake_virtual = path_virtual + snake_virtual[length_path:length_snake - length_path + 20]
    else:
        snake_virtual = path_virtual[0:length_snake]
    snake_virtual.reverse()

    return AStar(Grid(snake_virtual[-1][0], snake_virtual[-1][1]), Grid(snake_virtual[0][0] + 10, snake_virtual[0][1] + 10),
                 snake_virtual).pathFinding()


def moveOneStep(snake_body, path):
    print(path[0:2])  #################################################################
    global food_x, food_y
    head_move_x = snake_body[-1][0] + path[1][0] - path[0][0]
    head_move_y = snake_body[-1][1] + path[1][1] - path[0][1]

    if not inside(head_move_x, head_move_y) or [head_move_x, head_move_y] in snake_body:
        square(head_move_x, head_move_y, 10, "red")
        update()
        print("得分: ", len(snake))
        return

    snake.append([head_move_x, head_move_y])

    if head_move_x == food_x and head_move_y == food_y:
        if len(snake) == len(all_food):
            print("YOU WIN!")
            return
        else:
            food_x, food_y = new_food()
    else:
        snake.pop(0)
    clear()
    frame()
    for body in snake:
        square(body[0], body[1], 10, "black")
    square(food_x, food_y, 10, "green")
    update()
    x = path[1][0] - path[0][0]
    y = path[1][1] - path[0][1]
    change(x, y)


def main():
    setup(420, 420)
    title("贪吃蛇")
    hideturtle()
    tracer(False)
    while True:
        mainAlgorithm()
    done()


if __name__ == "__main__":
    main()
