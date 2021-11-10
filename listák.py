from random import *

def listaAlapok():
    # lista létrehozása
    alapok=[]
    for i in range(10):
        alapok.append(randint(1,50))
    alapok.append('alma') # elem hozzáadása
    alapok.append('szilva') # elem hozzáadása
    print(alapok)
    # lista kiírása szépen
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok[4]) # 4-es indexű elem (sorban az ötödik)
    print(len(alapok)) # lista elemszáma
    alapok.insert(4,"körte") #elem beszúrása adott helyre
    print(alapok.index('körte')) # elem indexe
    #print(alapok.index(55)) # hibaüzenettel áll meg, ha nincs benne
    alapok.remove('körte') # elem törlése
    alapok.pop() # utolsó törlése
    del alapok[-1] # utolsó törlése
    del alapok[1] # 1-es indexű törlése
    #alapok.clear() # lista elemeket törli, lista megmarad
    #del alapok # listát törli
    alapok.reverse() # sorrendet megfordítja
    alapok.sort() # növekvő sorrend
    alapok.reverse()
    print()
    print(alapok[5:]) # 5-ös indextől a végéig
    print(alapok[:4]) # elejétől az adott indexűig(ezt már nem)
    print(alapok[-1]) # utolsó
    print(alapok[-2]) # utolsó előtti
    print(alapok[-2:]) # utolsó kettő
    print(alapok[3:5])
    alapok[6]='narancs'
    print(alapok[6])
    print()
    for item in alapok:
        print(item, end=" ")
    print()

def feladat1():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    paratlandb=0
    for item in szamok:
        if item%2==1:
            paratlandb+=1 # paratlandb=paratlandb+1
    print('A páratlanok száma',paratlandb)

def feladat2():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    osszeg=0
    for item in szamok:
        if item%2==0:
            osszeg+=item
    print("A párosok összege", osszeg)

def feladat3():
    elemszam=int(input("Add meg az elemek számát!"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok) # ellenőrzés miatt
    for i in range(len(szamok)):
        if szamok[i]%2==0:
            print(i+1, '\t', szamok[i])


def feladat5():
    lista = []
    elem = int(input('Add meg az elemek számát: '))
    for i in range(elem):
        lista.append(randint(1, 100))
        print(lista)
    szam = int(input('Adj meg egy egész számot: '))
    i = 0
    for item in lista:
        if item == szam:
            i =i+ 1
    print('A szám', str(i)+ 'szer szerepel a listában')

def feladat6():
    lista = ['Ferenc', 'Szilárd', 'Viktor', 'Klára', 'Péter', 'Gergő', 'Ferenc', 'Szilárd', 'György', 'Judit']
    szam = int(input("Add meg az osztály létszámát: "))
    deflista = lista[0:szam]
    print(deflista)
    nev = str(input("Addj meg egy nevet: "))
    i = 0
    for item in deflista:
        if item == nev:
            i += 1
    print(i, nev, "nevű ember jár az osztályba.")






feladat6()
#feladat5()
#listaAlapok()
#feladat1()
#feladat2()
#feladat3()



















