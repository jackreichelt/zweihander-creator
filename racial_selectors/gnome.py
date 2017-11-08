'''Racial generators for gnomes'''

# from random import choice
from custom_random import weighted_choice

def gnome_trait():
  'Returns a randomly selected trait'
  trait_weights = [
    ('Clockworks of War', 8),
    ('Crag Fighting', 16-8),
    ('Denizen of Stone', 25-16),
    ('Dungeons Deep', 33-25),
    ('Escape Artist', 41-33),
    ('Goldbergian', 49-41),
    ('Hocus Pocus', 58-49),
    ('Metrognome', 67-58),
    ('Thieving Stunties', 76-67),
    ('Tunnel Vision', 85-76),
    ('Underfoot', 92-85),
    ('Wretched Prankster', 100-92),
  ]

  return weighted_choice(trait_weights)
