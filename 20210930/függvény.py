def feladat1():
    szam = float(input("Kérek egy egész számot:"))
    if szam%2==0:
        print("A szám páros.")
    else:
        print("Szám páratlan")

def feladat4(szam1):
    if szam1>-30 and szam1<40 :
        print("A megadot szám -30 és 40 között van ")
    else:
        print("Nem esik a megadott intervallumba ")

def feladat5(szam):
    if szam <16 :
        print(szam*10)
    else:
        print(szam/3)
#a = int(input("Kérek egy számot:"))


def feladat11():
    a = float(input("Kérem a oldalt"))
    b = float(input("Kérem b oldalt"))
    c = float(input("Kérem c oldalt"))
    if a+b>c and a+c>b and c+b > a:
        print("A háromszög szerkezthető ")
    else:
        print("A háromszög nem szerkezthető")




def feladat2():
    a=float(input("Kérem a számot:"))
    if a>0:
        print("A szám pizitív")
    elif a == 0:
        print("A szám 0 így nem potitív se negatív")
    else:
        print("A szám negatív")


def feladat3():
    homerseklet=float(input("Kérem a hőmérségletet:"))
    if homerseklet>0:
        print("A nincs fagy oda kint.")
    else:
        print("Kint fagy van .")




def feladat6(szam1):
    if szam1>9 and szam1<19:
        print("A megadott szám tízesekbe tartozik ")
    elif szam1>19 and szam1<29:
        print("A megadott szám húszasokba tartozik ")
    elif szam1>29 and szam1<39:
        print("A megadott szám harminzasokba tartozik ")
    elif szam1>39 and szam1<49:
        print("A megadott szám negyvenesekbe tartozik ")

#a = float(input("Kérem a számot"))


def feladat7():
    a = int(input("Kérem a számot"))

    if a>12 and a<25 and a%2!=0 :
        print("Páratlan")
    elif a >12 and a<25:
        if a%2==0 :
            print("A szám páros " )
    elif a<12:
        print("")
def feladat8():
    a = float(input("Kérem a hőmérségletet"))
    if a>0 and a<100:
        print("Folyékony")
    elif a<0 :
        print("Szilárd")
    elif  a>100:
        print("Légnemű")


def feladat9():

    a = float(input("Kérem a számot"))

    if a%4==0 and a%3==0 and a%9==0:
        print("A szám mind hárommal osztható")
    elif a%3==0 and a%9==0:
        print("A szám 3-al és 9-el osztható")
    elif a%4==0 and a%3==0 :
        print("A szám  osztható 4-el és 3-al")
    elif a%4==0 :
        print("A szám  osztható 4-el")
    elif  a%3==0 :
        print("A szám  osztható 3-al" )
    else:
        print("a szám nem osztható 3-al ,4-el és 9-el se")

def feladat10():
    ev = float(input("add meg a évet "))
    if ev%4==0:
        if ev%100!=0:
            print("nem évszázados szökőév")
        elif ev%100==0:
            if ev%400!=0:
                print("nem szökőév")
            elif ev%400==0:
                print("évszázados szökőév")
    elif ev%4!=0:
        print("nem szökőév")

def feladat10_2():
    a = float(input("Add meg a évet "))
    if a%4 == 0 :
        print("szökőév")
    elif a%4!=0:
        print("nem szökőév")
    else:
        print("")



#feladat10_2()
#feladat1()
#feladat2()
#feladat3()
#feladat4(43)
#feladat5(a)
#feladat6(a)
#feladat7()
#feladat8()
#feladat9()
feladat10()
#feladat11()