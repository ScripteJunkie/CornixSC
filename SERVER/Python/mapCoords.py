from math import sin, cos, asin, degrees, radians
from jsonWiz import getCoords
from mathFunc import clC

# This should be used by the clientside or only called every time new coordinates are called. 
# From there the time between reporting can be calculated and fed here.
# Then this is fed to tracking of the coordinates and determining player movement.
# This file acts as an intermidiary library between getting coordinates on the client and tracking those to a surface.

# This should locate the closest planet to last reported coordinates
def planetLoc(coord):
    centers = getCoords()
    dists = []
    for center in centers:
        distance = ((center[0] - coord[0])**2 + (center[1] - coord[1])**2 + (center[2] - coord[2])**2)**0.5
        dists.append(distance)
    index = dists.index(min(dists))
    return index, dists[index]

# Takes counterclockwise angle and origin coordinates and solves for new coordinates
def coordSolver(angle, origin):
    axis = [getCoords()[planetLoc(origin)[0]][0], getCoords()[planetLoc(origin)[0]][1], getCoords()[planetLoc(origin)[0]][2]]
    c = ((axis[0] - origin[0])**2 + (axis[1] - origin[1])**2 + (axis[2] - origin[2])**2)**0.5
    while angle >= 360:
        angle -= 360
    radius = ((axis[0] - origin[0])**2 + (axis[1] - origin[1])**2)**0.5
    distance = (((radius) - origin[0])**2 + (axis[1] - origin[1])**2)**0.5
    # angle between origin coord and axisX + distance, axisY, also is clockwise
    diff = clC(2 * degrees(asin(0.5 * distance / radius)))
    if (origin[1] > axis[1]):
        diff = 360 - diff
    theta = diff + (90 - angle)
    while theta >= 360:
        theta -= 360
    newCoord = [clC(radius * sin(radians(theta))), clC(radius * cos(radians(theta))), origin[2]]
    return newCoord

# gets lat, lon from game coordinates
def coordsCart(coord, meridian):
    planetLoc(coord)
    return 