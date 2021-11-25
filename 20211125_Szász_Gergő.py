'''
1. Írj programot, amely a 20-tól 40-ig terjedő számok négyzeteit egy listába teszi!
'''
from random import *
def feladat1():
    a = []
    for i in range(20,40+1):
        #print(i,end=" ")
        a.append(i*i)
    print(a)
'''
2. Adott a következő szöveg:
"Az ősz annyira szereti a naplementéket, hogy minden egyes levélre egyet fest."
Írj programot
amely megszámolja, hogy
:
a.) hány karakterből áll a mondat
b.) hány szóból áll, a szavakat listába is tárold el

c.) hány "e" betű van benne
d.)
hány magánhangzó van benne (tipp: a magánhangzókat tedd egy sztringbe,
és azt vizsgáld, hogy az adott karakter benne van-e a sztringben)
'''

def feladat2():
    szoveg= "Az ősz annyira szereti a naplementéket, hogy minden egyes levélre egyet fest."
    print("A szöveg",len(szoveg),"karakterből áll össze.") #a

    szoveg_szo=szoveg.split()
    print(len(szoveg_szo)," szóból áll a mondat. ")        #b

    e = 0                                                  #c
    for i in szoveg:
        if i == 'e':
            e =e+ 1
    print(e,"e karakter van a mondatban . ")

    mh = "aáeéoóöőüűuúií"       #d

    mhszama = 0
    for i in szoveg:
        if i.lower() in mh:
            mhszama =mhszama+  1
    print(mhszama,"magánhangzó van a mondatban." )


'''
3. Generálj 15 véletlenszámot 1 és 100 között egy listába, majd adj választ az alábbiakra!
a.) Mennyi a számok összege?
b.) Mennyi a számok átlaga?
c.) Mennyi a számok terjedelme (A legnagyobb és legkisebb számok különbsége)?
d.) Hány hárommal osztható szám van közöttük? Melyek ezek?
'''
def feladat3():
    a= []
    for i in range(10):
        a.append(randint(0,100))
    #print(a) #ell
    print(sum(a), "a listában lévő számok összege") #a
    print(sum(a)/15, 'a számok átlaga')       #b
   # print(sum(a)//15, 'a számok átlaga')     #b.2
    print("A számok terjedel =",max(a)-min(a)) #c


#d
    oszt=[]
    for i in a:
        if i%3==0:
            oszt.append(i)
    print(len(oszt),"szám osztható 3-al a listából,","hárromal osztható számok a random lisából:",oszt,)   #d






feladat1()
feladat2()
feladat3()
