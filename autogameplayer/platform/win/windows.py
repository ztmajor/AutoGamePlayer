from pywinauto.application import Application
from pywinauto import mouse, keyboard


#TODO: 参考airtest
class Windows(object):
    """Windows client."""

    def __init__(self, handle=None, dpifactor=1, **kwargs):
        super(Windows, self).__init__()
        self.app = None
        self.handle = int(handle) if handle else None
        # windows high dpi scale factor, no exact way to auto detect this value for a window
        # reference: https://msdn.microsoft.com/en-us/library/windows/desktop/mt843498(v=vs.85).aspx
        self._dpifactor = float(dpifactor)
        self._app = Application()
        self._top_window = None
        self._focus_rect = (0, 0, 0, 0)
        self.mouse = mouse
        self.keyboard = keyboard
        self._init_connect(handle, kwargs)

        self.screen = mss.mss()
        self.monitor = self.screen.monitors[0]  # 双屏的时候，self.monitor为整个双屏
        self.main_monitor = self.screen.monitors[1]  # 双屏的时候，self.main_monitor为主屏