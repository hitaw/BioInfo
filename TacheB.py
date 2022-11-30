from TacheA import *

def DIST_1(x,y):

	""" Prérequis :
	x : str
	y : str """

	n = len(x)+1
	m = len(y)+1
	T = [[0] * m for i in range(n)]

	for i in range(n): #on parcourt x
 		for j in range(m): #on parcourt y
			if i == 0: #quand on est à la première lettre de x
				T[i][j] = j * CINS #on donne le résultat de la multiplication de l'indice j et du coût d'une insertion à la case [0][j] du tableau T
			elif j == 0:#quand on est à la première lettre de y
				T[i][j] = i * CDEL #on donne le résultat de la multiplication de l'indice i et du coût d'une suppression à la case [i][0] du tableau T

			else:
				ins = T[i][j-1] + CINS
				sup = T[i-1][j] + CDEL
				sub = T[i-1][j-1] + csub(x[i-1], y[j-1])
				T[i][j] = min(ins,sup,sub)

	return (T,T[n-1][m-1]) #On récupère également T pour pouvoir l'utiliser dans SOL_1

def SOL_1(x,y,T):

	""" Prérequis :
	x : str
	y : str
	T : list
	len(T) > 0
	T est le tableau contenant les distances d'édition à chaque étape de x et y """

	i = len(x)
	j = len(y)
	x_ali = ""
	y_ali = ""
	#L'implémentation actuelle de python optimise la concaténation de string avec "+=" de sorte à ce que la complexité soit approximativement la même qu'avec une liste, nous avons donc choisi d'utiliser des string pour les alignements.

	while i > 0 or j > 0:
		if j > 0 and T[i][j] == T[i][j-1] + CINS:
			x_ali += "-"
			y_ali += y[j-1]
			j -= 1

		elif i > 0 and T[i][j] == T[i-1][j] + CDEL:
			x_ali += x[i-1]
			y_ali += "-"
			i -= 1

		else:
			x_ali += x[i-1]
			y_ali += y[j-1]
			i -= 1
			j -= 1

	return (x_ali[::-1],y_ali[::-1])

def PROG_DYN(x,y):
	""" Prérequis :
	x : str
	y : str """

	T,d = DIST_1(x,y)

	return (d, SOL_1(x,y,T))