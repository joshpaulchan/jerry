#! usr/bin/python

import pyautogui
import math

def main():
    """
    `main`

    Moves the mouse in a circle
    """
    i = 0
    v = 20
    while True:
        x = (a * math.cos(i * m)) + b
        y = (a * math.sin(i * m)) + b
        # print("At: ({},{})".format(x, y))
        pyautogui.moveTo(x, y)
        v += 1
        i += k * abs(v * math.sin(math.pi / 28))

if __name__ == '__main__':
    # pyautogui config
    pyautogui.PAUSE = 0

    # sine funciton config
    screenWidth, screenHeight = pyautogui.size()
    a = screenHeight * 0.33
    k = 20
    m = 2 * math.pi / screenWidth
    b = (screenHeight / 2)

    # start program
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye")
