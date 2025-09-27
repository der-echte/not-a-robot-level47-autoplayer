import pyautogui
import keyboard
import time

columns = [
    (790, 625),
    (900, 625),
    (1010, 625),
    (1120, 625)
]

keys = ["left", "down", "up", "right"]

target_color = (255, 255, 255)

def color_match(c1, c2, tolerance=150):
    return all(abs(a-b) <= tolerance for a, b in zip(c1, c2))

was_block = [False, False, False, False]

print("Starts in 3 seconds")
time.sleep(3)

try:
    while True:
        for i, (x, y) in enumerate(columns):
            pixel = pyautogui.pixel(x, y)
            is_block = color_match(pixel, target_color)

            if is_block and not was_block[i]:
                print(f"Drücke: {keys[i]}")
                keyboard.press_and_release(keys[i])

            was_block[i] = is_block
except KeyboardInterrupt:
    print("Exit")
