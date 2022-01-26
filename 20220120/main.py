from random import * 

def feladat1():
    elemszam = int(input("Add meg az elemek számát!"))
    szamok = []
    paratlan = []
    for i in range(elemszam):
        szamok.append(randint(1,50))
    for item in szamok:
        if item%2 != 0 :
            paratlan.append(item)
    print("A páratlanok száma",len(paratlan))
#feladat1()
def feladat2():
    elemszam = int(input("Add meg az elemek számát!"))
    szamok=[]
    parosok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    for item in szamok:
        if item%2 == 0 :
            parosok.append(item)
    print(sum(parosok),"Páros számok összege  ")

#feladat2()


'''
 elemszam = int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))

'''
def feladat3():
    elemszam = int(input("Add meg az elemek számát!"))
    szamok=[]
    parosok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    for item in szamok:
        if item%2 == 0 :
            parosok.append(item)
    print(parosok)
    print(szamok.index(parosok))



feladat3()