'''
#import math
#a=math.pi
# kerekítés
print(round(6.1432,3))
print(round(6.1432,2))
#hatványozás
print(pow(2,8)) #pow(alao,kitevő)
#abs aboszolut ertek

#print(abs(-12))
#print(min(1,2,3,5,6,7,8,9,))
#print(max(1,2,3,4,5,6,7,8,9))
#print(a)

from math import *
b=pi
print(b)
#négyzetgyök vonás -sqrt

print(sqrt(4))
#felfelé kerekítés ceil
print(ceil(4.12))
print(floor(5.99))

from math import*
'''
from math import *

#1.f négyzet kerülete területe 4*a  a **2

a= float(input("Kérem az első számot:"))
kerület = 4*a
terület = a**2
print(kerület)
print(terület)





#2.f téglalap kerülete területe k = 2*a+2*b   t = a*b
a = float(input("Kérem a oldalt:"))
b = float(input("Kérem b oldalt:"))
terület = 2*a+2*b
kerület =  a*b
print(terület)
print(kerület)


#3.f kör  kerülete(2*r*PI) területe r**2 *PI

r= float(input("Kérem r oldalt:"))

kerülete = 2*r*pi
területe = r**2*pi
print(kerülete)
print(területe)





#4.f kocka  térfogata V = a**3 felszíne A= 6*a**2

a = float(input("Kérem a oldalt :"))
V = a**3
A = 6*a**2
print(V)
print(A)




#5.f   pitagorasz
# c négyzetgyök a **2 + b**2

a = float(input("Kérem a számot:"))
b = float(input("Kérem b számot:"))
negyzetgyok = a**2+b**2
megoldas = sqrt(negyzetgyok)
print(megoldas)




















