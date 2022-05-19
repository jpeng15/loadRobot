import math
import requests

def loadRobot(loadID, x, y):

    URL = 'https://60c8ed887dafc90017ffbd56.mockapi.io/robots'

    r = requests.get(url = URL)
    data = r.json()
    
    result = data[0]
    mindist = distance(x, result['x'], y, result['y'])
    maxbattery = result['batteryLevel']

    for x in range(0, 100):
        robot = data[x]
        roboDistance = distance(x, robot['x'], y, robot['y'])

        if roboDistance < mindist and mindist > 10:
            mindist = roboDistance
            result = robot
        
        elif mindist <= 10 and roboDistance <= 10 and robot['batteryLevel'] > maxbattery:
            result = robot
            maxbattery = robot['batterLevel']
    
    roboInfo = {
        "robotID": result['robotId'],
        "distanceToGoal": distance(x, result['x'], y, result['y']),
        "batteryLevel": result['batteryLevel']

    }
    return roboInfo


def distance(x1, x2, y1, y2):
    xdif = x2 - x1
    ydif = y1 - y2
    return math.sqrt(pow(xdif, 2) + pow(ydif, 2))
