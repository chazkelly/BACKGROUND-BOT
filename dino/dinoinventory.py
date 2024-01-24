import ctypes
import threading
from dino.dinoleveller import DinoLeveller
from player.sendkeys import SendKeys
import time
import cv2
import numpy as np
import pyautogui


PostMessage = ctypes.windll.user32.PostMessageA
SendInput = ctypes.windll.user32.SendInput
SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow


class DinoInventory:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.click_thread = None
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)

    def capture_specific_area(self, x, y, width, height):
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        return screenshot

    def match_template_in_specific_area(self, x, y, width, height, template_path):
        screenshot = self.capture_specific_area(x, y, width, height)

        template = cv2.imread(template_path)
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(
            gray_screenshot, gray_template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            print("Template found in the specified area.")
            return True
        else:
            return False

    def keep_meat_hide(self):
        self.dinoleveller.bring_to_foreground()
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
        time.sleep(0.1)
        while not self.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_key_press(self.sendkeys.VK_P)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("raw")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1410, 198, 1)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("hide")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1410, 198, 1)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.1)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def keep_metal(self):
        self.dinoleveller.bring_to_foreground()
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
        time.sleep(0.3)
        while not self.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("err")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("s")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("w")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("at")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.1)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
