import sapai.shop as sh
import random as rand
import numpy as np


# This function returns a list containing the mean, median, and maximum values of pets on a given turn
# pet_values: a 66-element dictionary containing the values of each pet by name
# shop: the shop object
# avail_pets: an array of pets available in the current turn
def turn_stats(pet_values, turn):
    avail_values = []
    for pet in sh.pet_tier_avail_lookup(turn):
        avail_values.append(pet_values[pet])
    return [min(avail_values), max(avail_values)]


# generates a 5x5 matrix of values for the gold function
# rows: # of empty spaces
# columns: # of gold: 0 - 3, 1 - 6, 2 - 9, 3 - 4 or 5, 4 - 7 or 8, 5 - 10
def generate_threshold(empty_spaces, gold):
    parameters = np.empty(6, 6)
    parameters[0, 1] = rand.uniform(0, 1)
    parameters[0, 2] = rand.uniform(0, parameters[0, 1])
    parameters[0, 3] = rand.uniform(0, parameters[0, 2])
    parameters[0, 4] = rand.uniform(0, parameters[0, 3])
    parameters[0, 5] = rand.uniform(0, parameters[0, 4])
    for i in range(0, 6):
        for j in range(0, 6):
            if i == 0 and j == 0:
                parameters[i, j] = 1
            elif i == 0:
                parameters[i, j] = rand.uniform(0, parameters[i, j-1])
            else:
                parameters[i, j] = rand.uniform(parameters[i-1, j], parameters[i-1, j-1])
    return parameters


# implements the gold function using (6,6) values similar to the shape returned by generate_thresholds
def threshold_function(parameters, empty_spaces, gold):
    switch = {
        0: parameters[empty_spaces, 0],
        1: parameters[empty_spaces, 0],
        2: parameters[empty_spaces, 0],
        3: parameters[empty_spaces, 0],
        4: parameters[empty_spaces, 3],
        5: parameters[empty_spaces, 3],
        6: parameters[empty_spaces, 1],
        7: parameters[empty_spaces, 4],
        8: parameters[empty_spaces, 4],
        9: parameters[empty_spaces, 2],
        10: parameters[empty_spaces, 5],
    }
    return switch.get(gold)
