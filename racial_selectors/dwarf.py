'''Racial generators for dwarves'''

# from random import choice
from custom_random import weighted_choice

def dwarf_trait():
  'Returns a randomly selected trait'
  trait_weights = [
    ('Cavesight', 8),
    ('Children of the Earth', 16-8),
    ('Consume Alcohol', 25-16),
    ('Dwarven Warfare', 33-25),
    ('Grudgebearer', 41-33),
    ('Ironclad', 49-41),
    ('Oathkeeper', 58-49),
    ('Physical Prowess', 67-58),
    ('Rune-marked Glory', 76-67),
    ('Stentorian Voice', 85-76),
    ('Stoneheaded', 92-85),
    ('Strength of the Mountain', 100-92),
  ]

  return weighted_choice(trait_weights)
