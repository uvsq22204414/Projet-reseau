from abc import ABC, abstractmethod
from paquet import Paquet

class Machine (ABC): 

	somme_temps_paquets = 0
	paquets_arrives = 0
	paquets_generes = 0
	paquets_perdus  = 0

	def __init__(self):
		self._connections = []
	

	def connect(self, m):
		self._connections.append(m)

	@abstractmethod
	def arrivee(self, p : Paquet):
		'''
			Gère l'arrivée d'un paquet p
		'''
		pass

	@abstractmethod
	def transmission(self, m):
		'''
			Gère la transmission à une machine m
		'''
		pass

	@abstractmethod
	def update(self):
		pass