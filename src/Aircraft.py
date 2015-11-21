__author__ = 'randy'

from math import *
from src.Util import *

class Aircraft:
    def __init__(self, xInFeet: int, yInFeet: int, zInFeet: int,
                 heading: float, vSpeedFPS: int, gSpeedFPS: int,
                 alertLevel: int, id: int):
        self.xInFeet = xInFeet
        self.yInFeet = yInFeet
        self.zInFeet = zInFeet
        self.heading = heading
        self.vSpeedFPS = vSpeedFPS
        self.gSpeedFPS = gSpeedFPS
        self.alertLevel = alertLevel
        self.id = id

    def getXInFeet(self):
        return self.xInFeet

    def getYInFeet(self):
        return self.yInFeet

    def getZInFeet(self):
        return self.zInFeet

    def getHeading(self):
        return self.heading

    def getVSpeedFPS(self):
        return self.vSpeedFPS

    def getGSpeedFPS(self):
        return self.gSpeedFPS

    def getAlertLevel(self):
        return self.alertLevel

    def horizDistToOwnship(self):
        return sqrt(self.xInFeet * self.xInFeet +
                    self.yInFeet * self.yInFeet)

    def calcAlertLevel(self, ownShip):
        hDistNM = feetToNauticalMiles(self.horizDistToOwnship())
        vDist = abs(self.getZInFeet())
        if vDist <= 1500 and hDistNM <= 4.0:
            self.alertLevel = 5
            return
        if vDist <= 2000 and hDistNM <= 5.0:
            self.alertLevel = 4
            return
        if vDist <= 3000 and hDistNM <= 6.0:
            self.alertLevel = 3
            return
        #
        # TODO
        # if ???????????????:
        #   self.alertLevel = 2
        #   return
        #
        self.alertLevel = 1

    def distanceToOwnship(self):
        return sqrt(self.xInFeet * self.xInFeet +
                    self.yInFeet * self.yInFeet +
                    self.zInFeet * self.zInFeet)

    def __lt__(self, other):
        return self.comparePriority(other) < 0

    def __eq__(self, other):
        return self.comparePriority(other) == 0

    def comparePriority(self, other):
        if self.alertLevel < other.alertLevel:
            return -1
        if self.alertLevel == other.alertLevel:
            if self.distanceToOwnship() < other.distanceToOwnship():
                return -1
            if self.distanceToOwnship() == other.distanceToOwnship():
                return 0
        return 1
