def feladat1():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    t3=[]
    for i in range(0, len(t1)):
        t3.append(t2[i])
        t3.append(t1[i])
    print('csúnyán:')
    print(t3)
    print('szépen:')
    #for item in t3:
    #    print(item, end=' ')
   # feladat2(t3)

def feladat2(eztirjukki):
    for item in eztirjukki:
        print(item, end=' ')
    print()

def feladat2(eztirjukki, elvalaszto):
    for item in eztirjukki:
        print(item, end=elvalaszto)
    print()

def feladat3(legnagyobbatkeres):
    legnagyobb=max(legnagyobbatkeres)
    print(legnagyobb)


def feladat4(szetvalogat):
    paros=[]
    paratlan=[]
    for item in szetvalogat:
        if item%2==0:
            paros.append(item)
        else:
            paratlan.append(item)
    print('párosok:', end=' ')
    feladat2(paros)
    print('páratlanok:', end=' ')
    feladat2(paratlan)

def feladat5(lista):
    HatnalRovidebb=[]
    HatVagyHosszabb=[]
    for item in lista:
        hossz=len(item)
        if hossz<6:
            HatnalRovidebb.append(item)
        else:
            HatVagyHosszabb.append(item)
    print('Hatnál rövidebb szavak:', end=' ')
    feladat2(HatnalRovidebb)
    print('Hat vagy annál hosszabb szavak:', end=' ')
    feladat2(HatVagyHosszabb)

def feladat6_1(szoveg):
    print('A szöveg hossza', len(szoveg))
    darabok=[]
    for i in range(0, len(szoveg), 5):
        darabok.append(szoveg[i:i+5])
    darabok.reverse()
    feladat2(darabok, '')




# itt kezdődik a főprogram
#lista=['alma', 'körte', 'szilva', 'banán', 'őszibarack','ananász']
#feladat1() #két listát összefűz
#feladat2(lista) #kiírja a lista elemeit
#szamok=[32, 5, 12, 8, 3, 75, 2, 15]
#feladat3(szamok) #legnagyobbat keresi meg
#feladat4(szamok)
#feladat5(lista)
szo='elkelkáposztástalaníthatatlanságoskodásaitokért'
#feladat6_1(szo)
#feladat6_1('legeslegmegszentségteleníttethetetlenebbjeiteknek')


def feladat6_5():
    prefixes = ['ack','ack','ack','ack','ack','ack','ack','ack']
    suffixe = ['J', 'K' ,'L','M','N','O','P','Q']
    nevek=[]
    for i in range(0, len(prefixes)):
        nevek.append(suffixe[i])
        nevek.append(prefixes[i])

        for item in nevek:
            print(item, end='')


#feladat6_5()

def feladat6_6():

    szo=["A"," ma", "is", "működő,", "magyar"]
    print(len(szo))
# hatodik('Ez egy nagyon hosszú mondat sok szóval benne.')

feladat6_6()





















