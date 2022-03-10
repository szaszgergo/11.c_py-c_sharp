class Csapat:
    def __init__(self,egysor): # speciális metodus konstruktor ( kezdőértékek beálitásáért felel)
        darabok=egysor.split(";")
        self.csapat = darabok[0]
        self.helyezes =int(darabok[1])
        self.valtozas =int(darabok[2])
        self.pontszam =int(darabok[3])




f = open("fifa.txt","r")
beolvas=f.readlines()


f.close()
csapatok= []
for i in range(1,len(beolvas)):
    csapatok.append(Csapat(beolvas[i]))  
print("3. feladat: A világ ranglistán", len(csapatok), "csapat szerepel")
osszeg = 0
for item in csapatok:
    osszeg += item.pontszam
atlag = osszeg/len(csapatok)
print("4. feladat : a csapatok átlagos pontszáma" , round(atlag,2) , "pont.")
valtozasok=[]
for item in csapatok:
    valtozasok.append(item.valtozas)
maxvaltozas = max(valtozasok)
maxvaltozasindex= valtozasok.index(maxvaltozas)
print("5. feladat : A legtöbbet javító csapat:")
print("\t Helyezés:", csapatok[maxvaltozasindex].helyezes)
print("\t Csapat:", csapatok[maxvaltozasindex].csapat)
print("\t Pontszám:", csapatok[maxvaltozasindex].pontszam)


print("5. feladat : A legtöbbet javító csapat:")

for item in csapatok:
    if item.valtozas==maxvaltozas:
        print("\t Helyezés:", item.helyezes)
        print("\t Csapat:", item.csapat)
        print("\t Pontszám:", item.pontszam)      
f=open("fifa.txt", "r")
minden=f.read()
f.close()
if "Magyarország" in minden:
    print("6. feladat: Csapatok között van Magyaroszág")
else: 
    print("6. feladat: Csapatok között nincs Magyaroszág")

vanbene = False
for item in csapatok:
    if item.csapat=="Magyarország":
        vanbene=True
        break

if vanbene:
        print("6. feladat: Csapatok között van Magyaroszág")
else: 
    print("6. feladat: Csapatok között nincs Magyaroszág")