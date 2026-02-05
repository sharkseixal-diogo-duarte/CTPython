import pyautogui
from time import sleep
def youtube():
    pyautogui.press("win")
    sleep(1)
    pyautogui.write("chrome")
    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.write("youtube.com")
    sleep(1)
    pyautogui.press("enter")
youtube()