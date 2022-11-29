from TacheA import *

#Tests DIST_NAIF:
"""
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_44.adn")

d = DIST_NAIF(x,y)

if d == 10: print("Valide pour Inst_0000010_44.adn")

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_7.adn")

d = DIST_NAIF(x,y)

if d == 8: print("Valide pour Inst_0000010_7.adn")

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_8.adn")

d = DIST_NAIF(x,y)

if d == 2: print("Valide pour Inst_0000010_8.adn")"""

#Inst_0000012_56.adn : 0.31 min
#Inst_0000013_45 : 1 min 25
#Inst_0000013_56 : 2 min 34

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000013_89.adn")

start = time.time()
DIST_NAIF(x,y)
end = time.time()

elapsed = (end - start)/60
print(f"Temps d'exécution : {elapsed:.2}min")
