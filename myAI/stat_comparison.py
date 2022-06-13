import math
import random as rand
import numpy as np

# Goal: Create a text file containing
# a "tier list" of stat values
# made by finding the number of wins and ties out of all potential
# enemy stats
def fight(att, hp, enemy_att, enemy_hp):
    outcome = math.ceil(enemy_hp / att) - math.ceil(hp / enemy_att)
    # if outcome negative: our pet wins
    # if outcome is zero: it is a tie
    # positive: lose
    if outcome > 0:
        return 0
    if outcome == 0:
        return 1
    if outcome < 0:
        return 2


def main():
    tier_list = np.empty([50*50, 3], int)
    index = 0
    for att in range(1, 51):
        for hp in range(1, 51):
            total = 0
            for enemy_att in range(1, 51):
                for enemy_hp in range(1, 51):
                    total += fight(att, hp, enemy_att, enemy_hp)
            tier_list[index, 0] = total
            tier_list[index, 1] = att
            tier_list[index, 2] = hp
            index += 1
    tier_list_sorted = tier_list[tier_list[:, 0].argsort()]
    with open('stat_tier_list.txt', 'w') as f:
        for i in range(50*50):
            f.write(str(tier_list_sorted[i, 0]) + ',' + str(tier_list_sorted[i, 1]) + ',' + str(tier_list_sorted[i, 2]) + '\n')
        f.close()


if __name__ == "__main__":
    main()
