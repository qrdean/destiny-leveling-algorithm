from random import choice
from level_system import LevelingSystem
from player import Player
from guardian import Guardian
from gear import Gear
import pandas as pd


class LevelingAlgorithm:
    def __init__(self):
        self

    def run(self, tierOnePowerfulCount, tierTwoPowerfulCount, tierThreePowerfulCount, primeEngramCount, primeEngramDropWeight, weeks, weightedChoiceGear, samplePlayerSize, grindForPrimes):
        levelingSystem: LevelingSystem = LevelingSystem()
        print("Initialize Leveling System")
        playersDictionary = []
        playerNumb = 0
        while(samplePlayerSize > 0):
            playerNumb += 1
            newPlayer: Player = self.setUpPlayer()
            print("set up new player")
            tempWeeks = weeks
            currentWeek = 0
            while(tempWeeks > 0):
                currentWeek += 1
                primeEngramsDropped = 0
                print("Number of weeks left: ", str(weeks))
                for x in range(1, 4):
                    print("Start guardian number: ", str(x))
                    currentLevelingGuardian: Guardian = newPlayer.getGuardianByNumber(
                        x)

                    tempTierOnePowerfulCount = tierOnePowerfulCount
                    tempTierTwoPowerfulCount = tierTwoPowerfulCount
                    tempTierThreePowerfulCount = tierThreePowerfulCount
                    tempPrimeEngramCount = primeEngramCount

                    print("Grinding Tier 1")
                    while (tempTierOnePowerfulCount > 0):
                        # print("Tier 1 left: " + str(tempTierOnePowerfulCount))
                        if tempPrimeEngramCount > 0:
                            primeEngramDrop = choice(primeEngramDropWeight)
                            if primeEngramDrop == 'Y':
                                gearDrop = choice(weightedChoiceGear)
                                levelOfItemDrop = levelingSystem.primeEngram(
                                    currentLevelingGuardian.getPowerLevel())
                                if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                                    currentLevelingGuardian.updateGearByPiece(
                                        gearDrop, levelOfItemDrop)
                                primeEngramsDropped += 1
                                tempPrimeEngramCount -= 1

                        gearDrop = choice(weightedChoiceGear)
                        levelOfItemDrop = levelingSystem.tierOneLevel(
                            currentLevelingGuardian.getPowerLevel())
                        if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                            currentLevelingGuardian.updateGearByPiece(
                                gearDrop, levelOfItemDrop)

                        tempTierOnePowerfulCount -= 1

                    print("Grinding Tier 2")
                    while (tempTierTwoPowerfulCount > 0):
                        # print("Tier 2 left: " + str(tempTierTwoPowerfulCount))
                        if tempPrimeEngramCount > 0:
                            primeEngramDrop = choice(primeEngramDropWeight)
                            if primeEngramDrop == 'Y':
                                gearDrop = choice(weightedChoiceGear)
                                levelOfItemDrop = levelingSystem.primeEngram(
                                    currentLevelingGuardian.getPowerLevel())
                                if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                                    currentLevelingGuardian.updateGearByPiece(
                                        gearDrop, levelOfItemDrop)
                                primeEngramsDropped += 1
                                tempPrimeEngramCount -= 1

                        gearDrop = choice(weightedChoiceGear)
                        levelOfItemDrop = levelingSystem.tierTwoLevel(
                            currentLevelingGuardian.getPowerLevel())
                        if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                            currentLevelingGuardian.updateGearByPiece(
                                gearDrop, levelOfItemDrop)

                        tempTierTwoPowerfulCount -= 1

                    print("Grinding Tier 3")
                    while (tempTierThreePowerfulCount > 0):
                        # print("Tier 3 left: " + str(tempTierThreePowerfulCount))
                        if tempPrimeEngramCount > 0:
                            primeEngramDrop = choice(primeEngramDropWeight)
                            if primeEngramDrop == 'Y':
                                gearDrop = choice(weightedChoiceGear)
                                levelOfItemDrop = levelingSystem.primeEngram(
                                    currentLevelingGuardian.getPowerLevel())
                                if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                                    currentLevelingGuardian.updateGearByPiece(
                                        gearDrop, levelOfItemDrop)
                                primeEngramsDropped += 1
                                tempPrimeEngramCount -= 1

                        gearDrop = choice(weightedChoiceGear)
                        levelOfItemDrop = levelingSystem.tierThreeLevel(
                            currentLevelingGuardian.getPowerLevel())
                        if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                            currentLevelingGuardian.updateGearByPiece(
                                gearDrop, levelOfItemDrop)

                        tempTierThreePowerfulCount -= 1

                    ########## FOR HARDCORE ##############
                    if grindForPrimes:
                        print("Grinding primeEngrams")
                        while (tempPrimeEngramCount > 0):
                            # print("Prime Engrams Left" + str(primeEngramCount))
                            gearDrop = choice(weightedChoiceGear)
                            levelOfItemDrop = levelingSystem.primeEngram(
                                currentLevelingGuardian.getPowerLevel())
                            if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                                currentLevelingGuardian.updateGearByPiece(
                                    gearDrop, levelOfItemDrop)
                            primeEngramsDropped += 1
                            tempPrimeEngramCount -= 1

                    # Ace of Spades
                    if currentWeek == 2:
                        print("Get ace of spades")
                        gearDrop = "kinetic"
                        levelOfItemDrop = levelingSystem.exoticQuests(
                            currentLevelingGuardian.getPowerLevel())
                        if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                            currentLevelingGuardian.updateGearByPiece(
                                gearDrop, levelOfItemDrop)

                    # Chaperone
                    if currentWeek == 2:
                        print("Get chaperone")
                        gearDrop = "kinetic"
                        levelOfItemDrop = levelingSystem.exoticQuests(
                            currentLevelingGuardian.getPowerLevel())
                        if not currentLevelingGuardian.isCurrentGearHigher(gearDrop, levelOfItemDrop):
                            currentLevelingGuardian.updateGearByPiece(
                                gearDrop, levelOfItemDrop)

                    print("Done with character:", str(x))
                    print(currentLevelingGuardian.getGuardianNumber())
                    print(currentLevelingGuardian.getPowerLevel())

                    if x < 3:
                        print("Switching to character number: ", str(x+1))
                        print("Transferring Weapons")
                        nextGuardian: Guardian = newPlayer.getGuardianByNumber(
                            x+1)
                        newPlayer.transferWeapons(
                            currentLevelingGuardian.getGuardianNumber(), nextGuardian.getGuardianNumber())
                    else:
                        highestGuardian = newPlayer.getHighestLevelGuardian()
                        playerDictionary = {"Player": playerNumb, "Week #": currentWeek, "Primes Dropped": primeEngramsDropped,
                                            "Guardian Number": highestGuardian[0], "Power Level": highestGuardian[1]}
                        playersDictionary.append(playerDictionary)
                        print(playerDictionary, file=open("output.txt", "a"))

                tempWeeks -= 1
            samplePlayerSize -= 1
        print("Output to csv")
        pd.DataFrame(playersDictionary).to_csv('out.csv', index=False)

    def setUpPlayer(self):
        newGear = Gear(500)
        hunter = Guardian(1, newGear)
        newGear2 = Gear(500)
        warlock = Guardian(2, newGear2)
        newGear3 = Gear(500)
        titan = Guardian(3, newGear3)

        return Player(hunter, warlock, titan)
