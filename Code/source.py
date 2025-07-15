from machine import Machine
from paquet import Paquet
from random import random


class Source (Machine):

	generation_probability = 0.1

	def __init__(self, s: str, generator = True):
		super().__init__()
		self.__nom = s
		self.__a_envoyer = None
		self.__is_generator = generator

	@property
	def nom(self):
		return self.__nom
	

	def arrivee(self, p: Paquet):
		'''
            Affiche le nom de la source et le contenu du paquet
        '''
		print(f"{self.__nom} reçoit {p}")
		self.__a_envoyer = p
		if not self.__is_generator:
			Machine.somme_temps_paquets += p.age
			Machine.paquets_arrives += 1

	def transmission(self, m: Machine):
		'''
            Transmet __a_transmettre
        '''
		if self.__a_envoyer == None:
			return False
		print(f"{self.__nom} transmet {self.__a_envoyer}")
		m.arrivee(self.__a_envoyer)
		self.__a_envoyer = None
		return True

	def update(self):

		# Transmet le paquet à tous les successeurs
		for m in self._connections:
			self.transmission(m)
		
		# Génère un paquet si les conditions sont réunies
		if self.__is_generator and random() < Source.generation_probability:
			self.__a_envoyer = Paquet()
			Machine.paquets_generes += 1

	@property
	def a_envoyer(self):
		return self.__a_envoyer

	def __repr__(self):
		return f"Source {self.__nom}"
