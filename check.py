import pyautogui
import time

print("Move your mouse to the target button in 3 seconds...")
time.sleep(3)
x, y = pyautogui.position()
print(f"Target Coordinates: X={x}, Y={y}")
# Write these numbers down to put in the main script below!