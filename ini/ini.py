import ctypes
from player.sendkeys import SendKeys
import time


# console_variables =

SendInput = ctypes.windll.user32.SendInput
FindWindow = ctypes.windll.user32.FindWindowA
hwnd = FindWindow(None, b"ArkAscended")

class Ini:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.sendkeys = SendKeys(self.hwnd)
        
    def apply_selection(self):
        self.sendkeys.send_tab()
        time.sleep(1)
        self.sendkeys.send_word("grass.Enable 0 | r.Water.SingleLayer.Reflection 0 | r.LightShaftQuality 0 | r.shadowquality 0 | r.VolumetricCloud 0 | r.VolumetricFog 0 | r.BloomQuality 0 | r.Lumen.Reflections.Allow 0 | r.Lumen.DiffuseIndirect.Allow 1 | r.Shadow.Virtual.Enable 0 | r.DistanceFieldShadowing 0 | r.Shadow.CSM.MaxCascades 0 | sg.FoliageQuality 0 | sg.TextureQuality 0 | show InstancedFoliage | show InstancedStaticMeshes | show DynamicShadows | show InstancedGrass | wp.Runtime.HLOD 0 | r.PostProcessing.DisableMaterials 1")
        time.sleep(0.1)
        self.sendkeys.send_enter()

        
        

        
