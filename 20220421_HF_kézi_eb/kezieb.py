class Jatekos:
    def __init__(self,egysor):
    darabok=egysor.split(";")
    self.nev=darabok[0]
    self.dobottgol=int(darabok[1])
    self.kapuraloves=int(darabok[2])
    self.sikereshetmeteres=int(darabok[3])
    self.hetesproba=int(darabok[4])
    self.ketperceskiallitas=int(darabok[])
    self.poszt=int(darabok[6])
    self.magassag=int(darabok[8])
    self.csapat=int(darabok[9])
f=open("kezieb.txt","r" encoding="utf8")
beolvas=f.readlines()
f.close()
jatekosok=[]
for item in beolvas:
    jatekosok.append(Jatekos(item))
print(jatekosok[0].nev)
# hf 2,3,4,8,11,14