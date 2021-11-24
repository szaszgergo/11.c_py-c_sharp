def megtalal(karakterlanc, keresendo):
    if keresendo in karakterlanc:
        return karakterlanc.index(keresendo)
    else:
        return -1

def karakterszam(karakterlanc, megszamolando):
    return karakterlanc.count(megszamolando)

def feladat2():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    karakter=input('Adj meg egy karaktert!')
    # kiírjuk a visszakapott eredményt
    print(megtalal(szoveg, karakter))
    # változóba tesszük
    eredmeny=megtalal(szoveg,karakter)
    if eredmeny==-1:
        print("A megadott karakter nem szerepel a szövegben")
    else:
        print('A megadott karakter a', eredmeny, 'indexű helyen fordul elő először.')

def feladat4():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    karakter=input('Adj meg egy karaktert!')
    print('A megadott szövegben az adott karakter',karakterszam(szoveg, karakter), 'alkalommal fordul elő')

def feladat6():
    szoveg='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusamus, qui?'
    print('A megadott szöveg', karakterszam(szoveg, ' ')+1,'szóból áll.')

def feladat5():
    prefixes='JKLMNOPQ'
    suffixe='ack'
    kacsak=[]
    for item in prefixes:
        kacsak.append(item+suffixe)
    for item in kacsak:
        print(item, end=' ')

#itt kezdődik a főprogram

def nagybetu():
    szo = input("Kérem adjon meg egy betűt ! ")
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]
#így nem lehet más karaktereket írni
    if  szo.islower()==True:
            print("Kis betű ")
    elif szo == abc or abc2 :
        if szo.isupper()==True:
            print("Nagy betű")
    else:
        print(" ")
def feladat10():
    mondat= "Három főbb szempontból a mondat meghatározásai a következők"
    szavak = mondat.split()
    print(szavak)
    for item in szavak:
        print(item,end=" ")
#feladat10()






#nagybetu()
#feladat8()
#feladat10()
#feladat2()
#feladat4()
#feladat5()
#feladat6()