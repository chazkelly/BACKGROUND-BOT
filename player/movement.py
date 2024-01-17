from PIL import Image
import threading
import ctypes
import pyautogui

PostMessage = ctypes.windll.user32.PostMessageA

class Movement:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.click_thread = None
        
    def turn_90_degrees(self, direction):
        if direction == "left":
            pyautogui.moveTo(0, 0)
        elif direction == "right":
            pyautogui.moveTo(1919, 0)
        else:
            raise ValueError("Invalid direction: {}".format(direction))
        