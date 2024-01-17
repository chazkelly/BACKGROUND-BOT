import ctypes
import time
import threading

WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
MK_LBUTTON = 0x0001

PostMessage = ctypes.windll.user32.PostMessageA
SendInput = ctypes.windll.user32.SendInput
SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow


class DinoLeveller:
    def __init__(self, hwnd, clicker_button_callback=None):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.click_thread = None
        self.button_callback = clicker_button_callback

    def bring_to_foreground(self):
        if self.hwnd != 0:
            SetForegroundWindow(self.hwnd)
            return True
        else:
            print(f"Window with title '{self.hwnd}' not found.")
            return False

    def start_click_loop(self, x, y, clicks):
        self.bring_to_foreground()
        time.sleep(0.1)
        threading.Thread(target=self.click_loop, args=(x, y, clicks)).start()

    def click(self, x, y):
        client_point = ctypes.wintypes.POINT(x, y)
        ctypes.windll.user32.ScreenToClient(
            self.hwnd, ctypes.byref(client_point))
        PostMessage(self.hwnd, WM_LBUTTONDOWN, 1, ctypes.wintypes.LPARAM(
            client_point.y << 16 | client_point.x))
        PostMessage(self.hwnd, WM_LBUTTONUP, 0, ctypes.wintypes.LPARAM(
            client_point.y << 16 | client_point.x))

    def click_loop(self, x, y, clicks):
        for _ in range(clicks):
            self.click(x, y)
            time.sleep(0.01)

    def set_click_coordinates(self, x, y):
        self.click_coordinates = (x, y)
