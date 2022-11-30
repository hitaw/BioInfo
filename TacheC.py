from TacheB import *

def DIST_2(x,y):
	""" 
	Calcule la distance d'édition de (x,y) avec une complexité spatiale moindre

	Entrée :

	x : str
	y : str 

	Sortie :
	
	T : list(int)
	D(x,y) : int
	"""

	n = len(x)+1
	m = len(y)+1
	T = [[0]*m for i in range(2)]						#On initialise cette fois un tableau de taille m*2

	for i in range(m):
		T[0][i] = i * CINS
	
	for i in range(1,n):
		T[1] = [0] * m

		for j in range(m):
			if j == 0:
				T[1][j] = i * CDEL

			else:
				ins = T[1][j-1] + CINS
				sup = T[0][j] + CDEL
				sub = T[0][j-1] + csub(x[i-1], y[j-1])
				T[1][j] = min(ins,sup,sub)

		if i != n - 1:
			T[0] = [k for k in T[1]]					#On remplace la première ligne par la ligne courante

	return (T,T[1][m-1])