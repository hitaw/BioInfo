from TacheA import *

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_44.adn")

d = DIST_NAIF(x,y)

if d == 10: print("Valide pour Inst_0000010_44.adn")

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_7.adn")

d = DIST_NAIF(x,y)

if d == 8: print("Valide pour Inst_0000010_7.adn")

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_8.adn")

d = DIST_NAIF(x,y)

if d == 2: print("Valide pour Inst_0000010_8.adn")

#Inst_0000012_56 : 19 secondes
#Inst_0000013_45 : 41 secondes
#Inst_0000013_56 : 46 secondes
#Inst_0000013_89 : 45 secondes
#Inst_0000014_7 : 1 minute 39 secondes
#Inst_0000014_23 : 12 secondes
#Inst_0000014_83 : 1 min 41s

x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000015_2.adn")

start = time.time()
DIST_NAIF(x,y)
end = time.time()

elapsed = (end - start)
minutes = int(elapsed//60)
secondes = int(elapsed%60)
temps = str(minutes) + " min " + str(secondes) + " sec"
print("Temps d'exécution : " + temps)
