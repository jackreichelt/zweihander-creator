'''A module of functions for random dice roles'''
from random import randint

def d10(number=1, bonus=0):
  'Return the result of a 10 sided die'
  total = 0
  for _ in range(number):
    total += randint(1, 10)
  return total + bonus

def d100(number=1, bonus=0):
  'Return the result of a 100 sided die'
  total = 0
  for _ in range(number):
    total += randint(1, 100)
  return total + bonus

def dnum(sides, number=1, bonus=0):
  'Return the result of a die with an arbitrary number of sides'
  total = 0
  for _ in range(number):
    total += randint(1, sides)
  return total + bonus

def weighted_choice(choices):
  '''
    Takes in an array of tuples in the format [(choice1, weight1), (chioice2, weight2)]
    Weights are relative to the total count, not out of a specific number
  '''
  total_weights = sum(w for c, w in choices)
  roll = randint(1, total_weights)
  upto = 0

  for choice, weight in choices:
    if roll <= upto + weight:
      return choice
    upto += weight
