#Partie 4

from TacheD import *
import random

L = ["A","C","T","G"]
k = 1

def generate_instance(n, m):
	""" Prérequis : 
	n : int
	m : int """
	global k

	nom_fic = "Instances_partie_quatre/Instance_" + str(k) +".adn"
	k += 1
	f = open(nom_fic, "w")

	if f is None:
		raise Exception("Erreur lors de l'ouverture du fichier")
		return None

	for i in range(n):
		f.write(random.choice(L))

	f.write("\n")

	for i in range(m):
		f.write(random.choice(L))

	f.close()

	return nom_fic

instance1 = generate_instance(1000,10)
instance2 = generate_instance(5000,100)
instance3 = generate_instance(15000,500)

print("\n")

f = open(instance1, "r")
lines = f.readlines()
f.close()

x = lines[0]
x = x.replace("\n","")
y = lines[1]
y = y.replace("\n","")

T, d = DIST_2(x,y)

print("Distance d'édition pour n = 1000, m = 10 : " + str(d))
print("(m - n) * CDEL = " + str((len(x)-len(y))*CDEL))
print("\n")

f = open(instance2, "r")
lines = f.readlines()
f.close()

x = lines[0]
x = x.replace("\n","")
y = lines[1]
y = y.replace("\n","")

T, d = DIST_2(x,y)

print("Distance d'édition pour n = 5000, m = 100 : " + str(d))
print("(m - n) * CDEL = " + str((len(x)-len(y))*CDEL))
print("\n")

f = open(instance3, "r")
lines = f.readlines()
f.close()

x = lines[0]
x = x.replace("\n","")
y = lines[1]
y = y.replace("\n","")

T, d = DIST_2(x,y)

print("Distance d'édition pour n = 15000, m = 500 : " + str(d))
print("(m - n) * CDEL = " + str((len(x)-len(y))*CDEL))
print("\n")




