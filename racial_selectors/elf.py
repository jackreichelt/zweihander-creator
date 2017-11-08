'''Racial generators for elves'''

# from random import choice
from custom_random import weighted_choice

def elf_trait():
  'Returns a randomly selected trait'
  trait_weights = [
    ('Bewitching', 8),
    ('Beyond the Veil', 16-8),
    ('Deadly Aim', 25-16),
    ('Enduring Mortality', 33-25),
    ('Fey Treachery', 41-33),
    ('Firstborn', 49-41),
    ('Kindred Warband', 58-49),
    ('Lament of the Ages', 67-58),
    ('Meditative Healing', 76-67),
    ('Nature\'s Own', 85-76),
    ('Nighteyes', 92-85),
    ('Warrior\'s Tattoo', 100-92),
  ]

  return weighted_choice(trait_weights)
