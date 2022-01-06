import pyautogui
import time
import unicodedata

Spam = open("spam.txt","r", encoding='utf-8')
time.sleep(5) 

with open('spam.txt', encoding='utf-8') as f: 
    for copiar in f:
        print(copiar)
        pyautogui.typewrite(copiar)
        pyautogui.press("enter")
        time.sleep(5)










