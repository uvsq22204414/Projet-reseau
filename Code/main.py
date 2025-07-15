from machine import Machine
from source import Source
from super_source import SuperSource
from buffer import Buffer
from time import time, sleep
import tkinter as tk
from drawings import BufferDrawing, SourceDrawing
from application import Tab

def update_model(reseau, canvas, delay = 500):
	'''
		Fonction chargée de mettre à jour le réseau
		et d'afficher l'état avec des print.
	
		reseau : Liste contenant les sources et les buffers
		canvas : Canvas à utiliser pour appel en boucle de cette fonction
		delay  : Quantum de temps
	'''
	for m in reseau:
		m.update()

	print("Frame") # Affichée à chaque quantum de temps

	# On réappelle la fonction avec canvas.after pour réaliser
	# une boucle _non bloquante_
	canvas.after(delay, lambda: update_model(reseau, canvas, delay = delay))

def update_drawings(drawings, canvas):
	'''
		Met à jour le visuel du réseau

		drawings : Liste contenant les instances dérivant de MachineDrawing
		canvas   : Canvas à appeler pour bouclage non bloquant
	'''

	for d in drawings:
		d.update()

	# Bouclage _non bloquant_
	canvas.after(35, lambda: update_drawings(drawings, canvas))

def update_stats(stats, canvas):
    '''
        Fonction qui met à jour l'affichage des statistiques.

        stats : Un dictionnaire qui contient des labels d'affichage de statistiques
    '''
    if Machine.paquets_generes == 0:
        stats["Perte"].config(text="Aucun paquet généré.")
    else:
        stats["Perte"].config(text=str(int(Machine.paquets_perdus/Machine.paquets_generes * 100)) + "% de pertes")

    if Machine.paquets_arrives == 0:
        stats["Temps"].config(text="Aucun paquet arrivé.")
    else:
        stats["Temps"].config(text=f"Temps de vie moyen : {round(Machine.somme_temps_paquets/Machine.paquets_arrives, 2)} s")

    # Bouclage _non bloquant_
    canvas.after(35, lambda: update_stats(stats, canvas))


def reinit_stats():
	Machine.paquets_generes = 0
	Machine.paquets_perdus  = 0
	Machine.somme_temps_paquets = 0
	Machine.paquets_arrives = 0
def set_random_strategy():
	reinit_stats()
	SuperSource.strategy = "Random"
def set_turn_strategy():
	reinit_stats()
	SuperSource.strategy = "TurnByTurn"
def set_bigger_strategy():
	reinit_stats()
	SuperSource.strategy = "BiggerFirst"

if __name__ == "__main__":

	win = tk.Tk()
	win.title("Projet IN407")
	win.minsize(0, 600)
	win.resizable(0, 0)
	win.option_add('*Font', 'Arial 10')

	# Initialisation des onglets
	tabs = {
		"Demo"   : Tab(win, "Démonstration du réseau"),
		"Lambda" : Tab(win, "Variation du lambda"),
		"Stats"  : Tab(win, "Statistiques"),
		"Strat1" : Tab(win, "Plus encombrée en priorité", set_bigger_strategy),
		"Strat2" : Tab(win, "A tour de rôle", set_turn_strategy),
		"Strat3" : Tab(win, "Aléatoire", set_random_strategy)
	}


	# Création du réseau
	reseau = [
		SuperSource(3),
		SuperSource(3),
		Buffer(2),
		Buffer(2),
		Source("C", False),
		Source("D", False)
	]
	reseau[0].connect(reseau[2])
	reseau[1].connect(reseau[2])
	reseau[2].connect(reseau[3])
	reseau[3].connect(reseau[4])
	reseau[3].connect(reseau[5])

	# Création du canvas
	can = tk.Canvas(win, width = 400, height = 400, bg = "#FFFFF0")
	drawings = [
		BufferDrawing(reseau[0], 10, 50, 32, can),
		BufferDrawing(reseau[1], 10, 150, 32, can),
		BufferDrawing(reseau[2], 150, 100, 32, can),
		BufferDrawing(reseau[3], 250, 100, 32, can),
		SourceDrawing(reseau[4], 350, 50, 32, can),
		SourceDrawing(reseau[5], 350, 150, 32, can),
	]

	# Création du widget affichant les statistiques
	class GenProbVar:
		def set(self, v):
			Source.generation_probability = float(v)
			Machine.paquets_generes = 0
			Machine.paquets_perdus  = 0
			Machine.somme_temps_paquets = 0
			Machine.paquets_arrives = 0
	user_input = GenProbVar()
	stats = {
		"Perte" : tk.Label(win, text = "undefined"),
		"Temps" : tk.Label(win, text = "undefined")
	}

	# Remplissage des onglets
	tabs["Lambda"].add_widget(tk.Label(win, text = "Choisir la densité de génération :"))
	tabs["Lambda"].add_widget(tk.OptionMenu(win, user_input, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0))
	for stat in stats:
		tabs["Stats"].add_widget(stats[stat])
	tabs["Strat1"].add_widget(tk.Label(win, text = "La source la plus encombrée est maintenant priorisée !"))
	tabs["Strat2"].add_widget(tk.Label(win, text = "On choisit les sources tour à tour."))
	tabs["Strat3"].add_widget(tk.Label(win, text = "On choisit une source aléatoire à chaque quantum."))

	for tab in tabs:
		tabs[tab].add_widget(can)

	tabs["Demo"].show()


	# Appels des fonctions boucles non bloquantes
	update_stats(stats, can)
	update_model(reseau, can, 500)
	update_drawings(drawings, can)

	win.mainloop()
