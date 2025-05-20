import pyautogui
import getpass
user_name = input("Escreva o email: ")
pass_word = getpass.getpass("Escreva a password: ")
pyautogui.PAUSE=1.5
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("outlook")
pyautogui.press("enter")
pyautogui.click(230,300)
pyautogui.write(user_name)
pyautogui.press("enter")
pyautogui.write(pass_word)
pyautogui.press("enter")
