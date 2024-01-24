from dino.dinoinventory import DinoInventory
from dino.dinoleveller import DinoLeveller
from player.sendkeys import SendKeys
import threading
import time
import tkinter as tk


import threading
import time

class InventoryHandler:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)

    def bring_to_foreground(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)

    def wait_for_inventory(self):
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)

    def perform_action(self, click_x, click_y, keyword, key_press=None):
        self.bring_to_foreground()
        time.sleep(0.1)
        self.wait_for_inventory()
        self.dinoleveller.start_click_loop(click_x, click_y, 1)
        self.sendkeys.send_word(keyword)
        if key_press:
            time.sleep(0.01)
            self.dinoleveller.start_click_loop(key_press[0], key_press[1], 1)
            time.sleep(0.01)
            self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def perform_loop(self, is_active, action_method, *args):
        while is_active:
            action_method(*args)
            time.sleep(1)
            if self.stop_event.is_set():
                break

class MagicF:
    def __init__(self, hwnd, magic_f_button_callback=None, selected_option=None):
        self.hwnd = hwnd
        self.inventory_handler = InventoryHandler(self.hwnd)
        self.stop_event = self.inventory_handler.stop_event
        self.button_callback = magic_f_button_callback
        self.selected_option = selected_option
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)

    def rawmeat(self):
        self.inventory_handler.perform_action(256, 198, "raw", (385, 198))

    def berries(self):
        self.inventory_handler.perform_action(256, 198, "berry", (385, 198))

    def paste(self):
        self.inventory_handler.perform_action(1278, 198, "paste", (1458, 198))

    def takeall(self):
        self.inventory_handler.perform_action(1412, 198, "takeall")

    def cropplot(self):
        self.inventory_handler.perform_action(1412, 198, "cropplot", (386, 198))

    def rawmeat_loop(self, is_rawmeat_active):
        self.inventory_handler.perform_loop(is_rawmeat_active, self.rawmeat)
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(256, 198, 1)
        self.sendkeys.send_word("raw")
        self.dinoleveller.start_click_loop(385, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def berries(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(256, 198, 1)
        self.sendkeys.send_word("berry")
        self.dinoleveller.start_click_loop(385, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def paste(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
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
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1412, 198, 1)
        time.sleep(0.01)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def cropplot(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1412, 198, 1)
        time.sleep(0.5)
        self.dinoleveller.start_click_loop(386, 198, 1)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)

    def rawmeat_loop(self, is_rawmeat_active):
        while True:
            self.rawmeat()
            time.sleep(1)
            if self.stop_event.is_set():
                break

    def berry_loop(self, is_berry_active):
        self.inventory_handler.perform_loop(is_berry_active, self.berries)

    def paste_loop(self, is_paste_active):
        self.inventory_handler.perform_loop(is_paste_active, self.paste)

    def takeall_loop(self, is_takeall_active):
        self.inventory_handler.perform_loop(is_takeall_active, self.takeall)

    def cropplot_loop(self, is_cropplot_active):
        self.inventory_handler.perform_loop(is_cropplot_active, self.cropplot)