import cv2
import numpy
import os
from PIL import Image

import win32gui, win32ui, win32con

def getAppScreen(hwnd):
    # 获取窗口大小
    _left, _top, _right, _bottom = win32gui.GetWindowRect(hwnd)
    width = _right - _left
    height = _bottom - _top

    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)

    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（width，height）的图片
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)

    # 保存图像
    #saveBitMap.SaveBitmapFile(saveDC, filename)
    # 获取位图信息
    signedIntsArray = saveBitMap.GetBitmapBits(True)

    ###获取位图信息
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    ###生成图像
    im_PIL = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd,hwndDC)

    # 生成图片
    img = numpy.frombuffer(signedIntsArray, dtype = 'uint8')
    img.shape = (height, width, 4)
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    return img, im_PIL
