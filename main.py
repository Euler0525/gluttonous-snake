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
    ################################################################################
    print(food_path)
    print(tail_path)
    ################################################################################
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
    ################################################################################
    print(path_virtual)
    ################################################################################

    return AStar(Grid(snake_virtual[-1][0], snake_virtual[-1][1]), Grid(snake_virtual[0][0], snake_virtual[0][1]),
                 snake_virtual).pathFinding()


def moveOneStep(snake_body, path):
    global food_x, food_y
    head_move_x = snake_body[-1][0] + path[1][0] - path[0][0]
    head_move_y = snake_body[-1][1] + path[1][1] - path[0][1]

    # 判断是否撞到边框或者撞到自己
    if not inside(head_move_x, head_move_y) or [head_move_x, head_move_y] in snake_body:
        square(head_move_x, head_move_y, 10, "red")
        update()
        print("得分: ", len(snake))
        return

    snake.append([head_move_x, head_move_y])

    # 判断是否吃到食物以及是否胜利
    if head_move_x == food_x and head_move_y == food_y:
        if len(snake) == len(all_food):
            print("YOU WIN!")
            return
        else:
            food_x, food_y = new_food()
    else:
        snake.pop(0)
    clear()
    # 绘制边框, 蛇和食物
    frame()
    for body in snake:
        square(body[0], body[1], 10, "black")
    square(food_x, food_y, 10, "green")
    update()
    # 根据得分调节速度, 每到达一定分数会提高速度
    x = path[1][0] - path[0][0]
    y = path[1][1] - path[0][1]
    change(x, y)
    if len(snake) < 10:
        ontimer(move, 40)
    elif len(snake) < 20:
        ontimer(move, 30)
    elif len(snake) < 30:
        ontimer(move, 20)
    elif len(snake) < 40:
        ontimer(move, 10)
    else:
        ontimer(move, 0)


def main():
    setup(420, 420)
    title("贪吃蛇")
    hideturtle()
    tracer(False)
    mainAlgorithm()
    done()


if __name__ == "__main__":
    main()
