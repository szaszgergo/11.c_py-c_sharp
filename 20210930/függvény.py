def feladat1():
    szam = int(input("Kérek egy egész számot:"))
    if szam%2==0:
        print("A szám páros.")
    else:
        print("Szám páratlan")

def feladat4(szam1):
    if szam1>-30 and szam1<40 :
        print("A megadot szám -30 és 40 között van ")
    else:
        print("Nem esik a megadott intervalumba ")

def feladat5(szam):
    if szam <16 :
        print(szam*10)
    else:
        print(szam/3)



def feladat11():
    a = float(input("Kérem a oldalt"))
    b = float(input("Kérem b oldalt"))
    c = float(input("Kérem c oldalt"))
    if a+b>c and a+c>b and c+b > a:
        print("A háromszög szerkezthető ")
    else:
        print("A háromszög nem szerkezthető")
feladat11()


#feladat5(a)
#a = int(input("Kérek egy számot:"))
#feladat1()
#feladat4(43)

