from sapai.pets import Pet
import math
import numpy as np

pet = Pet("ant")
print(pet)
### Printing pet is given in the form of < PetName Attack-Health Status Level-Exp >
pet._attack += 3
pet.gain_experience()
print(pet)

print(pet.ability)


def decorator(cls):
    class Wrapper:
        def __init__(self, value=0):
            self.wrap = cls()
            self.value = value
    return Wrapper

# Determines
def stat_function(mult, func, x):
    switch = {
        'sigmoid': mult(1 / (1 + math.exp(-(x - 51) / 49))),
        'quadratic': mult(((x - 2) / 98) ^ 2),
        'linear': mult((x - 2) / 98),
        'sum': mult(1 / (1 + math.exp(-(x - 51) / 49))) + mult(((x - 2) / 98) ^ 2)
               + mult((x - 2) / 98)
    }
    return switch.get(func)

def simple_value(att, hp, type, status):


def value(combat_multiplier, function, att, hp, long_val, faint_val, status_val):
    total = att + hp
    return stat_function(combat_multiplier,function,total) + long_val + faint_val + status_val


def value_stat_change(team, mult, func, position, change, targets):
    team[position]

#def long_term_value():
