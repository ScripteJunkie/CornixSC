# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
from ctypes import wintypes
import time
from pyautogui import write
from ahk import AHK

SendInput = ctypes.windll.user32.SendInput

ahk = AHK()

# 0x11 is w

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def  typeskey(hexKeyCode):
    #ReleaseKey(0x11)
    PressKey(hexKeyCode)
    ReleaseKey(0x10)
    time.sleep(.01)
    ReleaseKey(hexKeyCode)
    #ReleaseKey(0x11)
    #time.sleep(.1)

BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL

class keyboardDisable():

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
            msvcrt.getwch()


    def __init__(self):
        self.on = False
        import msvcrt

disable = keyboardDisable()
if __name__ == '__main__':
    while(True):
        time.sleep(10)
        BlockInput(True)
        typeskey(0x1C)
        time.sleep(.02)
        typeskey(0x35)
        typeskey(0x1F)
        typeskey(0x23)
        typeskey(0x18)
        typeskey(0x11)
        typeskey(0x26)
        typeskey(0x18)
        typeskey(0x2E)
        typeskey(0x1E)
        typeskey(0x14)
        typeskey(0x17)
        typeskey(0x18)
        typeskey(0x31)
        time.sleep(.02)
        typeskey(0x1C)
        BlockInput(False)