from random import randint

def d10(number=1, bonus=0):
  total = 0
  for i in range(number):
    total += randint(1, 10)
  return total + bonus

def d100(number=1, bonus=0):
  total = 0
  for i in range(number):
    total += randint(1, 100)
  return total + bonus

def d(sides, number=1, bonus=0):
  total = 0
  for i in range(number):
    total += randint(1, sides)
  return total + bonus

def weighted_choice(choices):
  '''
    Takes in an array of tuples in the format [(choice1, weight1), (chioice2, weight2)]
    Weights are relative to the total count, not out of a specific number
  '''
  total_weights = sum(w, for c, w in choices)
  roll = randint(1, total)
  upto = 0
  
  for c, w in choices:
    if r <= upto + w:
      return c
    upto += w