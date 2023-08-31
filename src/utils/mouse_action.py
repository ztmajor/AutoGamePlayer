import time
import pyautogui


def doClick(cx, cy, press_time=0.2):
    pyautogui.moveTo(cx, cy)
    pyautogui.mouseDown()
    time.sleep(press_time)
    pyautogui.mouseUp()

    # or
    # pyautogui.click(cx, cy)

def eliminate(x1, y1, x2 ,y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.click()

    pyautogui.moveTo(x2, y2)
    pyautogui.click()


def drag(start, end, duration=2, button='left'):
    s_x, s_y = start
    e_x, e_y = end
    pyautogui.moveTo(s_x, s_y)
    pyautogui.dragTo(e_x, e_y, duration, button=button)     


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
