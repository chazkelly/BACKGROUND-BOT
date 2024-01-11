import ctypes
import time
import threading
import win32api
import win32con

WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
MK_LBUTTON = 0x0001

PostMessage = ctypes.windll.user32.PostMessageA
FindWindow = ctypes.windll.user32.FindWindowA

class AutoClicker:
    def __init__(self, hwnd, clicker_button_callback=None):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.click_thread = None
        self.button_callback = clicker_button_callback

    def toggle_clicking(self):
        if not self.is_clicking():
            self.start_clicking()
        else:
            self.stop_clicking()

    def is_clicking(self):
        return self.click_thread and self.click_thread.is_alive()

    def start_clicking(self):
        self.stop_event.clear()
        self.click_thread = threading.Thread(target=self.click_loop)
        self.click_thread.start()
        self.update_button_text("Stop Clicking")

    def stop_clicking(self):
        self.stop_event.set()
        if self.click_thread and self.click_thread.is_alive():
            self.click_thread.join()
        self.update_button_text("Start Clicking")

    def click_loop(self):
        while not self.stop_event.is_set():
            PostMessage(self.hwnd, WM_LBUTTONDOWN, MK_LBUTTON, 0)
            PostMessage(self.hwnd, WM_LBUTTONUP, MK_LBUTTON, 0)
            time.sleep(0.1)

    def update_button_text(self, text):
        if self.button_callback:
            self.button_callback(text)
            
