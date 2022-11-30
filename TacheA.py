import math
import time
from ouverture_fichier import *
CDEL = 2
CINS = 2

def csub(a, b):
	""" 
	Calcul de csub

	Entrée :

	a : str
	b : str
	len(a) == 1
	len(b) == 1 

	Sortie :

	CSUB : int
	"""

	if (a == b):
		return 0

	if (a in ("A", "T") and b in ("A", "T")) or (a in ("G","C") and b in ("G","C")):
		return 3

	return 4


def DIST_NAIF_REC(x, y, i, j, c, dist):

	""" 
	Calcule le coût du meilleur alignement de (x,y) connu après l'appel

	Entrée : 

	x : str
	y : str
	i : int <= len(x)
	j : int <= len(y)
	c : int
	dist : int 

	Sortie :

	dist : int
	"""

	if (i == len(x) and j == len(y)):
		if (c < dist):
			dist = c
	else :
		if (i<len(x) and j<len(y)):
			dist = DIST_NAIF_REC(x, y, i+1, j+1, c + csub(x[i],y[j]), dist)

		if (i<len(x)):
			dist = DIST_NAIF_REC(x, y, i+1, j, c + CDEL, dist)

		if (j<len(y)):
			dist = DIST_NAIF_REC(x, y, i, j+1, c + CINS, dist)

	return dist

def DIST_NAIF(x, y):
	""" 
	Appel de la fonction DIST_NAIF_REC() pour calculer la distance d'édition de (x,y)

	Entrée :

	x : str
	y : str 

	Sortie :

	D(x,y) : int
	"""

	dist = math.inf

	return DIST_NAIF_REC(x, y, 0, 0, 0, dist)


