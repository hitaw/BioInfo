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

	j = 0
	m = len(y)

	while j < m:
		if csub(x, y[j])<CDEL+CINS:
			if j > 0:
				return (mot_gaps(j)+x+mot_gaps(m-j-1),y)
			else:
				return (x+mot_gaps(m-1),y)
		j += 1

	return (mot_gaps(j)+x, y+"-")

def coupure(x,y):

	""" Prérequis :
	x : str
	y : str """

	i_etoile = len(x)//2
	n = len(x)+1
	m = len(y)+1
	T = [[0]*m for i in range(2)]

	for i in range(i_etoile, n):
		for j in range(m):
			if i == i_etoile:
				T[1][j] = j

			else:
				D, v = DIST_2(x[:i],y[:j])
				mini = min(D[0][j], D[0][j-1], D[1][j-1])

				if mini == D[1][j-1]:
					T[1][j] = T[1][j-1]

				elif mini == D[0][j]:
					T[1][j] = T[0][j]

				else:
					T[1][j] = T[0][j-1]

		if i != n - 1:
			T[0] = T[1]

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
		return(x, mot_gaps(n))

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