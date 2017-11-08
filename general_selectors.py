'''These are rollers and selectors that are general across all races and careers'''

from random import choice
from custom_random import d10, d100

def primary_attributes():
  'Roll for the primary attributes of the character'
  attributes = {
    'Combat'      : d10(3, 25),
    'Brawn'       : d10(3, 25),
    'Agility'     : d10(3, 25),
    'Perception'  : d10(3, 25),
    'Intelligence': d10(3, 25),
    'Willpower'   : d10(3, 25),
    'Fellowship'  : d10(3, 25),
  }

  return attributes

def gender():
  'Select a random gender'
  return choice(['Female', 'Male'])

def race(chance=10):
  'Roll for a race. Change of being non-human can be altered'
  if d100() > 100 - chance:
    return choice(['Dwarf', 'Gnome', 'Halfling', 'Ogre', 'Elf'])
  return 'Human'

def racial_modifiers(char_race):
  'Return\'s the racial modifiers for the character\'s race'
  bonuses = {
    'Human'   : ['CB', 'IB', 'PB'],
    'Dwarf'   : ['BB', 'CB', 'WB'],
    'Gnome'   : ['AB', 'IB', 'WB'],
    'Halfling': ['AB', 'FB', 'PB'],
    'Ogre'    : ['BB', 'BB', 'CB'], # duplicates intentional. represent a +2 bonus
    'Elf'     : ['AB', 'PB', 'IB'],
  }

  penalties = {
    'Human'   : ['AB', 'FB', 'WB'],
    'Dwarf'   : ['AB', 'FB', 'PB'],
    'Gnome'   : ['BB', 'CB', 'FB'],
    'Halfling': ['BB', 'CB', 'IB'],
    'Ogre'    : ['AB', 'AB', 'PB'], # duplicates intentional. represent a -2 penalty
    'Elf'     : ['BB', 'FB', 'WB'],
  }

  return bonuses[char_race], penalties[char_race]
