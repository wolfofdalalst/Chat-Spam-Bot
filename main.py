from time import sleep
from pyautogui import typewrite
from keyboard import is_pressed

print("PYTHON CHAT SPAMMER")
print("CLICK ON THE TEXT FIELD BEFORE TIME RUNS OUT")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = 'T - {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1

with open("./facts.txt", "r") as file:
    facts = file.readlines()

SAFE_KEY = "q"

print("ALERT: THE SAFE KEY IS 'q'. TERMINATE THE PROGRAM BY PRESSING IT")
countdown(10)
print("Fire in the hole!!!!")

for line in facts:
    sleep(1)
    typewrite(line)
    if is_pressed(SAFE_KEY):
        break

print("PROGRAM TERMINATED")