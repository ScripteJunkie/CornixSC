import json

# Opens the POI.json for other functions
def openJSON():
    with open('../CornixPOI/POI.json') as f:
        data = json.load(f)
        #print(data[0]['POI'][1])
    return data

# Return list of all center coordinate data indexed by order of entry
def getCoords():
    data = openJSON()
    coords = []
    for i in range(len(data)):
        coords.append((data[i]['gloX'], data[i]['gloY'], data[i]['gloZ']))
    return coords

# Return list of all rotation data indexed by order of entry
def getRotation():
    data = openJSON()
    rots = []
    for i in range(len(data)):
        rots.append((data[i]['rotV'], data[i]['period']))
    return rots

# Return list of the values of all entries of 'term' => getCustom('name')
def getCustom(term):
    data = openJSON()
    cust = []
    for i in range(len(data)):
        cust.append((data[i][term]))
    return cust

# Return all data in index => getEntry(3)
def getEntry(index):
    data = openJSON()
    return data[index]