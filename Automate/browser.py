import pyautogui
import threading
import os


def open_browser():
    os.sytstem('start https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fi0.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F000%2F091%2FTrollFace.jpg&f=1')
    timer = threading.Timer(1, open_browser)
    timer.start()

pyautogui.FAILSAFE = False
open_browser()

while True:
    pyautogui.moveTo(400, 300)