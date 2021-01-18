import time
import pyperclip

while(True):
    data = pyperclip.waitForNewPaste()
    data = data.split(' ')
    data.pop(0)
    data = float(data[0][2:]), float(data[1][2:]), float(data[2][2:])
    print(time.time(), data[0], data[1], data[2])