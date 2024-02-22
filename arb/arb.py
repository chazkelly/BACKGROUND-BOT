from dino.dinoinventory import DinoInventory
from dino.dinoleveller import DinoLeveller
from player.sendkeys import SendKeys
import pyautogui
import pydirectinput as pdinput
import threading
import time

class Arb:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.stop_event = threading.Event()
        self.click_thread = None
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)
        
    def arb(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(1)
        # self.spark_craft()
        # time.sleep(170)
        # self.gunpowder_craft()       
        self.empty_chem_bench("powder")
        time.sleep(1)
        self.deposit_dedi()
        
        
    def spark_craft(self):
        self.spawn_bed("arb1")
        self.singleplayerbedshite()
        self.craft("spark")
        self.spawn_bed("arb2")
        self.singleplayerbedshite()
        self.craft("spark")
        self.spawn_bed("arb3")
        self.singleplayerbedshite()
        self.craft("spark")
        self.spawn_bed("arb4")
        self.singleplayerbedshite()
        self.craft("spark")
        self.spawn_bed("arb5")
        self.singleplayerbedshite()
        self.craft("spark")
        self.spawn_bed("arb6")
        self.singleplayerbedshite()
        self.craft("spark")
        
    def gunpowder_craft(self):
        self.spawn_bed("arb1")
        self.singleplayerbedshite()
        self.craft("gun")
        self.spawn_bed("arb2")
        self.singleplayerbedshite()
        self.craft("gun")
        self.spawn_bed("arb3")
        self.singleplayerbedshite()
        self.craft("gun")
        self.spawn_bed("arb4")
        self.singleplayerbedshite()
        self.craft("gun")
        self.spawn_bed("arb5")
        self.singleplayerbedshite()
        self.craft("gun")
        self.spawn_bed("arb6")
        self.singleplayerbedshite()
        self.craft("gun")

        
    def craft(self, craftselection):
        self.chem_bench(craftselection)
        time.sleep(0.5)
        pdinput.moveRel(-300, 0)
        time.sleep(0.1)
        self.chem_bench(craftselection)
        time.sleep(1)
        pdinput.moveRel(0, 1000)
        pyautogui.press("e")
        
    def chem_bench(self, craftselection):
        self.sendkeys.send_key_press_up(self.sendkeys.VK_F)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        time.sleep(0.05)
        self.sendkeys.send_word(craftselection)
        self.dinoleveller.start_click_loop(1250, 278, 1)
        pyautogui.moveTo(1250, 278)
        for i in range(10):
            self.sendkeys.send_key_press_up(self.sendkeys.VK_A)
            time.sleep(0.1)
        self.sendkeys.send_key_press_up(self.sendkeys.VK_F)
        
    def spawn_bed(self, bed_name):
        self.sendkeys.send_key_press_up(self.sendkeys.VK_E)
        while not self.dinoinventory.match_template_in_specific_area(290, 930, 200, 100, "templates/searchbed.png"):
            time.sleep(0.1)
        time.sleep(1)
        self.dinoleveller.click(370, 967)
        time.sleep(0.1)
        self.sendkeys.send_word(bed_name)
        time.sleep(2)
        self.dinoleveller.click(330, 220)
        time.sleep(1)
        self.dinoleveller.click(1650, 950)
        time.sleep(7)

    def singleplayerbedshite(self):
        time.sleep(0.1)
        pdinput.moveRel(0, 400)
        time.sleep(0.1)
        self.sendkeys.send_key_press(self.sendkeys.VK_E)
        time.sleep(0.3)
        pdinput.leftClick(1164, 461)
        time.sleep(1)
        pyautogui.press("e")
        time.sleep(0.5)
        pdinput.moveRel(-420, 0)
        
    def empty_chem_bench(self, resourceselection):
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(1278, 198, 1)
        self.sendkeys.send_word(resourceselection)
        time.sleep(0.1)
        self.dinoleveller.start_click_loop(1411, 198, 1)
        time.sleep(0.5)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
        
    def turn_90_left(self):
        pdinput.moveRel(-412, 0)
        
    def turn_90_right(self):
        pdinput.moveRel(412,0)
        
    def turn_180(self):
        pdinput.moveRel(824,0)
        
    def deposit_dedi(self):
        time.sleep(0.1)
        self.sendkeys.send_key_press(self.sendkeys.VK_C)
        self.turn_180()
        time.sleep(0.1)
        self.sendkeys.send_key_press(self.sendkeys.VK_F)
        while not self.dinoinventory.match_template_in_specific_area(1200, 100, 200, 100, "templates/inventory.png"):
            time.sleep(0.1)
        self.dinoleveller.start_click_loop(396, 196, 1)