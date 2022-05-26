class Magassag:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.orszag = darabok[0]
        self.foldrajzi_hely = darabok[1]
        self.magassag = int(darabok[2])


f = open("tengerszint.txt","r")
beolvas = f.readlines()
f.close()
orszagok = []
for item in beolvas:
   orszagok.append(Magassag(item))
print("10.",len(orszagok))
db5000=0 
for item in orszagok:
    if item.magassag> 5000:
        db5000 +=1
    print("5000-nél ",db5000,"csúcs van")
vanbenne=False
for item in orszagok:
    if item.magassag = 5000 : 
        vanbenne= True
    if vanbenne==True:
        print("Van")
    else:
        print("Nincs benne")

g= open("tengerszint.txt", "w" ,encoding="utf-8")
    for item in orszagok:
        fi item.magassag>7500:
        g.write(item.orszag+"\t"+item.foldrajzi_hely+"\t"+str(item.magassag))
        g.write("\r")
g.close()
atlaghoz = []
for item in orszagok:
    atlaghoz.append(item.magassag)
atlag=sum(atlaghoz)/len(atlaghoz)
