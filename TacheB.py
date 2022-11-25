import math
from TacheA import *
import matplotlib.pyplot as plt

def DIST_1(x,y):
	n = len(x)+1
	m = len(y)+1
	T = [[0] * m for i in range(n)] 
	#comme on initialise toutes les cases à 0, il n'y a pas besoin de gérer le cas i == 0 && j == 0

	for i in range(n):
		for j in range(m):
			if i == 0:
				if j != 0:
					T[i][j] = j * CINS
			else:
				if j == 0:
					T[i][j] = i * CDEL
				else:
					ins = T[i][j-1] + CINS
					sup = T[i-1][j] + CDEL
					sub = T[i-1][j-1] + csub(x[i-1], y[j-1])
					T[i][j] = min(ins,sup,sub)

	return (T,T[n-1][m-1]) #On récupère également T pour pouvoir l'utiliser dans SOL_1

def SOL_1(x,y,T):
	i = len(x)
	j = len(y)
	x_ali = ""
	y_ali = ""

	if len(T)==0:
		raise Exception("Le tableau est vide")
		return None
	while i > 0 or j > 0:
		if j > 0 and T[i][j] == T[i][j-1] + CINS:
			x_ali = "-" + x_ali
			y_ali = y[j-1] + y_ali
			j -= 1
		elif i > 0 and T[i][j] == T[i-1][j] + CDEL:
			x_ali = x[i-1] + x_ali
			y_ali = "-" + y_ali
			i -= 1
		elif i > 0 and j > 0 and T[i][j] == T[i-1][j-1] + csub(x[i-1],y[j-1]):
			x_ali = x[i-1] + x_ali
			y_ali = y[j-1] + y_ali
			i -= 1
			j -= 1
		else:
			raise Exception("Erreur")
			return None
	return (x_ali,y_ali)

def PROG_DYN(x,y):
	T,d = DIST_1(x,y)
	return (d, SOL_1(x,y,T))