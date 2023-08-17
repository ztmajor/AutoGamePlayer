import time
import random


def random_sleep(min=0.5, max=1., log=False):
    sleep_time = random.uniform(min, max)
    if log:
        print("sleep:", sleep_time)
    time.sleep(sleep_time)