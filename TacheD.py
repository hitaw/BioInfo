from TacheC import *


def mot_gaps(k):

	""" 
	Retourne le mot composé de k gaps

	Entrée :

	k : int 

	Sortie :

	s : str
	"""

	return "-"*k

def align_lettre_mot(x,y):

	""" 
	Crée le meilleur alignement pour la lettre x et le mot y

	Entrée : 

	x : str
	y : str
	len(x) = 1
	len(y) > 0 

	Sortie :

	(x_ali, y_ali) : tuple(str)

	"""

	m = len(y)

	for j in range(m):
		if x == y[j]:
			return(mot_gaps(j)+x+mot_gaps(m-j-1),y)

	for j in range(m):
		if csub(x, y[j])<CDEL+CINS:
			return (mot_gaps(j)+x+mot_gaps(m-j-1),y)

	return (mot_gaps(m-1)+x, y)


def coupure(x,y):

	""" 
	Trouve l'indice j auquel une coupure peut se faire dans le cadre de la méthode diviser pour mieux régner

	Entrée :

	x : str
	y : str 

	Sortie :

	j : int
	"""

	i_etoile = len(x)//2
	n = len(x)+1
	m = len(y)+1
	T = [[0]*m for i in range(2)]
	
	if i_etoile == 0:									#On crée le tableau D contenant les distances d'édition jusqu'à l'indice i_etoile
		D = DIST_2(x[:i_etoile+1],y)[0]
	else:
		D = DIST_2(x[:i_etoile],y)[0]
	D[1] = [0]*m

	for i in range(i_etoile, n):
		for j in range(m):
			if j == 0:									#Reproduction de DIST_2
				D[1][j] = i * CDEL

			else:
				ins = D[1][j-1] + CINS
				sup = D[0][j] + CDEL
				sub = D[0][j-1] + csub(x[i-1], y[j-1])
				D[1][j] = min(ins,sup,sub)

				if i == i_etoile:
					T[1][j] = j

				elif D[1][j] == sup:
					T[1][j] = T[0][j]

				elif D[1][j] == ins:
					T[1][j] = T[1][j-1]

				else:
					T[1][j] = T[0][j-1]

		D[0] = [k for k in D[1]]						#On remplace les premières lignes des tableaux par leur ligne courante respective
		T[0] = [k for k in T[1]]
	return T[1][m-1]

def SOL_2(x,y):

	""" 
	Crée récursivement le meilleur alignement du couple (x,y) à l'aide de la méthode diviser pour mieux régner

	Entrée : 

	x : str
	y : str 

	Sortie :

	(x_ali, y_ali) : tuple(str)
	"""

	n = len(x)
	m = len(y)

	if n == 0:										#Si x est un mot vide, alors on renvoie y ainsi qu'un mot composé de len(y) gaps.
		return (mot_gaps(m), y)

	if m == 0:										#Si y est un mot vide, alors on renvoie x ainsi qu'un mot composé de len(x) gaps.
		return (x, mot_gaps(n))

	if n == 1:										#Si x est une lettre, alors on renvoie la lettre alignée au mot y
		return align_lettre_mot(x,y)

	if m == 1:										#Si y est une lettre, alors on renvoie la lettre alignée au mot x
		y1, x1 = align_lettre_mot(y,x)
		return (x1,y1)

	i = n//2

	j = coupure(x,y)								#On trouve l'indice j associé à l'indice i

	x1,y1 = SOL_2(x[:i],y[:j])
	x2,y2 = SOL_2(x[i:],y[j:])

	return (x1+x2,y1+y2)							#On renvoie la concaténation entre la partie gauche et la partie droite de x et y