from gear import Gear
from guardian import Guardian
from player import Player
from leveling_algo import LevelingAlgorithm


def testAlgo():
    gear_drop_weight = ["kinetic"] * 1 + ["energy"] * 1 + ["power"] * 1 + ["helmet"] * \
        1 + ["arms"] * 1 + ["chest"] * 1 + \
        ["legs"] * 1 + ["classItem"] * 1

    primeEngram_drop_weight = ['Y'] * 5 + ['N'] * 95
    # tier 1
    # dailies = 12
    # spider = 1
    # strikes = 1
    # gambit = 1
    # pvp = 1
    # flash = 1
    # dailyStories = 1
    # ikora = 1
    tier1Count = 19

    # tier 2
    # nightfall = 1
    # dreamingCityBounty = 1
    # clanEngram = 1
    tier2Count = 3

    # tier 3
    # offering = 1
    # dreamingCityWeekly = 1
    tier3Count = 2

    # primeEngramPerDay = 2
    primeEngramsPerWeek = 7

    weeks = 2

    samplePlayerSize = 500000

    grindForPrimeEngrams = bool(0)

    levelingAlgorithm = LevelingAlgorithm()

    levelingAlgorithm.run(tier1Count, tier2Count, tier3Count,
                          primeEngramsPerWeek, primeEngram_drop_weight, weeks, gear_drop_weight, samplePlayerSize, grindForPrimeEngrams)


if __name__ == '__main__':
    testAlgo()
