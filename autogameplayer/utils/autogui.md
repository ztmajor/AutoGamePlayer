[toc]

# pyautogui
## mouse
https://pyautogui.readthedocs.io/en/latest/mouse.html

```
click()                 # click the mouse
    x, y                # move to (x, y) and then click
    button              # left, middle, right
    interval            # 间隔，在多次点击之间
    clicks              # 点击数
doubleClick()
tripleClick()
rightClick()
    >>> pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
    >>> pyautogui.mouseDown(button='right')  # press the right button down
    >>> pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.

moveTo()                # 移动到特定位置，x or y 取None表示为当前鼠标在的x or y
    >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
    >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
    >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
    >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
    >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end
move()                  # 相对移动

dragTo()
drag()
    >>> pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
    >>> pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
    >>> pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button

scroll()                #鼠标滚动
    >>> pyautogui.scroll(10)   # scroll up 10 "clicks"
    >>> pyautogui.scroll(-10)  # scroll down 10 "clicks"
    >>> pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"
    在 OS X 和 Linux 平台上，PyAutoGUI 还可以通过调用 hscroll() 函数来执行水平滚动。例如：
    >>> pyautogui.hscroll(10)   # scroll right 10 "clicks"
    >>> pyautogui.hscroll(-10)   # scroll left 10 "clicks"
```

## keyboard
https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
```
write()
    str
    interval

press()
    >>> pyautogui.press('enter')  # press the Enter key
    >>> pyautogui.press('f1')     # press the F1 key
    >>> pyautogui.press('left')   # press the left arrow key
    >>> pyautogui.press(['left', 'left', 'left'])   # press multiple keys
    >>> pyautogui.press('left', presses=3)
keyDown()
keyUp()
    >>> pyautogui.keyDown('shift')  # hold down the shift key
    >>> pyautogui.press('left')     # press the left arrow key
    >>> pyautogui.press('left')     # press the left arrow key
    >>> pyautogui.press('left')     # press the left arrow key
    >>> pyautogui.keyUp('shift')    # release the shift key

hold()
    >>> with pyautogui.hold('shift'):
        pyautogui.press(['left', 'left', 'left'])
holdkey()
    >>> pyautogui.hotkey('ctrl', 'shift', 'esc')
```

## screen shot
https://pyautogui.readthedocs.io/en/latest/screenshot.html
```
screenshot()
    >>> im1 = pyautogui.screenshot()
    >>> im2 = pyautogui.screenshot('my_screenshot.png')
    >>> im = pyautogui.screenshot(region=(0,0, 300, 400))

locateOnScreen()
center()
    >>> button7location = pyautogui.locateOnScreen('calc7key.png')
    >>> button7location
    Box(left=1416, top=562, width=50, height=41)
    >>> button7location[0]
    1416
    >>> button7location.left
    1416
    >>> button7point = pyautogui.center(button7location)
    >>> button7point
    Point(x=1441, y=582)
    >>> button7point[0]
    1441
    >>> button7point.x
    1441
    >>> button7x, button7y = button7point
    >>> pyautogui.click(button7x, button7y)  # clicks the center of where the 7 button was found
    >>> pyautogui.click('calc7key.png') # a shortcut version to click on the center of where the 7 button was found

    confidence(Note: You need to have OpenCV installed for the confidence keyword to work.)
    >>> button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)
    >>> button7location
    Box(left=1416, top=562, width=50, height=41)

locateCenterOnScreen()      #  combines locateOnScreen() and center()
locateOnScreen()
locateCenterOnScreen()
locateAllOnScreen()
    >>> for pos in pyautogui.locateAllOnScreen('someButton.png')
    ...   print(pos)
    ...
    (1101, 252, 50, 50)
    (59, 481, 50, 50)
    (1395, 640, 50, 50)
    (1838, 676, 50, 50)
    >>> list(pyautogui.locateAllOnScreen('someButton.png'))
    [(1101, 252, 50, 50), (59, 481, 50, 50), (1395, 640, 50, 50), (1838, 676, 50, 50)]
locate()
locateAll()

locateOnWindow              # need pyGetwindow
```

