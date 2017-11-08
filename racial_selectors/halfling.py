'''Racial generators for halflings'''

# from random import choice
from custom_random import weighted_choice

def halfling_trait():
  'Returns a randomly selected trait'
  trait_weights = [
    ('Beguiler', 8),
    ('Cat-like Reflexes', 16-8),
    ('Craven', 25-16),
    ('Farsight', 33-25),
    ('Fettered Chaos', 41-33),
    ('Fieldwarden', 49-41),
    ('Fleet-footed', 58-49),
    ('Hijinks', 67-58),
    ('Kleptomania', 76-67),
    ('Low Blow', 85-76),
    ('Memento', 92-85),
    ('Pintsized', 100-92),
  ]

  return weighted_choice(trait_weights)
