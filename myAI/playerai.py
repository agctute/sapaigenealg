from sapai.player import Player
import numpy as np


# This class will contain the weights of an AI
# We should be able to generate random weights, reproduce using parents, and mutate it
# We should also be able to obtain a sequence of actions during a buy phase that improves a team
# Variables:
# tier_list: a 51x51 array containing the values of a pet based on its stats. Since the indices denote the stats
# corresponding to the value, the first row and column will be 0 due to zero-indexing
class AI:
    def __init__(self, tier_list, player):
        self.player = player
        self.tier_list = tier_list
        if tier_list.shape != [51, 51]:
            raise Exception("tier_list shape not correct\nExpected: " + str([51, 51]) + '\nReceived: ' +
                            str(tier_list.shape))

    # Given a Player object from the engine, the AI outputs a recommended set of actions of the form
    # TODO
    #
    #
    def actions(self, player):
        # Step 1: check for empty spaces
        # Step 2: if , buy the highest value pet
        # Potential shop values: determined or coded?
        # Need potential pets in each tier avail_pets method
        #

