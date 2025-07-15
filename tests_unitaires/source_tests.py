from test_unitaire import TestUnitaire
from source import Source
from paquet import Paquet
from buffer import Buffer

import time

class SourceTest (TestUnitaire):

	def run(self):
		return self.test_const() and self.test_transmission()

	def test_const(self):
		s = Source("Test")
		return s.nom == "Test"

	def test_transmission(self):
		s = Source("Test")
		b = Buffer(1)
		s.connect(b)
		s.arrivee(Paquet())
		time.sleep(0.1)
		s.update()
		return b.queue.length == 1

	def __repr__(self):
		return "Tests de la source"

SourceTest()