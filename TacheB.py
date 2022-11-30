from TacheA import *

def DIST_1(x,y):

	""" 
	Calcul la distance d'édition de (x,y)

	Entrée :

	x : str
	y : str

	Sortie :

	T : list[int] 
	D(x,y) : int
	"""

	n = len(x)+1
	m = len(y)+1
	T = [[0] * m for i in range(n)]					#T de taille (len(x)+1)*(len(y)+1) pour gérer le mot vide

	#T[0][0] est ici déjà égal à 0, on peut passer directement au parcours de i et j

	for i in range(n): 								#On parcourt x
 		for j in range(m): 							#On parcourt y
 			if i == 0:								#Quand on est à la première lettre de x :
 				T[i][j] = j * CINS					#On donne le résultat de la multiplication de l'indice j et du coût d'une insertion à la case [0][j] du tableau T
 			elif j == 0:							#Quand on est à la première lettre de y :
 				T[i][j] = i * CDEL					#On donne le résultat de la multiplication de l'indice i et du coût d'une suppression à la case [i][0] du tableau T

 			else:
 				ins = T[i][j-1] + CINS
 				sup = T[i-1][j] + CDEL
 				sub = T[i-1][j-1] + csub(x[i-1], y[j-1])
 				T[i][j] = min(ins,sup,sub) 			#Minimum entre le coût d'une insertion, d'une suppression et d'une substitution

	return (T,T[n-1][m-1]) 							#On récupère également T pour pouvoir l'utiliser dans SOL_1

def SOL_1(x,y,T):

	""" 
	Trouve le meilleur alignement de (x,y)

	Entrée :

	x : str
	y : str
	T : list[int]
	len(T) > 0
	T est le tableau contenant les distances d'édition à chaque étape de x et y 

	Sortie :

	(x_ali, y_ali) : meilleur alignement de (x,y)
	"""

	i = len(x)
	j = len(y)
	x_ali = ""
	y_ali = ""

	while i > 0 or j > 0:							#Tant qu'il reste des lettres à étudier on continue.
		if j > 0 and T[i][j] == T[i][j-1] + CINS:	#S'il reste des lettres à y et que le coût minimal correspond à une insertion, on fait l'insertion
			x_ali += "-"
			y_ali += y[j-1]
			j -= 1 									#Comme on a géré y[j-1], on décrémente j

		elif i > 0 and T[i][j] == T[i-1][j] + CDEL:	#S'il reste des lettres à x et que le coût minimal correspond à une suppression, on fait la suppression
			x_ali += x[i-1]
			y_ali += "-"
			i -= 1 									#Comme on a géré x[i-1], on décrémente i

		else:										#Sinon cela veut dire que le coût minimal est une substitution, on fait donc la substitution
			x_ali += x[i-1]
			y_ali += y[j-1]
			i -= 1 									#Comme on a géré x[i-1] et y[j-1], on décrémente i et j
			j -= 1

	return (x_ali[::-1],y_ali[::-1])				#On retourne les string inversées, pour avoir les lettres dans le bon ordre

def PROG_DYN(x,y):
	""" 
	Retourne la distance d'édition et le meilleur alignement de (x,y)

	Entrée :

	x : str
	y : str 

	Sortie :
	D(x,y) : int
	(x_ali, y_ali) : tuple(str)
	"""

	T,d = DIST_1(x,y)

	return (d, SOL_1(x,y,T))