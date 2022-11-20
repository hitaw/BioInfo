import math
import time
CDEL = 2
CINS = 2

def csub(a, b):
	if (a == b):
		return 0
	if ((a in ("A", "T") and b in ("A", "T")) or (a in ("G","C") and b in ("G","C"))):
		return 3
	return 4


def DIST_NAIF_REC(x, y, i, j, c, dist):
	if (i == len(x) and j == len(y)):
		if (c<dist):
			dist = c
	else :
		if (i<len(x) and j<len(y)):
			dist = DIST_NAIF_REC(x, y, i+1, j+1, c + csub(x[i],y[j]), dist)
		if (i<len(x)):
			dist = DIST_NAIF_REC(x, y, i+1, j, c + CDEL, dist)
		if (j<len(y)):
			dist = DIST_NAIF_REC(x, y, i, j+1, c + CINS, dist)
	return dist

def DIST_NAIF(x, y):
	dist = math.inf
	return DIST_NAIF_REC(x, y, 0, 0, 0, dist)

"""f = open("Instances_genome/Inst_0000010_44.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

print(DIST_NAIF(x,y))

f = open("Instances_genome/Inst_0000010_7.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

print(DIST_NAIF(x, y))

f = open("Instances_genome/Inst_0000010_8.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

print(DIST_NAIF(x,y))"""

"""
test n = 13, m = 10, t = 55.8 s
test n = 12, m = 11, t = 1 min 6 s
test n = 14, m = 10, t = 1 min 48 s
test n = 14, m = 9, t = 35.4 s
test n = 15, m = 9, t = 1 min 6 s
test n = 11, m = 11, t = 49.2 s
text n = 12, m = 12, t = 3 min 9 s

Il n'y a donc pas vraiment de longueur maximale d'instance que l'on peut résoudre en moins d'une minute.
Si l'on prend n = 200 et m = 1, alors cette méthode se fera en moins d'une minute (même en moins d'une seconde).
Cependant, si l'on fait se rapprocher m et n au maximum, alors la taille d'instance max sera n = 13 et m = 10
Et si l'on pose n = m alors n = 11 sera la taille d'instance max que l'on peut résoudre en moins d'une minute.

x = "ACGTACGTACGT"
y = "ACGTACGTACGT" 

start = time.time()
print(DIST_NAIF(x,y))
end = time.time()
elapsed = (end - start)/60


print(f"Temps d'exécution : {elapsed:.2}min")"""
