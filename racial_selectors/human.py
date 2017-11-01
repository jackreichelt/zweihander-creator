from random import choice
from custom_random import weighted_choice

def human_trait():
  trait_weights = [
    ('Blessing in Disguise', 8),
    ('Danger Sense', 16-8),
    ('Dauntless', 25-16),
    ('Esoteric Memory', 33-25),
    ('Fortune\'s Wheel', 41-33),
    ('Grim Resolve', 49-41),
    ('Manifest Destiny', 58-49),
    ('Mixed Bloodline ({})'.format(choice(['Dwarf', 'Gnome', 'Halfling', 'Ogre', 'Elf'])), 67-58),
    ('Mountain Amongst Men', 76-67),
    ('Natural Selection', 85-76),
    ('Noble Savage', 92-85),
    ('Seventh Sense', 100-92),
  ]
  
  return weighted_choice(trait_weights)
  
  