### 灰度匹配 Grayscale Matching
https://pyautogui.readthedocs.io/en/latest/screenshot.html

Optionally, you can pass grayscale=True to the locate functions to give a slight speedup (about 30%-ish). This desaturates the color from the images and screenshots, speeding up the locating but potentially causing false-positive matches.

    >>> import pyautogui
    >>> button7location = pyautogui.locateOnScreen('calc7key.png', grayscale=True)
    >>> button7location
    (1416, 562, 50, 41)

### 像素匹配 Pixel Matching
To obtain the RGB color of a pixel in a screenshot, use the Image object’s getpixel() method:

```    
>>> import pyautogui
>>> im = pyautogui.screenshot()
>>> im.getpixel((100, 200))
(130, 135, 144)
```

Or as a single function, call the pixel() PyAutoGUI function, which is a wrapper for the previous calls:
```
>>> import pyautogui
>>> pix = pyautogui.pixel(100, 200)
>>> pix
RGB(red=130, green=135, blue=144)
>>> pix[0]
130
>>> pix.red
130
```

If you just need to verify that a single pixel matches a given pixel, call the pixelMatchesColor() function, passing it the X coordinate, Y coordinate, and RGB tuple of the color it represents:

```
>>> import pyautogui
>>> pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))
True
>>> pyautogui.pixelMatchesColor(100, 200, (0, 0, 0))
False
```

The optional tolerance keyword argument specifies how much each of the red, green, and blue values can vary while still matching:

```
>>> import pyautogui
>>> pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))
True
>>> pyautogui.pixelMatchesColor(100, 200, (140, 125, 134))
False
>>> pyautogui.pixelMatchesColor(100, 200, (140, 125, 134), tolerance=10)
True
```

# pygetwindow
```
注意：
#tdxW1.resizeTo(795,526)  #TdxW原始恢复窗口大小(795,526)

深入：
无以下方法：
#tdxW1.focus()
#gw.getFocusedWindow()

```

```
import pygetwindow as gw

print(gw.getAllTitles())        #获取所有应用程序名称
print(gw.getAllWindows())       #获取所有进程
print(gw.getWindowsAt(10, 10))  #获取指定区域进程



print(gw.getWindowsWithTitle('通达信金融终端V7.46')[0])
print(gw.getWindowsWithTitle('通达信金融终端V7.46')[1])



for tdxW in gw.getWindowsWithTitle('通达信金融终端V7.46'):
    print(tdxW)

tdxW1=gw.getWindowsWithTitle('通达信金融终端V7.46')[0]

tdxW1.maximize()            #窗口最大化
print(tdxW1.isMaximized)    #判定是否最大化窗口

tdxW1.minimize()            #窗口最小化
print(tdxW1.isMinimized)    #判定是否最小化窗口

tdxW1.maximize()
tdxW1.restore()             #窗口恢复之前

tdxW1.moveTo(400,50)        #窗口移动到绝对目标
tdxW1.moveRel(50,-100)       #窗口移动相对位置

#tdxW1.resizeTo(795,526)     #改变窗口大小绝对值     
#tdxW1.resizeRel(10,10)      #改变窗口大小相对值
print(tdxW1.size)           #窗口大小

print(tdxW1.width)          #窗口宽度
print(tdxW1.height)         #窗口高度

print(tdxW1.left)           #窗口左坐标
print(tdxW1.top)            #创欧上坐标
print(tdxW1.topleft)        #窗口左上角坐标
print(tdxW1.topright)       #窗口右上角坐标

print(tdxW1.right)          #窗口右坐标
print(tdxW1.bottom)         #窗口下坐标
print(tdxW1.bottomleft)     #窗口左下坐标
print(tdxW1.bottomright)    #窗口右下坐标


#tdxW1.close()

```


