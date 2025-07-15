from abc import ABC, abstractmethod

class MachineDrawing (ABC):
	'''
		Représente le visuel d'une machine
	'''
	def __init__(self, target, canvas):
		self._target = target # Machine à dessiner
		self._canvas = canvas # Canvas sur lequel dessiner

	@abstractmethod
	def update(self):
		pass

class SourceDrawing (MachineDrawing):
	'''
		Visuel des sources
	'''
	def __init__(self, target, x, y, unit, canvas):
		super().__init__(target, canvas)

		# Création du dessin
		self.__rec = self._canvas.create_rectangle(x, y, x + unit, y + unit)

	def update(self):
		'''
			Dessine la source en blanc si elle est vide
			ou en la couleur du paquet sinon.
		'''
		color = "white"

		if self._target.a_envoyer != None:
			color = self._target.a_envoyer.color
			color = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'

		self._canvas.itemconfigure(self.__rec, fill = color)

class BufferDrawing (MachineDrawing):
	'''
		Visuel des buffers
	'''

	def __init__(self, target, x, y, unit, canvas):
		super().__init__(target, canvas)
		self.__rects = []

		# Création des dessins
		for i in range(self._target.taille_m - 1):
			self.__rects.append(self._canvas.create_rectangle(x + i * unit, y, x + (i + 1) * unit, y + unit))


	def update(self):
		'''
			Dessine la file de paquets
		'''

		for i in range(len(self.__rects)):
			
			queue_i = i

			color = "white"
			if self._target.queue.length > queue_i and self._target.queue.as_list()[queue_i] != None:
				color = self._target.queue.as_list()[queue_i].color
				color = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
			self._canvas.itemconfigure(self.__rects[i], fill = color)