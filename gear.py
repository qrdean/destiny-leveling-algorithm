

class Gear:
    def __init__(self, baseGearLevel: int):
        self.gearDictionary: dict = {
            "kinetic": baseGearLevel,
            "energy": baseGearLevel,
            "power": baseGearLevel,
            "helmet": baseGearLevel,
            "arms": baseGearLevel,
            "chest": baseGearLevel,
            "legs": baseGearLevel,
            "classItem": baseGearLevel
        }

    def calculateAverageGear(self):
        totalGearValue = 0
        gear: dict = self.gearDictionary
        # get the total of the values
        for k, value in gear.items():
            totalGearValue = value + totalGearValue
        # coarsing to int automatically takes the floor
        return int(totalGearValue / len(gear))

    def findLowestGearName(self):
        gear: dict = self.gearDictionary
        minvalue = min(gear.values())

        return [k for k, v in gear.items() if v == minvalue]

    # Mutates class variable gearDictionary
    def updateGearByPiece(self, gearPiece, newPowerLevel):
        gear: dict = self.gearDictionary
        newDictionary: dict = {gearPiece: newPowerLevel}
        gear.update(newDictionary)
        self.gearDictionary = gear

    def updateGearByDictionary(self, gearToUpdate: dict):
        gear: dict = self.gearDictionary
        newDictionary: dict = gearToUpdate
        gear.update(newDictionary)
        self.gearDictionary = gear

    def getWeaponsAsDictionary(self):
        gear: dict = self.gearDictionary
        weaponsDictionary: dict = {
            "kinetic": gear["kinetic"],
            "energy": gear["energy"],
            "power": gear["power"],
        }
        return weaponsDictionary

    def getGear(self):
        gear: dict = self.gearDictionary
        return gear

    def getGearPowerByPiece(self, gearPiece):
        gear: dict = self.gearDictionary
        return gear[gearPiece]
