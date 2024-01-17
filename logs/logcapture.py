from PIL import Image
import requests
import threading
from capturescreen.capturescreen import Capture
import time
from settings.settings import Settings
import json


class Logging:
    def __init__(self, log_button_callback=None):
        self.stop_event = threading.Event()
        self.logcapture = Capture()
        self.logging_thread = None
        self.is_capturing_logs = False
        self.button_callback = log_button_callback
        self.send_interval = 180
        self.settings = Settings()
        self.settings.load_from_file("settings.json")
        self.webhook_url = self.settings.discord_webhook

    def toggle_capture_logs(self):
        if not self.is_running():
            self.start_logging()
        else:
            self.stop_logging()

    def is_running(self):
        return self.logging_thread and self.logging_thread.is_alive()

    def start_logging(self):
        self.stop_event.clear()
        self.logging_thread = threading.Thread(target=self.log_loop)
        self.logging_thread.start()
        self.update_button_text("Stop sending logs to discord")

    def stop_logging(self):
        self.is_capturing_logs = False
        self.stop_event.set()
        if self.logging_thread and self.logging_thread.is_alive():
            self.logging_thread.join(timeout=0)
        self.update_button_text("Start sending logs to discord")

    def log_loop(self):
        self.capture_logs()

    def capture_logs(self):
        while not self.stop_event.is_set():
            image_path = "logs/screenshots/logs_only.png"
            self.logcapture.capture_window_and_save(output_file=image_path)
            logs = Image.open(image_path)
            if logs:
                left = 757
                top = 188
                right = 1162
                bottom = 828
                cropped_image = logs.crop((left, top, right, bottom))
                cropped_image.save(image_path)
                self.post_to_discord(image_path)
            time.sleep(self.send_interval)
        self.stop_event.clear()
        return "logs_only.png"

    def post_to_discord(self, image_path):
        with open(image_path, 'rb') as file:
            image_data = file.read()
        payload = {
            'content': 'Logs:',
            'username': 'Chaz logs',
            'avatar_url': 'https://media.discordapp.net/attachments/1112710849832960050/1191025592422912090/chaz.png?ex=65a3f005&is=65917b05&hm=8b42cc9634d6a6f6a355ebe90bf9dc86a3139bcf3537ea1d040e7588fc80d51f&=&format=webp&quality=lossless',
        }
        files = {'file': (image_path, image_data)}
        response = requests.post(self.webhook_url, data=payload, files=files)
        print(response.text)

    def update_button_text(self, text):
        if self.button_callback:
            self.button_callback(text)
