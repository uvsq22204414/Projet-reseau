import tkinter as tk

class Tab:
	'''
		Classe représentant un onglet de l'application
	'''

	tabs = []
	def __init__(self, window, name, on_show = None):
		'''
			window  : Fenêtre de l'application
			name    : Titre de l'onglet
			on_show : Fonction à appeler lorsque l'onglet devient visible 
		'''
		self.__widgets = []
		self.__id = len(Tab.tabs)
		self.__handle = tk.Button(window, text = name, command = self.show, relief = "flat", bg = "#FFFFF0", bd = 4)
		self.__handle.grid(row = 0, column = len(Tab.tabs))
		self.__on_show = on_show

		Tab.tabs.append(self)

	def show(self):
		'''
			Cache tous les widgets et affiche self
		'''
		self.__handle["state"] = "disabled"
		for t in Tab.tabs:
			if t != self:t.hide()

		self.set_visible(True)

		# Appel de la fonction on_show
		if self.__on_show != None:
			self.__on_show()

	def hide(self):
		self.__handle["state"] = "normal"
		self.set_visible(False)

	def set_visible(self, b):
		'''
			Réaffiche tous les widgets
		'''
		for i in range(len(self.__widgets)):
			w = self.__widgets[i]
			if b:
				w.grid(row = 1 + i, column = 0, columnspan = len(Tab.tabs))
			else:
				w.grid_forget()

	def add_widget(self, w):
		self.__widgets.append(w)

