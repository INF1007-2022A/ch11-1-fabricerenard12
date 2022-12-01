"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@classmethod
	def make_unarmed(cls):
		return Weapon('Unarmed', cls.UNARMED_POWER, 1)

	@property
	def name(self):
		return self.__name


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.__weapon = Weapon.make_unarmed()
		self.hp = max_hp

	def compute_damage(self, defender):
		crit = (random.choices([1, 2], [0.9375, 0.0625])[0] == 2)
		modifier =  (2 if crit else 1) * random.uniform(0.85, 1)
		damage = ((((2 * self.level / 5) + 2) * self.weapon.power * (self.attack / defender.defense) / 50) + 2) * modifier
		return damage, crit

	@property
	def name(self):
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, wpn):
		if wpn == None:
			wpn = Weapon.make_unarmed()
		if wpn.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = wpn


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage = attacker.compute_damage(defender)[0]
	defender.hp -= damage

	return f'{attacker.name} used {attacker.weapon.name}\n\t{defender.name} took {damage} dmg'


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f'{c1.name} starts a battle with {c2.name}!')
	nb_tours = 0
	while c1.hp > 0 and c2.hp > 0:
		if nb_tours % 2 == 0:
			print(deal_damage(c1, c2))
		elif nb_tours % 2 == 1:
			print(deal_damage(c2, c1))
		nb_tours += 1

	return nb_tours
