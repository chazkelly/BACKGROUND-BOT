import requests
import json
from dino.dinoleveller import DinoLeveller

class Discord():
    def __init__(self, hwnd):
        self.dinoleveller = DinoLeveller(hwnd)
        
    def discord_embed(self, station_time, deposited_paste, station_number):
        
        # webhook_url = 'https://discord.com/api/webhooks/1191006621074206814/Ji2fDa4JdkxXXAhGSXtELL0h-RhHlAc4kIfGDPJMENTIsytDXNu-RFENQlL2GdIbsWD-'
        webhook_url = 'https://discord.com/api/webhooks/1199018034556305519/cY4lqtnicZjJQixBZbPECR5OK1TIpqnQ8zHSwAe2vOV4k-FoFU4plqXHgOoebWWWxhhp'
        

        paste_img = "https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Cementing_Paste.png/revision/latest?cb=20180801020251"

        payload = {
            'content': 'Paste',
            'username': 'Chaz paste',
            'avatar_url': 'https://media.discordapp.net/attachments/1112710849832960050/1191025592422912090/chaz.png?ex=65a3f005&is=65917b05&hm=8b42cc9634d6a6f6a355ebe90bf9dc86a3139bcf3537ea1d040e7588fc80d51f&=&format=webp&quality=lossless',
            "channel_id": "your_channel_id",
            "content": "",
            "tts": False,
            "embeds": [
                {
                    "type": "rich",
                    "title": "Paste Collected",
                    "description": f"Station {station_number} complete",
                    "color": 0x00FFFF,
                    "thumbnail": {
                        "url": paste_img,
                        "height": 0,
                        "width": 0
                    },
                    "fields": [
                        {
                            "name": "Time Taken:",
                            "value": f"{station_time} seconds"
                        },
                        {
                            "name": "Amount of Paste",
                            "value": f"{deposited_paste}"
                        }]
                }
            ]
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        

