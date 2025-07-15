from test_unitaire import *
from paquet import Paquet
from buffer import Buffer
import time

class BufferTest (TestUnitaire):

	def run(self):
		return self.test_arrivee() and self.test_transmission()

	def test_arrivee(self):
		b = Buffer(2)
		p = Paquet()
		b.arrivee(p)
		b.arrivee(p)
		return not b.arrivee(p)

	def test_transmission(self):
		b = Buffer(2)
		c = Buffer(2)
		b.connect(c)

		b.arrivee(Paquet())
		time.sleep(0.1)
		b.update()

		return b.queue.length == 0 and c.queue.length == 1
	

	def __repr__(self):
		return "Tests du Buffer"

BufferTest()