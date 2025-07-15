from abc import ABC, abstractmethod
import sys
sys.path.append("../code/")

class TestUnitaire (ABC):

	__instances = [] # Variable de classe qui retient toutes les instances crées

	def __init__(self):
		'''
			On ajoute chaque instance à __instances
		'''
		TestUnitaire.__instances.append(self)

	@abstractmethod
	def run(self):
		'''
			Méthode abstraite qui fait tourner tous les tests unitaires d'une classe
		'''
		return False


	@classmethod
	def run_all(cls):
		'''
			Méthode de classe qui fait tourner tous les tests unitaires du projet
		'''
		success = 0
		failures = []
		for t in cls.__instances:
			if t.run():
				success += 1
			else:
				failures.append(repr(t))

		print("_______________________________________")
		print(f"Test lancés : {len(cls.__instances)}\nTests réussis : {success}")
		if len(failures) > 0:
			print("Echecs :")
			for f in failures:
				print(f"\t{f}")
		else:
			print("Aucun echec !")
		print("_______________________________________")
