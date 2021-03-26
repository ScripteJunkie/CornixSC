import pymem

pm = pymem.Pymem('firefox.exe')
modules = list(pm.list_modules())
for module in modules:
    print(module.name)