import os
import sys
import time
x = 0
y = 0
z = 0
def checker(x, y, z):
     dist = ((x - avx)**2 + (y - avy)**2 + (z -avz)**2)**0.5
     return round(dist, 6)
with open(os.path.join(sys.path[0], "DaymarEquator.txt"), "r") as f:
    content = f.read().splitlines()
    flen = len(content)

    for l in content: 
            data = l
            data = data.split(' ')
            data.pop(0)
            data = float(data[0][2:]), float(data[1][2:]), float(data[2][2:]), int(data[3][5:])
            data = data[3], data[0], data[1], data[2]
            print(data)
            x = x + data[1]
            y = y + data[2]
            z = z + data[3]
    avx = round(x / flen, 6)
    avy = round(y / flen, 6)
    avz = round(z / flen, 6)
    print("Center: ", avx, avy, avz)
    print(checker(-18930369755.629940, -2610400166.433840, -0.056059))
    print(checker(-18930259733.400406, -2610252624.504298, -0.963677))
    print(checker(-18930245132.941551, -2610179399.053881, -0.023946))