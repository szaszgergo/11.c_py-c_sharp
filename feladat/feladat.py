class Magassag:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.orszag = darabok[0]
        self.foldrajzi_hely = darabok[1]
        self.magassag = int(darabok[2])
        

with open("tengerszint.txt") as f : 
    beolvas = f.readlines()

adatok=[]
for sor in beolvas:
    adatok.append(Magassag(sor))


print(f"10.feladat:\n\t{len(adatok)} legmagassabb pontja szerepel a listán.")

bt5000=0
for magassag in adatok:
    if magassag.magassag > 5000:
        bt5000+=1
print(f"11.feladat: {bt5000} ország legnagyobb tengerszint feletti magassága haladja meg az 5000 métert.")






hetezer= []
for magassag in adatok:
    if magassag.magassag > 7500 : 
        hetezer.append(magassag.orszag)
        hetezer.append(magassag.foldrajzi_hely)
        hetezer.append(magassag.magassag)




f = open("magasak.txt" ,"w") 
f.write(str(hetezer))
f.close()
