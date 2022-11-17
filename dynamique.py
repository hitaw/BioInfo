import math
import enumeration

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
					T[i][j] = min(min(CDEL,CINS),csub(x[i], y[m])) + T[i-1][j-1]