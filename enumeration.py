import math

def DIST_NAIF_REC(x, y, i, j, c, dist):
	if (i == len(x) and j == len(y)):
		if (c<dist):
			dist = c
	else :
		if (i<len(x) and j<len(y)):
			dist = DIST_NAIF_REC(x, y, i+1, j+1, c + c, dist)
		if (i<len(x)):
			dist = DIST_NAIF_REC(x, y, i+1, j, c + c, dist)
		if (j<len(y)):
			dist = DIST_NAIF_REC(x, y, i, j+1, c + c, dist)
	return dist

def DIST_NAIF(x, y):
	dist = math.inf
	return DIST_NAIF_REC(x, y, 0, 0, 0, dist)