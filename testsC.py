from TacheC import *
import matplotlib.pyplot as plt

elapsed = []
taille = [10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000,15000,20000]

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

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
elapsed.append((end - start)/60)

#Pour n = 50000 : > 10 minutes

plt.plot(taille, elapsed)
plt.show()