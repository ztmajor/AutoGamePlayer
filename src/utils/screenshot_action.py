import pyautogui


im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot("./test.png")

# 如果不能获取应用内部截屏，这个会很有用
im = pyautogui.screenshot(region=(0, 0, 300, 400))


x, y = pyautogui.locateAllOnScreen()
x, y = pyautogui.locateCenterOnScreen()
pyautogui.locate(needleImage, haystackImage)
pyautogui.locateAll(needleImage, haystackImage)
# need pyGetwindow
pyautogui.locateOnWindow