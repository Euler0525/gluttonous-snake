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
    tail_path = AStar(Grid(snake[-1][0], snake[-1][1]), Grid(snake[0][0], snake[0][1]), snake).pathFinding()
    if len(food_path) != 0:
        tmp = moveVirtual(deepcopy(snake), deepcopy(food_path))
        if len(tmp) != 0:
            moveOneStep(snake, food_path)
        else:
            moveOneStep(snake, tail_path)
    else:
        moveOneStep(snake, tail_path)


def moveVirtual(snake_virtual, path_virtual) -> list[list]:
    snake_virtual.reverse()
    path_virtual.reverse()
    length_snake = len(snake_virtual)
    length_path = len(path_virtual)

    if length_snake > length_path:
        snake_virtual = path_virtual + snake_virtual[length_path:length_snake - length_path + 1]
    else:
        snake_virtual = path_virtual[0:length_snake]
    snake_virtual.reverse()

    return AStar(Grid(snake_virtual[-1][0], snake_virtual[-1][1]), Grid(snake_virtual[0][0], snake_virtual[0][1]),
                 snake_virtual).pathFinding()


def moveOneStep(snake_body, path):
    pass