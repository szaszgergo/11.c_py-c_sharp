class Etel:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.nev=darabok[0]
        self.ar=int(darabok[1])
        self.tipus=darabok[2]

def feladat2():

    print("1. Feladat : Az éterem ", len(etelek),"féle ételt kínál .")


def feladat3():

    db = 0 
    osszeg = 0 
    for item in etelek:
        if item.tipus=="Leves":
            db += 1
            osszeg += item.ar
    print("3. Feladat: A levesek átlagos ára : ", osszeg/db,"forint")


def feladat4():
    db = 0 
    
    for item in etelek:
        if item.tipus=="Főétel":
            db += 1
            
    print("4. Feladat: ", db,"Főétel van.")

 


f = open("etelek.txt","r")
beolvas=f.readlines()
f.close()
etelek= []
for item in beolvas:
    etelek.append(Etel(item))

feladat2()


levesar=[]
for item in etelek:
    if item.tipus== "Leves":
        levesar.append(item.ar)
print("3. Feladat: A levesek átlagos ára : ", sum(levesar)/len(levesar),"forint")


feladat3()
feladat4()


for item in etelek:
    if "liba" in item.nev.lower():
        print(item.nev)



