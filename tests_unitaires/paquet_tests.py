from test_unitaire import TestUnitaire
from paquet import Paquet
from time import sleep

class PaquetTest (TestUnitaire):
	
	def run(self):
		p = Paquet()
		return int(p.age) == 0

	def __repr__(self):
		return "Tests des paquets";

PaquetTest()