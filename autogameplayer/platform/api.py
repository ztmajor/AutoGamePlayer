import os
import time


def get_device_class(platform):
    platform = platform.lower()
    if platform == "windows":
        from autogameplayer.platform.win.windows import Windows as c
    else:
        raise RuntimeError(f"Unknown platform: {platform}")
    return c