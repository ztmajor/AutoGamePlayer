import time
import pyautogui


def doClick(cx, cy):
    pyautogui.moveTo(cx, cy)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

    # or
    # pyautogui.click(cx, cy)

def eliminate(x1, y1, x2 ,y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.click()

    pyautogui.moveTo(x2, y2)
    pyautogui.click()


def drag():
    pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
    pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
    pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button


def get_mouse_position():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            # \b 表示退格键（backspace）
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')
