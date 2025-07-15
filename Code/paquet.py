from random import randint
import time

class Paquet:

	temps_initial = time.time() # Temps auquel le programme est lancé

	def __init__(self):
		self.__contenu = chr(randint(69, 90)) + chr(randint(69, 90)) + chr(randint(69, 90)) # Contenu aléatoire
		self.__creation_time = time.time() - Paquet.temps_initial # Temps entre le début du programme et la création de ce paquet
		#print(self.__creation_time)
	


	@property
	def contenu(self):
		return self.__contenu
	
	@property
	def age(self):
		return time.time() - self.__creation_time - Paquet.temps_initial
	
	@property
	def color(self):
		'''
			Renvoie une couleur basée sur le nom du paquet
		'''
		def chr_to_value(c):
			# Fonction bijective de 69..94 sur 0..255
			return int(255 * (ord(c) - 69)/25)

		return (chr_to_value(self.__contenu[0]), chr_to_value(self.__contenu[1]), chr_to_value(self.__contenu[2]))

	def __repr__(self):
		return f"Paquet contenant {self.__contenu}"