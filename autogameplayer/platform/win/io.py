import time
import pyautogui
import pygetwindow
from pyautogui import locateOnScreen


# === mouse action ===
def doClick(cx, cy, press_time=0.2):
    pyautogui.moveTo(cx, cy)
    pyautogui.mouseDown()
    time.sleep(press_time)
    pyautogui.mouseUp()


def drag(start, end, duration=2, button='left'):
    s_x, s_y = start
    e_x, e_y = end
    pyautogui.moveTo(s_x, s_y)
    pyautogui.dragTo(e_x, e_y, duration, button=button)     


def eliminate(x1, y1, x2 ,y2):
    """消除操作"""
    pyautogui.moveTo(x1, y1)
    pyautogui.click()

    pyautogui.moveTo(x2, y2)
    pyautogui.click()


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


# === keyboard action ===
keyboard_keys = [
    '\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright'
]

def ctrl_c():
    flag = input("warning! ctrl c option is dinguous, do you want to contine?(yes/no)?\n")
    if flag is False:
        return
    with pyautogui.hold('shift'):
        pyautogui.press('c')


def keyborad_press(key):
    pyautogui.press(key)


# === screen action ===
def test():
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot("./test.png")

    # 如果不能获取应用内部截屏，这个会很有用
    im = pyautogui.screenshot(region=(0, 0, 300, 400))


    x, y = pyautogui.locateAllOnScreen()
    x, y = pyautogui.locateCenterOnScreen()
    pyautogui.locate(needleImage, haystackImage)
    pyautogui.locateAll(needleImage, haystackImage)


def get_loc_on_backgroud_debug(target_img, title, **kwargs):
    # need pyGetwindow
    # pos_res = pyautogui.locateOnWindow(target_img, title)

    matchingWindows = pygetwindow.getWindowsWithTitle(title)
    if len(matchingWindows) == 0:
        raise Exception('Could not find a window with %s in the title' % (title))
    elif len(matchingWindows) > 1:
        raise Exception(
            'Found multiple windows with %s in the title: %s' % (title, [str(win) for win in matchingWindows])
        )

    win = matchingWindows[0]
    win.activate()
    # win.maximize()
    # print(win.isMaximized)
    win.moveTo(0, 0)

    # sleep 为了等待activate响应，然后截屏，避免截到其他窗口
    time.sleep(1)

    pyautogui.screenshot(imageFilename='./test.png', region=(win.left, win.top, win.width, win.height))
    pos_res = locateOnScreen(target_img, region=(win.left, win.top, win.width, win.height), **kwargs)
    print("pos_res", pos_res)

    return pos_res


def get_loc_on_screen(tgt_img, region, center=True, **kwargs):
    pyautogui.screenshot(imageFilename='./test.png', region=region)
    pos_res = pyautogui.locateOnScreen(tgt_img, region=region, **kwargs)

    
    # pos_res = pyautogui.locateCenterOnScreen(tgt_img, region=region, **kwargs)
    # print("pos_res", pos_res)
    if center:
        center_pos = pyautogui.center(pos_res) if pos_res is not None else None
        return center_pos
    else:
        return pos_res


def get_all_loc_on_screen(tgt_img, region, center=True, **kwargs):
    pos_res_list = pyautogui.locateAllOnScreen(tgt_img, region=region, **kwargs)

    if center:
        if pos_res_list is None:
            return None
        center_pos = []
        for pos_res in pos_res_list:
            center_pos.append(pyautogui.center(pos_res))
        return center_pos
    else:
        return pos_res_list
