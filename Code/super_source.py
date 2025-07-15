from machine import Machine
from buffer import Buffer
from source import Source
import random
from paquet import Paquet
from time import time

class SuperSource (Buffer):
	'''
		La SuperSource est une source pouvant gérer une queue. De manière purement
		pratique, elle dérive de Buffer, mais du fait des similitudes entre les
		Buffer et les sources, on peut la traiter comme une Source?
	'''

	entities = []
	strategy = "None"
	tour     = 0

	def __init__(self, e: int, g = True):
		super().__init__(e)

		self.__is_generator = g
		self.__id = len(SuperSource.entities)

		SuperSource.entities.append(self)

	def transmission(self, m):
		'''
			Transmet le premier paquet
		'''
		# Vérifie si le temps de tick est écoulé (pour éviter de transmettre
		# un paquet qui est arrivé dans le quantum de temps actuel)
		if time() - self._date_arrivee.avant > 0.001:
			p = self._queue_paquets.avant
			print(f"Une super source envoie : {p}")
			if not m.arrivee(p):
				print("\tMais la machine d'arrivée est pleine... Patientons.")
				return False
			return True
		else:
			return False

	def update(self):
		'''
			Met à jour self et gère les différentes stratégies
		'''

		if self.__id == 0:
			if SuperSource.strategy == "TurnByTurn":
				# On alterner régulièrement entre les SuperSource.
				SuperSource.tour += 1
				if SuperSource.tour >= len(SuperSource.entities):
					# Overflow
					SuperSource.tour = 0
			elif SuperSource.strategy == "BiggerFirst":
				# On priorise la source la plus encombrée.
				SuperSource.tour = 0
				
				# On cherche la source la plus encombrée...
				for i in range(len(SuperSource.entities)):
					if SuperSource.entities[i]._queue_paquets.length > SuperSource.entities[SuperSource.tour]._queue_paquets.length:
						SuperSource.tour = i
			elif SuperSource.strategy == "Random":
				SuperSource.tour = random.randint(0, len(SuperSource.entities) - 1)
			else:
				# Aucune stratégie particulière
				SuperSource.tour = -1

		# Generation de paquet
		if self.__is_generator and random.random() < Source.generation_probability:
			self.arrivee(Paquet())
			Machine.paquets_generes += 1

		# Si la source est choisie par la stratégie, on lui permet de se
		# mettre à jour
		if SuperSource.tour == -1 or SuperSource.tour == self.__id:
			super().update()