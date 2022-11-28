from TacheC import *
import matplotlib.pyplot as plt

elapsed = []
taille = [10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000,15000,20000,50000]

#10_7
f = open("Instances_genome/Inst_0000010_7.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#12_56
f = open("Instances_genome/Inst_0000012_56.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#13_89
f = open("Instances_genome/Inst_0000013_89.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#14_7
f = open("Instances_genome/Inst_0000014_7.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#15_2
f = open("Instances_genome/Inst_0000015_2.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#20_8
f = open("Instances_genome/Inst_0000020_8.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#50_9
f = open("Instances_genome/Inst_0000050_9.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#100_44
f = open("Instances_genome/Inst_0000100_44.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#500_88
f = open("Instances_genome/Inst_0000500_88.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#1000_2
f = open("Instances_genome/Inst_0001000_2.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#2000_44
f = open("Instances_genome/Inst_0002000_44.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#3000_1
f = open("Instances_genome/Inst_0003000_1.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#5000_32
f = open("Instances_genome/Inst_0005000_32.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#8000_32
f = open("Instances_genome/Inst_0008000_32.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#10000_7
f = open("Instances_genome/Inst_0010000_7.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#15000_3
f = open("Instances_genome/Inst_0015000_3.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#20000_77
f = open("Instances_genome/Inst_0020000_77.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))

#Pour n = 50000 : > 10 minutes
#50000_88
f = open("Instances_genome/Inst_0050000_88.adn", "r")
lines = f.readlines()
f.close()

x = lines[2]
x = x.replace(" ","")
x = x.replace("\n","")
y = lines[3]
y = y.replace(" ","")
y = y.replace("\n","")

start = time.time()
DIST_2(x,y)
end = time.time()
elapsed.append((end - start))
print("ok18")

plt.plot(taille, elapsed)
plt.title("Temps pris par DIST_2 en fonction de la taille de x")
plt.xlabel("Taille de x")
plt.ylabel("Temps (en secondes)")
plt.savefig("images/DIST2.png")