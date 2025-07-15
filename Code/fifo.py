class Fifo:
	def __init__(self):
		self.__data = []

	def enfiler(self, element):
		self.__data = [element] + self.__data

	def defiler(self):
		if self.length == 0:
			return None
		a = self.__data[-1]
		self.__data.pop()
		return a

	def supprimer(self, elem):
		self.__data = [e for e in self.__data if e != elem]


	def as_list(self):
		return list(self.__data) # Retourne une copie du contenu sous forme de liste

	@property
	def avant(self):
		if self.length == 0:
			return None
		return self.__data[-1]

	@property
	def length(self):
		return len(self.__data)
