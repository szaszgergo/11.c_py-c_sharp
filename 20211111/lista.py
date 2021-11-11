def feladat1():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus',
          'Szeptember', 'Október', 'November', 'December']
    t3 = []
    for i in range(0, len(t1)):
        t3.append(t2[i])
        t3.append(t1[i])
    print(t3)

    for item in t3:
        print(item, end=" ")


def feladat2(a):
    for item in a:
        print(item, end=" ")
    print()


def feladat3(legnagyobbatkeres):
    legnagyobb = max(legnagyobbatkeres)
    print(legnagyobb)


lista = ["alma", "körte", "szilva", "banán", "barack", "ananász"]

szamok = [32, 5, 12, 8, 3, 75, 2, 15]

feladat3(szamok)


def feladat4(szetvalogat):
    paros=[]
    paratlan=[]
    for item in szetvalogat:
        if item%2==0:
            paros.append(item)
        else:
            paratlan.append(item)
    print("párosok:",end=" ")
    feladat2(paros)
    print("páratlanok:",end=" ")
    feladat2(paratlan)
    '''
def feladat5(lista):
    hatnalrövidebb=[]
    hatnalnagyobb=[]

    for item in lista:
        hossz=len()
    if hossz<6:
        hatnalrövidebb.append(item)
    else:
        hatnalnagyobb.append(item)
print("Hatnál hosszabb szavak :",end=" ")
#(hatnalnagyobb)
print("Hatnál rövidebb szavak :",end=" ")
#feladat2(hatnalrövidebb)
'''


def feladat6(szoveg):

    print("A szóveg hossza",len(szoveg))
    darabok=[]
    for i in range(0,len(szoveg),5):
            darabok.append(szoveg[i:i+5])
    darabok.reverse()
    feladat2(darabok,"")


def feladat2(a,elvalaszto):
    for item in a:
        print(item, end=elvalaszto)
    print()


#5 HF
#6HF











szo=("eltöredezettségmentesítőtlenítetthetetlenségtelenítőtlenkedhetnétek")

feladat6(szo)
#feladat5(lista)
#feladat4(szamok)
# feladat2(lista)
# feladat1()




































