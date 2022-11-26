from TacheD import *

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
SOL_2(x,y)
end = time.time()
elapsed.append((end - start)/60)
print("ok9")