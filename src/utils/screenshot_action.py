import time
import pyautogui
import pygetwindow
from pyautogui import locateOnScreen
# from mouse_action import doClick

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


def get_loc_on_screen(tgt_img, region, **kwargs):
    # pyautogui.screenshot(imageFilename='./test.png', region=region)
    pos_res = locateOnScreen(tgt_img, region=region, **kwargs)
    print("pos_res", pos_res)

    return pos_res
