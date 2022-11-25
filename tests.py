from TacheD import *
import os

#Tests DIST_NAIF:
"""f = open("Instances_genome/Inst_0000010_44.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

d = DIST_NAIF(x,y)

if d == 10: print("Valide pour Inst_0000010_44.adn")

f = open("Instances_genome/Inst_0000010_7.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

d = DIST_NAIF(x,y)

if d == 8: print("Valide pour Inst_0000010_7.adn")

f = open("Instances_genome/Inst_0000010_8.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

d = DIST_NAIF(x,y)

if d == 2: print("Valide pour Inst_0000010_8.adn")"""

#Inst_0000012_13.adn : 0.91 min
#Inst_0000012_32.adn : 0.93 min
#Inst_0000012_56.adn : 6.4 min

"""f = open("Instances_genome/Inst_0000012_32.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
y = lines[3]
y = y.replace(" ","")

start = time.time()
print(DIST_NAIF(x,y))
end = time.time()
elapsed = (end - start)/60
print(f"Temps d'exécution : {elapsed:.2}min")"""

#Mémoire utilisée : 0.3% de 15 926 MiB -> 4 777 MiB = 5009 MB

