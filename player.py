from guardian import Guardian


class Player:
    def __init__(self, guardian1: Guardian, guardian2: Guardian, guardian3: Guardian):
        self.guardians = {
            guardian1.getGuardianNumber(): guardian1,
            guardian2.getGuardianNumber(): guardian2,
            guardian3.getGuardianNumber(): guardian3
        }

    def getHighestLevelGuardian(self):
        tempPowerLevel = 0
        guardianNumber = 0
        guardians: dict = self.guardians
        for key, guardian in guardians.items():
            if (tempPowerLevel < guardian.getPowerLevel()):
                tempPowerLevel = guardian.getPowerLevel()
                guardianNumber = guardian.getGuardianNumber()
        return [guardianNumber, tempPowerLevel]

    def getGuardianByNumber(self, guardianNumber):
        guardians = self.guardians
        return guardians.get(guardianNumber)

    def setGuardianByNumber(self, guardianNumber, guardianInfo):
        guardians: dict = self.guardians
        newGuardianDict: dict = {guardianNumber: guardianInfo}
        guardians.update(newGuardianDict)
        self.guardians = guardians

    def transferWeapons(self, fromGuaridanNumber: int, toGuardianNumber: int):
        guardianTransferringFrom: Guardian = self.getGuardianByNumber(
            fromGuaridanNumber)
        guardianTransferringTo: Guardian = self.getGuardianByNumber(
            toGuardianNumber)
        guardianTransferringTo.updateGearByDictionary(
            guardianTransferringFrom.getWeapons())
        self.setGuardianByNumber(toGuardianNumber, guardianTransferringTo)
