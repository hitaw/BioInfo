from TacheC import *


def mot_gaps(k):

	""" Prérequis :
	k : int """

	return "-"*k

def align_lettre_mot(x,y):

	""" Prérequis : 
	x : str
	y : str
	len(x) = 1
	len(y) > 0 """

	m = len(y)

	for j in range(m):
		if x == y[j]:
			return(mot_gaps(j)+x+mot_gaps(m-j-1),y)

	for j in range(m):
		if csub(x, y[j])<CDEL+CINS:
			return (mot_gaps(j)+x+mot_gaps(m-j-1),y)

	return (mot_gaps(m)+x, y+"-")

def coupure(x,y):

	""" Prérequis :
	x : str
	y : str """

	i_etoile = len(x)//2
	n = len(x)+1
	m = len(y)+1
	T = [[0]*m for i in range(2)]
	D = DIST_2(x[:i_etoile-1],y)[0]
	D[0] = [i for i in D[1]]

	for i in range(i_etoile, n):
		D[1][0] = i * CDEL
		for j in range(1,m):
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
		
		D[0] = [k for k in D[1]]
		T[0] = [k for k in T[1]]
	return T[1][m-1]

def SOL_2(x,y):

	""" Prérequis : 
	x : str
	y : str """

	n = len(x)
	m = len(y)

	if n == 0:
		return (mot_gaps(m), y)

	if m == 0:
		return (x, mot_gaps(n))

	if n == 1:
		return align_lettre_mot(x,y)

	if m == 1:
		y1, x1 = align_lettre_mot(y,x)
		return (x1,y1)

	i = n//2

	j = coupure(x,y)

	x1,y1 = SOL_2(x[:i],y[:j])
	x2,y2 = SOL_2(x[i:],y[j:])

	return (x1+x2,y1+y2)
