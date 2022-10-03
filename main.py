from snake import *
from pykeyboard import PyKeyboard


def main():
    k = PyKeyboard()
    setup(420, 420)
    title("贪吃蛇")
    hideturtle()
    tracer(False)

    while all_food:
        obj = AStar(Grid(0, 0), Grid(food_x, food_y), snake)
        path = obj.pathFinding()
        i = 0
        listen()
        while i < len(path) - 1:
            print(path[i + 1], path[i])
            if path[i + 1][0] - path[i][0] > 0:
                k.press_key(k.right_key)
                onkey(lambda: change(10, 0), "Right")
                k.release_key(k.right_key)
            elif path[i + 1][0] - path[i][0] < 0:
                k.press_key(k.left_key)
                onkey(lambda: change(-10, 0), "Left")
                k.release_key(k.left_key)
            elif path[i + 1][1] - path[i][1] > 0:
                k.press_key(k.up_key)
                onkey(lambda: change(0, 10), "Up")
                k.release_key(k.up_key)
            else:
                k.press_key(k.down_key)
                onkey(lambda: change(0, -10), "Down")
                k.release_key(k.down_key)
            move()
        done()


if __name__ == "__main__":
    main()
