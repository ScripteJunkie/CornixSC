import os
import sys
from mathFunc import setCoords, rotSolver, intersection

def getCoord():
     # writes DaymarEquator.txt into an array
     coords = []
     with open(os.path.join(sys.path[0], "DaymarEquator.txt"), "r") as f:
          content = f.read().splitlines()
          flen = len(content)
          for i in range(flen):
                    data = content[i]
                    data = data.split(' ')
                    data.pop(0)
                    data = float(data[0][2:]), float(data[1][2:]), float(data[2][2:]), int(data[3][5:])
                    # time, x, y, z
                    data = data[3], data[0], data[1], data[2]
                    coords.append((data[1], data[2], data[3], data[0]))
     return coords

coords = getCoord()
setCoords(coords)


# put in data and get everything out
final = intersection(2, 3, 3, 4)
avx = final[0]
avy = final[1]
print("Center: ", avx, avy, "~0")
print("Rotation: ", rotSolver(2, 3, 3, 4), "deg/sec")