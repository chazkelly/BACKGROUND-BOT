import tkinter as tk
from tkinter import ttk
from clicker.autoclicker import AutoClicker
from logs.logcapture import Logging
from capturescreen.capturescreen import Capture
from player.movement import Movement
from player.sendkeys import SendKeys
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

        self.root = tk.Tk()
        self.root.title("ASA Background Automation")
        self.root.geometry("350x200")

        self.auto_clicker = AutoClicker(self.hwnd, clicker_button_callback=self.update_clicker_button_text)
        self.logscapture = Logging(log_button_callback=self.update_log_button_text)

        self.click_button = ttk.Button(
            self.root, text="Start Clicking", command=self.auto_clicker.toggle_clicking)
        self.click_button.pack(pady=5)

        self.logs_button = ttk.Button(
            self.root, text="Start sending logs to discord", command=self.logscapture.toggle_capture_logs)
        self.logs_button.pack(pady=5)
        
        self.turn_left_button = ttk.Button(
            self.root, text="Turn Left", command=lambda: self.player.turn_90_degrees("left"))
        self.turn_left_button.pack(pady=5)
                
        self.turn_right_button = ttk.Button(
            self.root, text="Turn Right", command=lambda: self.player.turn_90_degrees("right"))
        self.turn_right_button.pack(pady=5)
        
        self.entry_var = tk.StringVar()
        self.text_entry = ttk.Entry(self.root, textvariable=self.entry_var)
        self.text_entry.pack(pady=5)
        
        self.testbutton = ttk.Button(
            self.root, text="Test", command=lambda: self.sendkeys.send_word(self.entry_var.get()))
        self.testbutton.pack(pady=5)

    def update_clicker_button_text(self, text):
        self.click_button.config(text=text)
        self.click_button.config

    def update_log_button_text(self, text):
        self.logs_button.config(text=text)
        self.logs_button.config

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = AutoClickerGUI()
    gui.run()
