import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapse = 0

    print(CLEAR)
    while time_elapse < seconds:
        time.sleep(1)
        time_elapse += 1

        time_left = seconds - time_elapse
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")

    pygame.mixer.init()
    pygame.mixer.music.load("alarm-clock/src/Alarm-Fast-High-Pitch-A3-www.fesliyanstudios.com.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)