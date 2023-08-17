import pyautogui

def doClick(cx, cy):
    pyautogui.moveTo(cx, cy)
    pyautogui.click()

    # or
    # pyautogui.click(cx, cy)

def eliminate(x1, y1, x2 ,y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.click()

    pyautogui.moveTo(x2, y2)
    pyautogui.click()