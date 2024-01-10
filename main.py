import tkinter as tk
from tkinter import ttk
from clicker.autoclicker import AutoClicker
from logs.logcapture import Logging
from capturescreen.capturescreen import Capture
from player.movement import Movement
from player.sendkeys import SendKeys
from dino.dinoleveller import DinoLeveller
from ini.ini import Ini
from dino.dinoinventory import DinoInventory
import keyboard

import ctypes

FindWindow = ctypes.windll.user32.FindWindowA
PostMessage = ctypes.windll.user32.PostMessageA


class AutoClickerGUI:
    def __init__(self):
        self.hwnd = FindWindow(None, b"ArkAscended")
        self.auto_clicker = AutoClicker(self.hwnd)
        self.logscapture = Logging()
        self.capturescreen = Capture()
        self.player = Movement(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.ini = Ini(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)

        self.root = tk.Tk()
        self.root.title("ASA Background Automation")
        self.root.geometry("400x400")

        self.notebook = ttk.Notebook(self.root)

        # Tab 1: Background
        self.background_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.background_tab, text='Background')

        self.auto_clicker = AutoClicker(
            self.hwnd, clicker_button_callback=self.update_clicker_button_text)
        self.logscapture = Logging(
            log_button_callback=self.update_log_button_text)

        self.click_button = ttk.Button(
            self.background_tab, text="Start Clicking", command=self.auto_clicker.toggle_clicking)
        self.click_button.pack(pady=5)

        self.logs_button = ttk.Button(
            self.background_tab, text="Start sending logs to discord", command=self.logscapture.toggle_capture_logs)
        self.logs_button.pack(pady=5)

        # Tab 2: Dino Leveller
        self.dino_leveller = ttk.Frame(self.notebook)
        self.notebook.add(self.dino_leveller, text='Dino Leveller')
        
        self.dino_hp_level_button = ttk.Button(
            self.dino_leveller, text="Level Dino HP - F4", command=lambda: self.dinoleveller.start_click_loop(1126, 505, 100))
        self.dino_hp_level_button.pack(pady=5)
        keyboard.add_hotkey("F4", lambda: self.dinoleveller.start_click_loop(1126, 505, 100))

        self.dino_melee_level_button = ttk.Button(
            self.dino_leveller, text="Level Dino Melee - F5", command=lambda: self.dinoleveller.click_loop(1126, 673, 100))
        self.dino_melee_level_button.pack(pady=5)
        keyboard.add_hotkey("F5", lambda: self.dinoleveller.start_click_loop(1126, 673, 100))    
        # Tab 3: INI Changer
        self.ini = ttk.Frame(self.notebook)
        self.notebook.add(self.ini, text='INI Changer')
        
        # Tab 4: Farmer
        self.farm_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.farm_tab, text='Farmer')
        
        self.keep_meat_button = ttk.Button(
            self.farm_tab, text="On a meatrun - F1", command=lambda: self.dinoinventory.keep_meat_hide())
        self.keep_meat_button.pack(pady=5)
        keyboard.add_hotkey("F1", lambda: self.dinoinventory.keep_meat_hide())
        
        self.keep_metal_button = ttk.Button(
            self.farm_tab, text="On a metalrun - F2", command=lambda: self.dinoinventory.keep_metal())
        self.keep_metal_button.pack(pady=5)
        keyboard.add_hotkey("F2", lambda: self.dinoinventory.keep_metal())  

        self.notebook.pack(expand=True, fill='both')

    def update_clicker_button_text(self, text):
        self.click_button.config(text=text)

    def update_log_button_text(self, text):
        self.logs_button.config(text=text)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = AutoClickerGUI()
    gui.run()
