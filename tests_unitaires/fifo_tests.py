from test_unitaire import *
from fifo import Fifo

class FifoTest (TestUnitaire):

	def run(self):
		return self.enfile_defile() and self.length() and self.priorite() and self.file_vide()

	def file_vide(self):
		f = Fifo()
		return f.defiler() == None

	def enfile_defile(self):
		f = Fifo()
		f.enfiler(10)
		a = f.defiler()

		return a == 10

	def priorite(self):
		f = Fifo()
		f.enfiler("A")
		f.enfiler("B")
		f.enfiler("C")

		return f.defiler() == "A"

	def length(self):
		f = Fifo()
		for i in range(10):
			f.enfiler(1)
		for i in range(3):
			f.defiler()

		return f.length == 7

	def __repr__(self):
		return "Test fifo"

FifoTest()