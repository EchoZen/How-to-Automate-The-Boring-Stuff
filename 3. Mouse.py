# in pyautogui, pixels 0,0 start from top left corner
# x increase left to right, y increase up to down
import pyautogui
# print(pyautogui.size()) # Gives width and size of screen
width, height= pyautogui.size() # assign w and h
# print(pyautogui.position()) # Tells you position of mouse
pyautogui.moveTo(100,300,1.5) # Move to those coordinates. Last argument is how long it takes
pyautogui.moveRel(0,-100,1) # Moves upwards
# Lets you click
pyautogui.click() # Can key in coordinates to click as well

# Go to command line 'python'
# pyautogui.displayMouseposition()
# shows you mouse positions and rgbs
