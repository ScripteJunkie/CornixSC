import pymem
import os

pm = pymem.Pymem('Spotify.exe')
modules = list(pm.list_modules())
for module in modules:
    print(module.name)