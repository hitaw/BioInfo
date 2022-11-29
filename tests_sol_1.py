from TacheB import *
import matplotlib.pyplot as plt

elapsed = []
taille = []

#10_7
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000010_7.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#12_56
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000012_56.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#13_89
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000013_89.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#14_7
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000014_7.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#15_2
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000015_2.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#20_8
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000020_8.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#50_9
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000050_9.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#100_44
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000100_44.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#500_88
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0000500_88.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#1000_2
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0001000_2.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#2000_44
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0002000_44.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#3000_1
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0003000_1.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#5000_32
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0005000_32.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#8000_32
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0008000_32.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#10000_7
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0010000_7.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

#15000_3
x,n,y,m = ouvrir_fichier("Instances_genome/Inst_0015000_3.adn")

start = time.time()
PROG_DYN(x,y)
end = time.time()

taille.append(n)
elapsed.append((end - start))

plt.plot(taille, elapsed)
plt.title("Temps pris par SOL_1 en fonction de la taille de x")
plt.xlabel("Taille de x")
plt.ylabel("Temps (en secondes)")
plt.savefig("images/SOL1.png")

print("tests_sol_1 done")