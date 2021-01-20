import os
import sys
import time

with open(os.path.join(sys.path[0], "DaymarEquator.txt"), "r") as f:
    content = f.read().splitlines()

    for l in content: 
            data = l
            data = data.split(' ')
            data.pop(0)
            data = float(data[0][2:]), float(data[1][2:]), float(data[2][2:]), int(data[3][5:])
            data = data[3], data[0], data[1], data[2]
            print(data)