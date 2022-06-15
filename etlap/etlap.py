class Etel:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.nev=darabok[0]
        self.ar=int(darabok[1])
        self.tipus=darabok[2]
        self.leg=len(self.nev)

with open("etlap.txt", encoding="utf-8") as f:
    beolvas = f.readlines()

etelek=[]

for sor in beolvas:
    etelek.append(Etel(sor))

print(f"2.fealdat:\n \tAz étlapon {len(etelek)} étel szerepel.")


levesek =[]
for sor in etelek:
    if sor.tipus == "Leves":
        levesek.append(sor.ar)
print(f"3.feladat: \n \tA levesek átlagos ára {sum(levesek)/len(levesek)}")

foetelek = 0
for sor in etelek:
    if sor.tipus == "Főétel":
        foetelek +=1

print(f"4.feladat: \n \t Az étlapon {foetelek} főételből lehet választani.")


print("5.feladat:")
for sor in etelek:
    if "liba" in sor.nev.lower():
        print(f"\t{sor.nev}")
        
deszertlegdragabb = []
for sor in etelek:
    if sor.tipus =="Desszert":
        deszertlegdragabb.append(sor.ar)
print(f"6.feladat: \n \t A legdrágább desszert: {max(deszertlegdragabb)}")

######################### min értékek tároloja 
legolcsobbteszta = []
legolcsobbfoetel=[]
legolcsobbsalata=[]
##################################################
for sor in etelek:
    if sor.tipus == "Főétel":
        legolcsobbfoetel.append(sor.ar)

for sor in etelek:                                                             # főételes számolás 
    if sor.tipus == "Saláta":
        legolcsobbsalata.append(sor.ar)
        break

for sor in etelek:
    if sor.tipus == "Tészta":
        legolcsobbteszta.append(sor.ar)                                         #tésztás számolás 
        
        break
##############################################
teszta_foetel= input("Főételt vagy tésztát szeretne enni?")
for sor in etelek:
    if teszta_foetel == "Főétel":
        print(f"7.feladat: \n \t A legocsóbb főétel plusz saláta {min(legolcsobbfoetel)+min(legolcsobbsalata)} ft-ba kerül.")
        break
    if teszta_foetel == "Tészta":
        print(f"7.feladat: \n \t A legolcsóbb tészta az étlapon {min(legolcsobbteszta)} ft-ba kerül.")
        break



print(f"8.feladat: \n Palacsintás ételek:")
for sor in etelek:
    if "palacsinta" in sor.nev.lower():
        print(f" \n \t  {sor.nev}")


vane = False

for sor in etelek:
    if "kacsa" in sor.nev.lower():
        vane = True
    else:
        vane = False

if vane:
    print(f"10.feladat: \n \tAz étlapon van kacsából készült étel.")
else:
    print(f"10.feladat: \n \tAz étlapon nincs kacsából készült étel.")

leghoszabbnevu = []

for sor in etelek:
    if len(sor.nev):
        leghoszabbnevu.append(len(sor.nev))

print(f"10.feladat(félig): \n \t A leghosszabb nevű étel{max(leghoszabbnevu)} karakterből áll.")

print(sor.leg)
    