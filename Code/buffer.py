from machine import Machine
from paquet import Paquet
from fifo import Fifo
from source import Source

from time import time

class Buffer (Machine):
	
	def __init__(self, e : int):
		super().__init__()
		self.__taille_m = e + 1
		self._queue_paquets = Fifo()
		self._date_arrivee = Fifo()


	def arrivee(self, p: Paquet):
		'''
			Insère le paquet s'il reste de la place dans la file
		'''
		if self._queue_paquets.length < self.__taille_m:
			self.insertion(p)
			print(f'Paquet reçu par un buffer : {p}')
			return True
		else:
			print("Buffer plein. Le paquet a été perdu dommage ╮(╯▽╰)╭")
			Machine.paquets_perdus += 1
			return False

	def transmission(self, m: Machine):
		'''
			Transmet le premier paquet
		'''
		# Vérifie si le temps de tick est écoulé (pour éviter de transmettre
		# un paquet qui est arrivé dans le quantum de temps actuel)
		if time() - self._date_arrivee.avant > 0.001:
			p = self._queue_paquets.avant
			print(f"Un buffer envoie {p}")
			m.arrivee(p)
			return True
		else:
			return False

	def insertion(self, p: Paquet):
		'''
			Insère un paquet dans la file
		'''
		self._queue_paquets.enfiler(p)
		self._date_arrivee.enfiler(time())
		

	def retrait(self, p: Paquet):
		'''
			 Retire un paquet de la file
		'''
		if p in self._queue_paquets:
			self._queue_paquets.supprimer(p)
			return p
		else:
			print("Le paquet n'est pas dans la file")

	def update(self):
		'''
			Vérifie s'il faut envoyer un paquet, si oui, l'envoyer.
		'''
		if self._queue_paquets.length > 0:
			transmis = False # Vérifie si un paquet n'a pas été transmit à cause du temps de tick
			for m in self._connections:
				transmis = self.transmission(m)
			if transmis: # Si on a bien transmit le paquet, c'est que le temps de tick est passé. On peut défiler le paquet
				self._queue_paquets.defiler()
				self._date_arrivee.defiler()

	@property
	def taille_m(self):
		return self.__taille_m
	

	@property
	def queue(self):
		return self._queue_paquets

	def __add__(self, p: Paquet):
		pass
	
	def __sub__(self, p: Paquet):
		pass

	def __eq__(self, b):
		return self._queue_paquets == b._queue_paquets

	def __lt__(self, b): # Strictement plus petit
		return len(self._queue_paquets) < len(b._queue_paquets)

	def __gt__(self, b): # Strictement plus grand
		return not (self < b or self == b)

	def __repr__(self):
		return f"Buffer de taille max {self.__taille_max}"
