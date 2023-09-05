import pyautogui
import sys
sys.path.append("/media/my/workspace/fun/AutoGamePlayer")
from autogameplayer.utils.mouse_action import get_mouse_position

print(pyautogui.size())
print(pyautogui.position())

get_mouse_position()