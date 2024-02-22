import tkinter as tk
from tkinter import ttk
from tkinter import *
from clicker.autoclicker import AutoClicker
from logs.logcapture import Logging
from capturescreen.capturescreen import Capture
from player.movement import Movement
from player.sendkeys import SendKeys
from dino.dinoleveller import DinoLeveller
from ini.ini import Ini
from arb.arb import Arb
from snails.snailempty import Snail
from snails.snailembed import Discord
from dino.dinoinventory import DinoInventory
from inventorymacro.inventory import MagicF
from settings.settings import Settings
import keyboard
from PIL import Image, ImageTk
import pydirectinput as pdinput
import ctypes
import threading
import os
import sys


FindWindow = ctypes.windll.user32.FindWindowA
PostMessage = ctypes.windll.user32.PostMessageA


class AutoClickerGUI:
    def __init__(self):
        self.hwnd = FindWindow(None, b"ArkAscended")
        self.auto_clicker = AutoClicker(self.hwnd)
        self.inventory = MagicF(self.hwnd)
        self.logscapture = Logging()
        self.capturescreen = Capture()
        self.player = Movement(self.hwnd)
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoleveller = DinoLeveller(self.hwnd)
        self.snails = Snail(self.hwnd)
        self.snailembed = Discord(self.hwnd)
        self.ini = Ini(self.hwnd)
        self.dinoinventory = DinoInventory(self.hwnd)
        self.settings = Settings()
        self.arb = Arb(self.hwnd)


        self.root = tk.Tk()
        self.root.title("ASA Automation")
        self.root.geometry("500x300")
        # self.root.resizable(0,0)
        img = tk.PhotoImage(
            file=self.resource_path("chaz.png"))
        self.root.iconphoto(True, img)
        


        self.notebook = ttk.Notebook(self.root)
        

        # Tab 1: Overview
        self.overview_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.overview_tab, text='Overview')
        overviewlabel = ttk.Label(
            self.overview_tab, text='F1 - Keeps meat and hide when on meatrun\nF2 - Keeps metal on metal run\nF3 - Apply INI\nF4 - Level Dino HP\nF5 - Level Dino Melee (Doesnt work on water dinos)\nF6 - Turn on broken INI\nF7- Turn off broken INI\n')
        overviewlabel.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        label1 = ttk.Label(
            self.overview_tab, text='The background tab has a script to send logs to\n discord make sure your logs are open when doing so.')
        label1.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        descriptionlabel = ttk.Label(
            self.overview_tab, text='This is a script that helps automate things in\n Ark Survival Ascended. \nWritten by chazkelly.')
        descriptionlabel.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        # Tab 2: Background
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

        # Tab 3: Dino Leveller
        self.dino_leveller = ttk.Frame(self.notebook)
        self.notebook.add(self.dino_leveller, text='Dino Leveller')

        self.dino_hp_level_button = ttk.Button(
            self.dino_leveller, text="Level Dino HP - F4", command=lambda: self.dinoleveller.start_click_loop(1126, 505, 100))
        self.dino_hp_level_button.pack(pady=5)
        keyboard.add_hotkey(
            "F4", lambda: self.dinoleveller.start_click_loop(1126, 505, 100))

        self.dino_melee_level_button = ttk.Button(
            self.dino_leveller, text="Level Dino Melee - F5", command=lambda: self.dinoleveller.click_loop(1126, 673, 100))
        self.dino_melee_level_button.pack(pady=5)
        keyboard.add_hotkey(
            "F5", lambda: self.dinoleveller.start_click_loop(1126, 673, 100))

        # Tab 4: INI Changer
        self.ini_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.ini_tab, text='INI Changer')

        self.ini_button = ttk.Button(
            self.ini_tab, text="Apply Ini - F3", command=lambda: self.ini.apply_ini())
        self.ini_button.pack(pady=5)
        keyboard.add_hotkey("F3", lambda: self.ini.apply_ini())

        self.broken_ini_on_button = ttk.Button(
            self.ini_tab, text="Apply broken Ini - F6", command=lambda: self.ini.turn_on_broken_ini())
        self.broken_ini_on_button.pack(pady=5)
        keyboard.add_hotkey("F6", lambda: self.ini.turn_on_broken_ini())

        self.broken_ini_off_button = ttk.Button(
            self.ini_tab, text="Turn off broken Ini - F7", command=lambda: self.ini.turn_off_broken_ini())
        self.broken_ini_off_button.pack(pady=5)
        keyboard.add_hotkey("F7", lambda: self.ini.turn_off_broken_ini())

        # Tab 5: Farmer
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

        # Tab 6: Magic F
        self.baby_feed_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.baby_feed_tab, text='Magic F')

        # Add three radio buttons
        self.selected_option = tk.StringVar()

        option1_radio = ttk.Radiobutton(
            self.baby_feed_tab, text="Raw meat", variable=self.selected_option, value="RawMeat")
        option1_radio.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        option2_radio = ttk.Radiobutton(
            self.baby_feed_tab, text="Berries", variable=self.selected_option, value="Berries")
        option2_radio.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        option3_radio = ttk.Radiobutton(
            self.baby_feed_tab, text="Paste (Empty snails)", variable=self.selected_option, value="Paste")
        option3_radio.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        option4_radio = ttk.Radiobutton(
            self.baby_feed_tab, text="Take all", variable=self.selected_option, value="TakeAll")
        option4_radio.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        option4_radio = ttk.Radiobutton(
            self.baby_feed_tab, text="Empty crop plots", variable=self.selected_option, value="CropPlots")
        option4_radio.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        self.activate_button = ttk.Button(
            self.baby_feed_tab, text="Activate", command=self.activate_function)
        self.activate_button.grid(
            row=7, column=0, padx=10, pady=10, sticky='w')

        self.deactivate_button = ttk.Button(
            self.baby_feed_tab, text="Deactivate", command=self.deactivate_function, state=tk.DISABLED)
        self.deactivate_button.grid(
            row=7, column=1, padx=10, pady=10, sticky='w')

        # Tab 7: Settings
        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text='Settings')

        entry_label = ttk.Label(self.settings_tab, text="Discord Webhook:")
        entry_label.pack(pady=10)
        entry = ttk.Entry(self.settings_tab)
        entry.insert(0, self.settings.discord_webhook)
        entry.pack(pady=10)

        save_button = tk.Button(self.settings_tab, text="Save",
                                command=lambda: self.settings.save_discord_webhook(entry))
        save_button.pack(pady=10)
        
        
        
        # Tab 8: Testing
        self.test_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.test_tab, text="Testing")
        
        test_button = tk.Button(self.test_tab, text="Test snail",
                                command=lambda: self.snails.empty_snail(29))
        test_button.pack(pady=10)
        
        keyboard.add_hotkey("#", lambda: pdinput.moveRel(0, 300))
        keyboard.add_hotkey("`", lambda: self.auto_clicker.toggle_clicking())


        self.notebook.pack(expand=True, fill='both')

    def activate_function(self):
        selected_value = self.selected_option.get()
        selected_value == ""

        if selected_value == "RawMeat":
            self.inventory.stop_event.clear()
            self.is_rawmeat_active = True
            self.activate_button.config(state=tk.DISABLED)
            self.deactivate_button.config(state=tk.NORMAL)
            threading.Thread(target=self.inventory.rawmeat_loop,
                             args=(self.is_rawmeat_active,)).start()

        elif selected_value == "Berries":
            self.inventory.stop_event.clear()
            self.is_berry_active = True
            self.activate_button.config(state=tk.DISABLED)
            self.deactivate_button.config(state=tk.NORMAL)
            threading.Thread(target=self.inventory.berry_loop,
                             args=(self.is_berry_active,)).start()

        elif selected_value == "Paste":
            self.inventory.stop_event.clear()
            self.is_paste_active = True
            self.activate_button.config(state=tk.DISABLED)
            self.deactivate_button.config(state=tk.NORMAL)
            threading.Thread(target=self.inventory.paste_loop,
                             args=(self.is_paste_active,)).start()

        elif selected_value == "TakeAll":
            self.inventory.stop_event.clear()
            self.is_takeall_active = True
            self.activate_button.config(state=tk.DISABLED)
            self.deactivate_button.config(state=tk.NORMAL)
            threading.Thread(target=self.inventory.takeall_loop,
                             args=(self.is_takeall_active,)).start()

        elif selected_value == "CropPlots":
            self.inventory.stop_event.clear()
            self.is_cropplot_active = True
            self.activate_button.config(state=tk.DISABLED)
            self.deactivate_button.config(state=tk.NORMAL)
            threading.Thread(target=self.inventory.cropplot_loop,
                             args=(self.is_cropplot_active,)).start()

    def deactivate_function(self):
        selected_value = self.selected_option.get()
        self.inventory.stop_event.set()
        self.is_rawmeat_active = False
        self.is_berry_active = False
        self.is_paste_active = False
        self.is_takeall_active = False
        self.is_cropplot_active = False
        self.activate_button.config(state=tk.NORMAL)
        self.deactivate_button.config(state=tk.DISABLED)
        

    def update_clicker_button_text(self, text):
        self.click_button.config(text=text)

    def update_log_button_text(self, text):
        self.logs_button.config(text=text)

    def update_magicf_button_text(self, text):
        self.activate_button.config(text=text)
        
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
            
        return os.path.join(base_path, relative_path)

    def run(self):
        self.root.mainloop()
