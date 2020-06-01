import pyautogui, os
os.chdir(r'C:\Users\zchen\OneDrive\Pictures')
pyautogui.screenshot('screenshot1.png') # saves screenshot as this
pyautogui.moveTo(pyautogui.locateCenterOnScreen('pic7.png'),duration=1)
