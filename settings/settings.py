import json


class Settings:
    def __init__(self):
        self.discord_webhook = ""

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.__dict__.update(data)
        except FileNotFoundError:
            print("Settings file not found. Using default settings.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Using default settings.")

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.__dict__, file, indent=4)

    def save_discord_webhook(settings, entry):
        discord_webhook = entry.get()
        settings.discord_webhook = discord_webhook
        settings.save_to_file("settings.json")
