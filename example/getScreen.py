import pyautogui
import pygetwindow
import time
import os


def get_pic_path(platform, mode, name):
    dir = r"E:\project\AutoGamePlayer\data\template\superWorld"
    return os.path.join(dir, platform, mode, f"{name}.png")


def get_loc_on_screen(tgt_img, region, **kwargs):
    # pyautogui.screenshot(imageFilename='./test.png', region=region)
    pos_res = pyautogui.locateOnScreen(tgt_img, region=region, **kwargs)

    return pos_res


def test_data(tgt_img, screen_region):
    img_loc = get_loc_on_screen(tgt_img, region=screen_region, confidence=0.9)

    if img_loc is not None:
        img_click_point = pyautogui.center(img_loc)
        x, y = img_click_point
        # doClick(x, y)

        im = pyautogui.screenshot(imageFilename='./test_region.png', region=img_loc)
        print("找到对应位置")
    else:
        print("未找到对应位置")


if __name__ == "__main__":
    # title = '腾讯手游助手【标准引擎】'
    title = '腾讯手游助手(64位)'
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
    print(win.isMaximized)
    win.moveTo(0, 0)
    time.sleep(1)

    screen_region = (win.left, win.top, win.width, win.height)
    pyautogui.screenshot(imageFilename='./test.png', region=screen_region)


    # target_img = get_pic_path(platform='app', mode='maincity', name='select_attack')
    # test_data(target_img, screen_region)

    # img_loc = get_loc_on_screen(target_img, region=(win.left, win.top, win.width, win.height), confidence=0.9)

    # if img_loc is not None:
    #     img_click_point = pyautogui.center(img_loc)
    #     x, y = img_click_point
    #     # doClick(x, y)

    #     im = pyautogui.screenshot(imageFilename='./test_region.png', region=img_loc)
    #     print("找到对应位置")
    # else:
    #     print("未找到对应位置")