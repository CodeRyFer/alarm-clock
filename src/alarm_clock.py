import pygame
import time

def alarm(seconds):
    time_elapse = 0

    while time_elapse < seconds:
        time.sleep(1)
        time_elapse += 1

        time_left = seconds - time_elapse
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{minutes_left:02d}:{seconds_left:02d}")

