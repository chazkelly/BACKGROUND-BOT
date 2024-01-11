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
        
        
