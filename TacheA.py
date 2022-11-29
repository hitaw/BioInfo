import math
import time
from ouverture_fichier import *
CDEL = 2
CINS = 2

def csub(a, b):
	""" Prérequis :
	a : str
	b : str
	len(a) == 1
	len(b) == 1 """

	if (a == b):
		return 0

	if (a in ("A", "T") and b in ("A", "T")) or (a in ("G","C") and b in ("G","C")):
		return 3

	return 4


def DIST_NAIF_REC(x, y, i, j, c, dist):

	""" Prérequis : 
	x : str
	y : str
	i : int
	j : int
	c : int
	dist : int 
	i <= len(x)
	j <= len(y) """

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
	""" Prérequis :
	x : str
	y : str """

	dist = math.inf

	return DIST_NAIF_REC(x, y, 0, 0, 0, dist)


