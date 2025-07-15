from test_unitaire import TestUnitaire
from buffer_tests import BufferTest
from fifo_tests import FifoTest
from paquet_tests import PaquetTest
from source_tests import SourceTest

if __name__ == "__main__":
	# Faire tourner les tests unitaires
	TestUnitaire.run_all()