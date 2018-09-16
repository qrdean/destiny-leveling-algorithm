from gear import Gear


class Guardian:
    def __init__(self, guardianNumber: int, startingGear: Gear):
        self.guardianNumber = guardianNumber
        self.gear: Gear = startingGear

    def getGear(self):
        return self.gear.getGear()

    # Mutates that Guardian's gear
    def updateGearByPiece(self, gearPiece, newPowerLevel):
        gear: Gear = self.gear
        gear.updateGearByPiece(gearPiece, newPowerLevel)
        self.gear = gear

    def updateGearByDictionary(self, dictionary):
        gear: Gear = self.gear
        gear.updateGearByDictionary(dictionary)
        self.gear = gear

    def getPowerLevel(self):
        gear: Gear = self.gear
        return gear.calculateAverageGear()

    def lowestGear(self):
        gear: Gear = self.gear
        return gear.findLowestGearName()

    def getGuardianNumber(self):
        return self.guardianNumber

    def getWeapons(self):
        gear: Gear = self.gear
        return gear.getWeaponsAsDictionary()

    def isCurrentGearHigher(self, incomingGearType, incomingPowerLevel):
        gear: Gear = self.gear
        if (gear.getGearPowerByPiece(incomingGearType) > incomingPowerLevel):
            return bool(1)
        else:
            return bool(0)
