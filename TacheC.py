from TacheB import *

def DIST_2(x,y):
	n = len(x)+1
	m = len(y)+1
	T = [[0]*m for i in range(2)]

	for i in range(m):
		T[0][i] = i * CINS
	
	for i in range(1,n):
		T[1] = [0]*m
		for j in range(m):
			if j == 0:
				T[1][j] = i * CDEL
			else:
				ins = T[1][j-1] + CINS
				sup = T[0][j] + CDEL
				sub = T[0][j-1] + csub(x[i-1], y[j-1])
				T[1][j] = min(ins,sup,sub)
		T[0] = T[1]
	return T[1][m-1]