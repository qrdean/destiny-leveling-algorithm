class LevelingSystem:
    def tierOneLevel(self, powerLevel):
        if powerLevel < 520:
            return powerLevel + 5
        else:
            return powerLevel + 1

    def tierTwoLevel(self, powerLevel):
        if powerLevel < 540:
            return powerLevel + 5
        else:
            return powerLevel + 1

    def tierThreeLevel(self, powerLevel):
        return powerLevel + 5

    def exoticQuests(self, powerLevel):
        return powerLevel + 3

    def primeEngram(self, powerLevel):
        return powerLevel + 5
