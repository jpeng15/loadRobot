import math
import requests

def loadRobot(loadID, x, y):

    closeRobots = []
    URL = 'https://60c8ed887dafc90017ffbd56.mockapi.io/robots'

    r = requests.get(url = URL)
    data = r.json()
    


def distance(x1, x2, y1, y2):
    xdif = x2 - x1
    ydif = y1 - y2
    return math.sqrt(pow(xdif, 2) + pow(ydif, 2))
