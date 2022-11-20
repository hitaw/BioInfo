import math
from enumeration import *

def DIST_1(x,y):
	n = len(x)
	m = len(y)
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
					sub = T[i-1][j-1] + csub(x[i], y[j])
					T[i][j] = min(ins,sup,sub)
	return T

def SOL_1(x,y,T):
	i = len(x)-1
	j = len(y)-1
	x_ali = ""
	y_ali = ""

	while i > 0 or j > 0:
		if j > 0 and T[i][j] == T[i][j-1] + CINS:
			x_ali = "-" + x_ali
			y_ali = y[j] + y_ali
			j -= 1
		elif i > 0 and T[i][j] == T[i-1][j] + CDEL:
			x_ali = x[i] + x_ali
			y_ali = "-" + y_ali
			i -= 1
		elif i > 0 and j > 0 and T[i][j] == T[i-1][j-1] + csub(x[i],y[j]):
			x_ali = x[i] + x_ali
			y_ali = y[j] + y_ali
			i -= 1
			j -= 1
		else:
			raise Exception("Erreur")
			return (None,None)
	return (x_ali,y_ali)

print(SOL_1("ATCG","CGAT",DIST_1("ATCG","CGAT")))