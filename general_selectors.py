from custom_random import d10, d100
from random import choice

def primary_attributes():
  attributes = {
    'Combat'      : d10(3,25),
    'Brawn'       : d10(3,25),
    'Agility'     : d10(3,25),
    'Perception'  : d10(3,25),
    'Intelligence': d10(3,25),
    'Willpower'   : d10(3,25),
    'Fellowship'  : d10(3,25),
  }

  return attributes

def gender():
  return choice(['Female', 'Male'])

def race(chance=10):
  if d100() > 100-chance:
    return choice(['Dwarf', 'Gnome', 'Halfling', 'Ogre', 'Elf'])
  else:
    return 'Human'

def racial_modifiers(race):
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