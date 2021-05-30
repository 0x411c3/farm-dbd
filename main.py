import pyautogui
import time
from cv2 import cv2
import keyboard

ans=True
while ans:
    print ("""
    1.Start
    2.Discord
    3.Exit/Quit
    4.Tutorial
    """)
    ans=input('Type: ')
    if ans=="1": 
        last_time = time.time()
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(1)
        while(True):
            print('Loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            pyautogui.moveTo(1736, 1007, 1)
            pyautogui.moveTo(1649, 1012, 1)
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(2.5)
        # FICA CORRENDO
            pyautogui.keyDown("w")
            time.sleep(1.5)
            pyautogui.click()
            pyautogui.keyDown('left')
            time.sleep(1)
            pyautogui.keyUp('left')
            time.sleep(0.7)
            pyautogui.keyDown('d')
            time.sleep(0.7)
            pyautogui.keyDown('right')
            time.sleep(0.8)
            pyautogui.keyUp('right')
            time.sleep(0.5)

    elif ans=="2":
      print("\n memcpy#2707")
      break
    elif ans=="3":
      print("\n Goodbye") 
      break
    elif ans=="4":
      print("\n version to 1920x1080, you need to have the game currently open and in killer lobby to found a match") 
      break
    elif ans !="":
      print("\n Not Valid Choice Try again")
