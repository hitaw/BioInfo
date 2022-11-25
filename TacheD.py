from TacheC import *

def mot_gaps(k):
	return "-"*k

def align_lettre_mot(x,y):
	"""Hypothèses : len(x) = 1, len(y) > 0"""
	j = 0
	m = len(y)
	while j < m:
		if csub(x, y[j])<CDEL+CINS:
			if j > 0:
				return (mot_gaps(j)+x+mot_gaps(m-j-1),y)
			else:
				return(x+mot_gaps(m-1),y)
		j += 1
	return (mot_gaps(j)+x, y+"-")

x = "A"
y = "CTG"

print(align_lettre_mot(x,y))