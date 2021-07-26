from math import sqrt, degrees, asin
coords = []

def setCoords(coordinates):
    global coords
    coords = coordinates

def clC(number):
    if 0 < abs(number-int(number)) < 0.0000001:
        number = float(int(number))
    if 0 < abs(number-round(number, 6)) < 0.0000001:
        number = float(int(number) + 1)
    return number


# get distance between points or distance(radius) between given point and solved center (point, center, true)
def dist(point1, point2, center):
    # distance to center
    if center:
        distance = ((intersection(2, 3, 3, 4)[0] - coords[point1][0])**2 + (intersection(2, 3, 3, 4)[1] - coords[point1][1])**2 + (intersection(2, 3, 3, 4)[2] - coords[point1][2])**2)**0.5
    # normal distance
    else:
        distance = ((coords[point2][0] - coords[point1][0])**2 + (coords[point2][1] - coords[point1][1])**2 + (coords[point2][2] - coords[point1][2])**2)**0.5
    return distance

# solves hypotenuse and remaing angles given right angle and two sides (length, height)
def rightSolver(dist, zcoord):
    c = sqrt(dist**2 + zcoord**2)
    distA = degrees(asin((c/dist)**-1))
    distB = degrees(asin((c/zcoord)**-1))
    return (c, distA, distB)

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

# returns inner angle of chord given by two points around the known center
def angSolver(p1, p2, center):
    angle = 180 - (2 * degrees(asin(dist(p1, p2, False)/(2 * dist(p1, 0, True)))))
    return angle

# gives the average degrees moved per the length of time between data points (assumes 1 minute and divides the output by 60 seconds)
def rotSolver(p1, p2, p3, p4):
    avg = 0
    A1 = angSolver(p1, p2, intersection(2, 3, 3, 4))
    A2 = angSolver(p3, p4, intersection(2, 3, 3, 4))
    for i in range(len(coords)-1):
        avg = avg + angSolver(i, i+1, intersection(2, 3, 3, 4))
        #print(coords[i+1][3]-coords[i][3]) # 100 represents 1 minute
    rot = avg/(len(coords)-1)/60 # deg/sec
    return rot

# returns coordinate of intersection of the normals of two set of points p1, p2 and p3, p4
def intersection(p1, p2, p3, p4):
    line1 = normalSolver(p1, p2)
    line2 = normalSolver(p3, p4)
    xi = (line1[4] - line2[4]) / (line2[1] - line1[1])
    yi = line1[1] * xi + line1[4]
    return[xi, yi, 0]