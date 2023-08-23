import pyautogui

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

get_mouse_position()