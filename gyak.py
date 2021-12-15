from math import *
from random import *
def feladat1():
    a = str("nbfoahbfoainf")
def feladat2():
    b="a"
def feladat3():
    c=21
def feladat4():
    n=2.5
def feladat5():
    d=True
def feladat6():
    e=input("irj egy szot")
def feladat7():
    f=input("irj egy mondatot")
def feladat8():
    g=input("irj egy karaktert")
def feladat9():
    h=int(input("irj egy egész számot"))
def feladat10():
    i=float(input("irj egy valos számot"))
    print(i*2)
    print(i*pi)
    print(i**3)
    print(sqrt(i))
    print(round(i//2,2))
def feladat11():
    j=random.randint(10,50)
def feladat12():
    k=int(input("irj egy egész számot "))
    if k%2==0:
        print("páros a szám")
    else:
        print("páratlan a szám")
def feladat13():
    l=int(input("irj egy egész számot"))
    if l>0:
        print("pozitiv a szám")
    elif l<0:
        print("negativ a szám")
    else:
        print("a szám nulla")
def feladat14():
    m=int(input("irj egy egész számot"))
    if m>30:
        print("nagyobb mint 30")
    else:
        print("nem nagyobb mint 30")
def feladat15():
    aa=int(input("irj egy egész számot"))
    ab=int(input("irj egy egész számot"))
    if aa>ab:
        print(aa,"a nagyobb")
    else:
        print(ab,"a nagyobb")
def feladat16():
    ba=int(input("irj egy egész számot"))
    bb=int(input("irj egy egész számot"))
    if ba<bb:
        print(ba,"a kisebb")
    else:
        print(bb,"a kisebb")
def feladat17():
    o=input("irj egy szot")
    print(len(o))
def feladat18():
    u=input("irj egy szot")
    uu=u.count("e")
    print(uu)
def feladat19():

    a = input("írj egy szót ")
    keresendo = "aáeéiíoóöőuúüű"
    keresendok = 0
    for keres in a :
        if keres.lower() in keresendo:
            keresendok += 1
    print(keresendok , " ennyi magánhangzó van benne ")

def feladat20():
    a = input("írj egy szót ")
    print(len(a), " ennyi karakter van a szóban")

def feladat21():
    a = input("írj egy mondatott ")
    keresendo = " "
    keresendok = 0
    for keres in a :
        if keres in keresendo:
            keresendok += 1
    print(keresendok , "  szóköz van a mondatban ")


def feladat22():

    a = input("Kérek egy mondatott")
    mennyiseg=a.count("e")
    print(mennyiseg)

def feladat23():
    mondat = input("Kérek egy mondatott")

    szavak = mondat.split()

    print(len(szavak), ' szóból áll')


def feladat24():
    mondat = input("adj")
    szavak = mondat.split()
    for szo in szavak:
        print(len(szo), "karakterú hosszú",end=" ")

def feladat25():
    leghosszabb = 0
    for szo in szavak:
        if len(szo) > leghosszabb:
            leghosszabb = len(szo)
    print(leghosszabb)


def feladat26():

    a = input("Kérek egy mondatott megént geccc")
    jelolokk=".!?"
    mondat= 0
    for keres in a :
        if keres in jelolokk:
            mondat += 1
    print(mondat,"mondatból áll")
def feladat27():
    for i in range(1,10+1):
        print(i, end=" ")



def feladat28():
    for i in range(1, 11):
        print(i**2,end=" ")
def feladat29():
    for a in range (1,21):
       if a % 2 == 0:
            print(a, end=" ")



def feladat31():
    for a in range (10,101):
        if a%7==3:
            print(a,end=" ")

def feladat32():
     a = ["asdasdasdasdadsdasdadsdasd"]
def feladat33():
    a = ["aasdas","asdasdasdads","asdasdasda","asdasdasdadsasd","asdasdasdadsdasdadsadsd"]
def feladat34():
    a = ["a"]
def feladat35():
    a = ["asdasdasdadsasdads","kutyaaaaaa",1,3,5]
def feladat36():
    a = [2]
def feladat37():
    a = [3,5,12,323,4535]
def feladat38():
    a = [2.2]
def feladat39():
    a = [2.2,2.3,2.4,2.5,2.6]
def feladat40():
    veletlenek = []
    for i in range(10):
        veletlenek.append(randint(10, 50))
    print(veletlenek,end=" ")
    print(max(veletlenek),"legnagyobb")
    print(min(veletlenek),"legjisebb")
    print(sum(veletlenek),"összegük")
    print(sum(veletlenek)/15,"átlaguk")
    print(max(veletlenek)-min(veletlenek),"terjedelmük")






#feladat1()
#feladat2()
#feladat3()
#feladat4()
#feladat5()
#feladat6()
#feladat7()
#feladat8()
#feladat9()
#feladat10()
#feladat11()
#feladat12()
#feladat13()
#feladat14()
#feladat15()
#feladat16()
#feladat17()
#feladat18()
#feladat19()
#feladat20()
#feladat21()
#feladat22()
#feladat23()
#feladat24()
#feladat25()
#feladat26()
#feladat27()
#feladat28()
#feladat29()
#feladat30() nincs kész
#feladat31()
#feladat32()
#feladat33()
#feladat34()
#feladat35()
#feladat36()
#feladat37()
#feladat38()
#feladat39()
#feladat40()# fele nincs kész







