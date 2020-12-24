from time import sleep
from pyautogui import typewrite
from keyboard import is_pressed

file = open("facts.txt", "r")
facts = file.readlines()
file.close()

SAFE_KEY = "q"

sleep(10)

for line in facts:
    sleep(0.5)
    typewrite(line)
    if is_pressed(SAFE_KEY):
        break
