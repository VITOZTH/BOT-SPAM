import pyautogui
import time
import keyboard

Spam = open("spam.txt","r", encoding='utf-8')
time.sleep(5) 

with open('spam.txt', encoding='utf-8') as f: 
    for copiar in f:
        keyboard.write(copiar, delay=0.5)
        pyautogui.typewrite(copiar)
        pyautogui.press("enter")
        time.sleep(5)












