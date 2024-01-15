from dino.dinoinventory import DinoInventory
from dino.dinoleveller import DinoLeveller
from player.sendkeys import SendKeys
import threading
import time
import tkinter as tk


class MagicF:
    def __init__(self, hwnd, magic_f_button_callback=None, selected_option=None):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.magicf_thread = None
        self.button_callback = magic_f_button_callback
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)
        self.selected_option = selected_option

    def rawmeat(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, r"C:\Users\Charlie\Documents\GitHub\BACKGROUND BOT\templates\inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(256, 198, 1)
        self.sendkeys.send_word("raw")
        self.dinoleveller.start_click_loop(385, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def berries(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, r"C:\Users\Charlie\Documents\GitHub\BACKGROUND BOT\templates\inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(256, 198, 1)
        self.sendkeys.send_word("berry")
        self.dinoleveller.start_click_loop(385, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def paste(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, r"C:\Users\Charlie\Documents\GitHub\BACKGROUND BOT\templates\inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word("paste")
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1458, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def takeall(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, r"C:\Users\Charlie\Documents\GitHub\BACKGROUND BOT\templates\inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1412, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def cropplot(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, r"C:\Users\Charlie\Documents\GitHub\BACKGROUND BOT\templates\inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1412, 198, 1)
        time.sleep(0.5)
        self.dinoleveller.start_click_loop(386, 198, 1)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def rawmeat_loop(self, is_rawmeat_active):
        while is_rawmeat_active:
            self.rawmeat()
            time.sleep(1)
            if self.stop_event.is_set():
                break

    def berry_loop(self, is_berry_active):
        while is_berry_active:
            self.berries()
            time.sleep(1)
            if self.stop_event.is_set():
                break

    def paste_loop(self, is_paste_active):
        while is_paste_active:
            self.paste()
            time.sleep(1)
            if self.stop_event.is_set():
                break

    def takeall_loop(self, is_takeall_active):
        while is_takeall_active:
            self.takeall()
            time.sleep(1)
            if self.stop_event.is_set():
                break

    def cropplot_loop(self, is_cropplot_active):
        while is_cropplot_active:
            self.cropplot()
            time.sleep(1)
            if self.stop_event.is_set():
                break
