'''Racial generators for ogres'''

# from random import choice
from custom_random import weighted_choice

def ogre_trait():
  'Returns a randomly selected trait'
  trait_weights = [
    ('Broad-bellied', 8),
    ('Cast Iron Stomach', 16-8),
    ('Cruisin\' for a bruisin\'', 25-16),
    ('Frightening Bellow', 33-25),
    ('Gut-Plate', 41-33),
    ('Hunger Pangs', 49-41),
    ('Mighty Thews', 58-49),
    ('Odd Couple', 67-58),
    ('Rotgun Spray', 76-67),
    ('Slamdance', 85-76),
    ('Thick Lining', 92-85),
    ('Wendigo', 100-92),
  ]

  return weighted_choice(trait_weights)
