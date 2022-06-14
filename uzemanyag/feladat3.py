class Valtozas:
    def __init__(self, sor):
        darabok=sor.strip('\n').split(';')
        datum=darabok[0].split('.')
        self.datum = darabok[0]
        self.ev=int(datum[0])
        self.honap=int(datum[1])
        self.nap=int(datum[2])
        self.benzinar=int(darabok[1])
        self.gazolajar=int(darabok[2])
        self.kulonbseg = abs(self.gazolajar - self.benzinar)


with open('uzemanyag.txt') as f:
    beolvas = f.readlines()

valtozasok = []
for sor in beolvas:
    valtozasok.append(Valtozas(sor))

#3.feladat
print('3. feladat: változások száma:', len(valtozasok))
#4.feladat
legkisebb = 0 
for valtozas in valtozasok:
    if valtozas.kulonbseg> legkisebb:
        legkisebb =valtozas.kulonbseg
print(f"A legkisebb változás a {legkisebb}")
#5.feladat

szamol = 0 
for valtozas in valtozasok:
    if valtozas.kulonbseg == legkisebb:
        szamol +=1
print(f"A legkisebb kulonbseg {szamol}-szer van a listában")

#6. feladat
vane = False
for valtozas in valtozasok:
    if valtozas.ev%4==0:
        if valtozas.honap ==2 and valtozas.nap == 24:
            vane = True

if vane:
    print(" volt változás szökőnapon")

else:
    print("nem volt változás szökőnapon")


#7.feladat
with open("euro.txt", "w") as f:
    eu = 307.7
    for valtozas in valtozasok:
        benzineuro= round(valtozas.benzinar/eu,2)
        gazolajeuro= round(valtozas.gazolajar/eu,2)
        f.write(f"{valtozas.datum};{benzineuro};{gazolajeuro}\n")