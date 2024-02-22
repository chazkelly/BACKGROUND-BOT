from dino.dinoinventory import DinoInventory
from inventorymacro.inventory import InventoryHandler
from dino.dinoleveller import DinoLeveller
from logs.logcapture import Logging
from arb.arb import Arb
from player.sendkeys import SendKeys
from snails.snailembed import Discord
import pyautogui
import pydirectinput as pdinput
import threading
import time
import cv2
import pytesseract
from PIL import Image, ImageFilter, ImageFilter
import re

class Snail:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.click_thread = None
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)
        self.arb = Arb(self.hwnd)
        self.inventoryhandler = InventoryHandler(self.hwnd)
        self.snail = Discord(hwnd)
        self.logs = Logging(self.hwnd)
                
        
        
    def empty_snail(self, num_snails):
        duration_in_seconds = 8 * 60 * 60
        start_time = time.time()
        
        while time.time() - start_time < duration_in_seconds:
            self.dinoleveller.bring_to_foreground()
            for i in range(num_snails):
                station_number = "snail" + str(i).zfill(2)
                loop_start_time = time.time()
                self.arb.spawn_bed("snail" + str(i).zfill(2))
                pyautogui.press("c")
                pdinput.moveRel(0, 100)
                for i in range (4):
                    time.sleep(0.3)
                    self.take_paste()
                    time.sleep(0.7)
                    self.arb.turn_90_right()
                    
                pdinput.moveRel(-200, 0)
                time.sleep(0.5)
                self.sendkeys.send_key_press(self.sendkeys.VK_F)
                while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
                    time.sleep(0.1)
                time.sleep(0.1)
                self.dinoleveller.start_click_loop(386, 198, 1)
                time.sleep(0.1)
                self.sendkeys.send_key_press(self.sendkeys.VK_F)
                self.dinoinventory.capture_specific_area(0, 520, 400, 100)
                time.sleep(0.4)
                # self.get_paste_amount()
                deposited_paste = self.get_paste_amount()
                time.sleep(1)
                self.sendkeys.send_key_press_up(self.sendkeys.VK_L)
                time.sleep(1)
                self.logs.send_logs()
                time.sleep(1.5)
                self.dinoleveller.start_click_loop(1799, 65, 1)
                loop_end_time = time.time()
                loop_elapsed_time = loop_end_time - loop_start_time
                station_time = round(loop_elapsed_time, 1)
                self.snail.discord_embed(station_time, deposited_paste, station_number)
                time.sleep(0.5)
                pdinput.moveRel(-200, 1000)
                self.sendkeys.send_key_press_up(self.sendkeys.VK_X)
                time.sleep(0.1)
            self.arb.spawn_bed("suicide")
            time.sleep(30)
            self.suicide_spawn_bed("snailstart")
            time.sleep(10)
            pdinput.moveRel(-200, 1000)  
        print("Loop completed after 8 hours.")
        
        
        
    def suicide_spawn_bed(self, bed_name):
        self.sendkeys.send_key_press_up(self.sendkeys.VK_E)
        while not self.dinoinventory.match_template_in_specific_area(100, 930, 200, 100, "templates/searchbed.png"):
            time.sleep(0.1)
        time.sleep(1)
        self.dinoleveller.click(167, 967)
        time.sleep(0.1)
        self.sendkeys.send_word(bed_name)
        time.sleep(2)
        self.dinoleveller.click(330, 220)
        time.sleep(1)
        self.dinoleveller.click(1650, 950)
        time.sleep(7)
    
    def get_paste_amount(self):
        screenshot = self.dinoinventory.capture_specific_area(0, 520, 400, 100)
        img = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(img)
        removed_match = re.search(r'REMOVED:\s*(\d+)', text)
        removed_amount = None
        
        if removed_match:
            removed_amount = removed_match.group(1)
            print("Removed Amount:", removed_amount)
        else:
            print("No removed amount found.")
        # cv2.imshow("screenshot", img)
        # cv2.waitKey(0)
        return removed_amount
    
    def take_paste(self):
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
        start_time = time.time()
        
        while time.time() - start_time < 10:
            if self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
                self.dinoleveller.start_click_loop(1278, 198, 1)
                self.sendkeys.send_word("paste")
                time.sleep(0.5)
                self.dinoleveller.start_click_loop(1410, 198, 1)
                time.sleep(0.1)
                self.sendkeys.send_key_press(self.sendkeys.VK_F)
                break
            time.sleep(0.1)
        else:
            print("Template not found within the timeout period.")