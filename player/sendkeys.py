import ctypes
import win32gui
import win32api
import win32con
import time

SendInput = ctypes.windll.user32.SendInput
FindWindow = ctypes.windll.user32.FindWindowA
hwnd = FindWindow(None, b"ArkAscended")


class SendKeys:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        
    VK_A = 0x41
    VK_B = 0x42
    VK_C = 0x43
    VK_D = 0x44
    VK_E = 0x45
    VK_F = 0x46
    VK_G = 0x47
    VK_H = 0x48
    VK_I = 0x49
    VK_J = 0x4A
    VK_K = 0x4B
    VK_L = 0x4C
    VK_M = 0x4D
    VK_N = 0x4E
    VK_O = 0x4F
    VK_P = 0x50
    VK_Q = 0x51
    VK_R = 0x52
    VK_S = 0x53
    VK_T = 0x54
    VK_U = 0x55
    VK_V = 0x56
    VK_W = 0x57
    VK_X = 0x58
    VK_Y = 0x59
    VK_Z = 0x5A
    VK_0 = 0x30
    VK_1 = 0x31
    VK_2 = 0x32
    VK_3 = 0x33
    VK_4 = 0x34
    VK_5 = 0x35
    VK_6 = 0x36
    VK_7 = 0x37
    VK_8 = 0x38
    VK_9 = 0x39
    VK_SPACE = 0x20
    VK_ENTER = 0x0D
    VK_BACKSPACE = 0x08
    VK_TAB = 0x09
    VK_CAPS_LOCK = 0x14
    VK_SHIFT = 0x10 
    VK_RSHIFT = 0xA0 
    VK_CONTROL = 0x11 
    VK_RCONTROL = 0xA2 
    VK_ALT = 0x12 
    VK_RALT = 0xA4 
    WM_KEYPRESS = 0x0100
    WM_KEYUP = 0x0101

    def send_key_press(self, key_code):
        ctypes.windll.user32.PostMessageW(self.hwnd, self.WM_KEYPRESS, key_code, 0)
        
    def send_key_press_up(self, key_code):
        ctypes.windll.user32.PostMessageW(self.hwnd, self.WM_KEYPRESS, key_code, 0)
        ctypes.windll.user32.PostMessageW(self.hwnd, self.WM_KEYUP, key_code, 0)
        
    
    def send_word(self, word):
        for char in word:
            key_code = ord(char.upper())
            self.send_key_press(key_code)
            
    def send_tab(self):
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, self.VK_TAB, 0)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, self.VK_TAB, 0)
            
    def send_enter(self):
        time.sleep(0.1)
        win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        time.sleep(0.1)
        win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        time.sleep(0.1)
        
    def send_ctrl_v(self):
        win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_CONTROL, 0)
        win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, self.VK_V, 0)
        win32gui.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_CONTROL, 0)
        win32gui.PostMessage(hwnd, win32con.WM_KEYUP, self.VK_V, 0)
