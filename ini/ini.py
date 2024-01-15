import ctypes
from player.sendkeys import SendKeys
from dino.dinoleveller import DinoLeveller
import time
import pyperclip

console_variables = r"stat fps | grass.Enable 0 | r.Water.SingleLayer.Reflection 0 | r.LightShaftQuality 0 | r.shadowquality 0 | r.VolumetricCloud 0 | r.VolumetricFog 0 | r.BloomQuality 0 | r.Lumen.Reflections.Allow 0 | r.Lumen.DiffuseIndirect.Allow 1 | r.Shadow.Virtual.Enable 0 | r.DistanceFieldShadowing 0 | r.Shadow.CSM.MaxCascades 0 | sg.FoliageQuality 0 | sg.TextureQuality 0 | show InstancedFoliage | show InstancedStaticMeshes | show DynamicShadows | show InstancedGrass | wp.Runtime.HLOD 0 | r.PostProcessing.DisableMaterials 1"
broken_ini_on = r"wp.Runtime.OverrideRuntimeSpatialHashLoadingRange -range="
broken_ini_off = r"wp.Runtime.OverrideRuntimeSpatialHashLoadingRange -range=5000"

SendInput = ctypes.windll.user32.SendInput
FindWindow = ctypes.windll.user32.FindWindowA
hwnd = FindWindow(None, b"ArkAscended")


class Ini:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.sendkeys = SendKeys(self.hwnd)
        self.dinoleveller = DinoLeveller(self.hwnd)

    def apply_ini(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        self.sendkeys.send_tab()
        pyperclip.copy(console_variables)
        self.sendkeys.send_ctrl_v()
        time.sleep(0.01)
        self.sendkeys.send_enter()

    def turn_on_broken_ini(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        self.sendkeys.send_tab()
        pyperclip.copy(broken_ini_on)
        self.sendkeys.send_ctrl_v()
        self.sendkeys.send_enter()

    def turn_off_broken_ini(self):
        self.dinoleveller.bring_to_foreground()
        time.sleep(0.1)
        self.sendkeys.send_tab()
        pyperclip.copy(broken_ini_off)
        self.sendkeys.send_ctrl_v()
        self.sendkeys.send_enter()
