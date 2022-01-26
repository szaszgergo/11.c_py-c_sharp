from random import * 

def feladat1():
    szamok=[]
    a = int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
   
    print(szamok)
    db=0
    for item in szamok:
        if item%2==1:
            db=db+1
    if db>0:
        print("A páratlanok száma:", db)
    else:
        print("Nincsenek páratlan számok.")

#feladat1()
def feladat2():
    szamok=[]
    parosok= []
    a = int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
    print(szamok)
    for item in szamok : 
        if item%2 ==0 :
            parosok.append(item)
        else: 
            print(" ")
    print("A párosok összege : ",sum(parosok))
#feladat2()

def feladat3():
    szamok=[]
    a = int(input("Add meg a számok számát: "))
    for i in range(a):
        szamok.append(int(input("Kérek egy számot: ")))
    print(szamok)
    for item in szamok:
        if item %2==0:
            print(item,"a",szamok.index(item),". indexen van")
#feladat3()
def feladat4():

    szamok=[]
    szam= int(input("Add meg a számok számát: "))
    for i in range(szam):
        szamok.append(int(input("Kérek egy számot: ")))
    print(szamok)
    x = int(input("Kérek egy számot"))
    for item in szamok : 
        if item == x :
            print(item,"a listában a  ",szamok.index(item),". helyen van ")
        elif  x != item :
            print("Nincs benne a listában")
#feladat4()
def feladat5():
    szamok=[]
    szam= int(input("Add meg a számok számát: "))
    for i in range(szam):
        szamok.append(int(input("Kérek egy számot: ")))
    print(szamok)
    beker = int(input("Kérek egy egész számot"))
    print("A bekért szám",szamok.count(beker) ,"szerepel a listában.")
#feladat5()
def feladat6():
    szamok=[]
    szam= int(input("Add meg a keresztnevek számát: "))
    for i in range(szam):
        szamok.append(input("Kérek egy keresztnevet: "))
    print(szamok)
    beker = input("Írj be egy keresztnevet ")
    print("A bekért név",szamok.count(beker) ,"szerepel a listában.")
#feladat6()

def feladat7():
    szamok=[]
    szam= int(input("Add meg a számok  számát: "))
    for i in range(szam):
        szamok.append(int(input("Kérek egy számot ")))
    print(szamok)
    a = (max(szamok)- min(szamok))
    print("A legnagyobb és a legkisebb különbsége",abs(a))

feladat7()