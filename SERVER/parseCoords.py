import os
import sys
coords = []

# checks distance(radius) between given point and solved center
def checker(x, y, z):
     dist = ((x - avx)**2 + (y - avy)**2 + (z - 0)**2)**0.5
     return round(dist, 6)

# solves for midpoint, slope, normal, and both y-intercepts between two points
def normalSolver(index1, index2):
     slope = (coords[index2][1]-coords[index1][1])/(coords[index2][0]-coords[index1][0])
     normal = -1/slope
     midp = (coords[index1][0]+coords[index2][0])/2, (coords[index1][1]+coords[index2][1])/2
     yint = midp[1] - (slope * midp[0])
     Nyint = midp[1] - (normal * midp[0])
     # print("Slope: ", slope)
     # print("Normal: ", normal)
     # print("Midpoint: ", midp)
     # print("Y-Int: ", yint)
     # print("Normal Y-Int: ", Nyint)
     return[slope, normal, midp, yint, Nyint]

# returns coordinate of intersection of the normals of two set of points p1, p2 and p3, p4
def intersection(p1, p2, p3, p4):
     line1 = normalSolver(p1, p2)
     line2 = normalSolver(p3, p4)
     xi = (line1[4] - line2[4]) / (line2[1] - line1[1])
     yi = line1[1] * xi + line1[4]
     return[xi, yi]

# writes DaymarEquator.txt into an array
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
            coords.append((data[1], data[2], data[3]))

# 
    final = intersection(2, 3, 3, 4)
    avx = final[0]
    avy = final[1]
    print("Center: ", avx, avy, "~0")