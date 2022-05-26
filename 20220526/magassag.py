from math import *


def teglatest():
    print("1 . feladat Téglatest")
    a= float(input("Kérem a téglatest 1. oldalát:"))
    b= float(input("Kérem a téglatest 2. oldalát:"))
    c= float(input("Kérem a téglatest 3. oldalát:"))

    f = pow(a,2)+ pow(b,2) + pow(c,2)
    x = sqrt(f)
    print("A testátló hossza : ", x)



def mondatt():
    print("3. feladat: Mondat")
    z = input("Kérek egy mondatott: ")
    c = input("Kérek egy karaktert: ")
    mondat = z.split()
    megszamol = z.count(c)
    print("Az adott karakter : ",megszamol," fordul elő a mondatban")

mondatt()

    









