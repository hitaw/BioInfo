from TacheD import *

#20000_77
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
print((end - start)/60)