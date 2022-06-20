import pyautogui
import time
start = time.time()
i = 0
while time.time()  - start <= 5:
    s = pyautogui.screenshot()
    i += 1
print(i)