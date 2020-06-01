import pyautogui
# pyautogui.click(500,500)
# pyautogui.typewrite('Hello World',0.2) # 2nd argument is duration
# special keys
print(pyautogui.KEYBOARD_KEYS) # lets you know how to press special keys
# pyautogui.typewrite(['left','left','abc'])
# pyautogui.press('f1')

# Hotkeys such as ctrlc, ctrlv
# lets you press it tgt
pyautogui.click(500,500)
pyautogui.dragRel(-200,0)
pyautogui.hotkey('ctrl','c')