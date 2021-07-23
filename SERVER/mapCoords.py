import os
import sys
import math
import time
coords = [[-18930539539.534645, -2610158765.4989395, 0]]
centers = [[-18930539539.534645, -2610158765.4989395, 0]]
rots = []

# This should be used by the clientside or only called every time new coordinates are called. 
# From there the time between reporting can be calculated and fed here.
# Then this is fed to tracking of the coordinates and determining player movement.
# This file acts as an intermidiary library between getting coordinates on the client and tracking those to a surface.

# This should locate the closest planet to last reported coordinates
def planetLoc(coord):
    dists = []
    for center in centers:
        distance = ((center[0] - coord[0])**2 + (center[1] - coord[1])**2 + (center[2] - coord[2])**2)**0.5
        dists.append(distance)
    index = dists.index(min(dists))
    return index, dists[index]

# Takes angle and origin coordinates and solves for new coordinates
def coordSolver(angle, origin):
    
    return

def initCoords():

    return