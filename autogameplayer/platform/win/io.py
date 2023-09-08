import time
import pyautogui
import pygetwindow
from pyautogui import locateOnScreen


# === mouse action ===
def doClick(cx, cy, interval=0.1):
    """
    注意，pyautogui.click(interval)中的interval代表多次点击之间的间隔，本函数的
    interval表示按键按下与抬起之间的间隔(因为有时候点的太快模拟器响应有问题)
    """
    pyautogui.moveTo(cx, cy)
    pyautogui.mouseDown()
    time.sleep(interval)
    pyautogui.mouseUp()


def drag(start, end, duration=2, button='left'):
    #TODO: 测试该函数
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


def keyborad_press(key, interval=0.1):
    pyautogui.press(key)
    time.sleep(interval)    # 防止按太快


# === screen action ===
def get_window(title, maximize=False, moveTo=(0,0), save_path=None):
    """获取对应窗口的截图/在屏幕中位置"""
    matchingWindows = pygetwindow.getWindowsWithTitle(title)
    if len(matchingWindows) == 0:
        raise Exception('Could not find a window with %s in the title' % (title))
    elif len(matchingWindows) > 1:
        raise Exception(
            'Found multiple windows with %s in the title: %s' % (title, [str(win) for win in matchingWindows])
        )

    win = matchingWindows[0]
    win.activate()
    if maximize:
        win.maximize()
        print("maximize", win.isMaximized)
    if moveTo is not None:
        win.moveTo(moveTo)

    # sleep 为了等待activate响应，然后截屏，避免截到其他窗口
    time.sleep(1)

    if save_path is not None:
        pyautogui.screenshot(imageFilename=save_path, region=(win.left, win.top, win.width, win.height))

    return (win.left, win.top, win.width, win.height)


def get_loc_on_window(temp_img, title, center=True, **kwargs):
    """直接从窗口获取模板图片的位置"""
    pos = pyautogui.locateOnWindow(temp_img, title, **kwargs)

    if center:
        center_pos = pyautogui.center(pos) if pos is not None else None
        return center_pos
    else:
        return pos


def get_loc_on_screen(temp_img, region, save_path=None, center=True, **kwargs):
    """获取屏幕上模板图片的位置

    Args:
        temp_img (_type_): 模板图片，在screen上找该图片
        region (Tuple[int, int, int ,int]): 在整个屏幕上子区域的范围
        center (bool, optional): 是否返回中心坐标. Defaults to True.

    Returns:
        Tuple[int, int]: 返回坐标值
    """
    if save_path is not None:
        # 保存屏幕截图
        pyautogui.screenshot(imageFilename=save_path, region=region)
    
    # TODO: 此处代码需要测试
    pos = pyautogui.locateAllOnScreen(temp_img, region=region, **kwargs)
    # center_pos = pyautogui.locateCenterOnScreen(temp_img, region=region, **kwargs)

    if center:
        center_pos = pyautogui.center(pos) if pos is not None else None
        return center_pos
    else:
        return pos


def get_all_loc_on_screen(tgt_img, region, save_path=None, center=True, **kwargs):
    if save_path is not None:
        # 保存屏幕截图
        pyautogui.screenshot(imageFilename=save_path, region=region)
        
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
