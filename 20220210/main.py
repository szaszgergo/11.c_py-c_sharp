from random import *
def feladat16():
    f = open("sorozat.txt","w")
    a = 22 
    for i in range(1,10+1):
        f.write(str(a)+" ")
        a+=4
    f.close

# itt kezdődik a fő program 

feladat16()

def feladat17():
    f=open("dobokocka.txt","w")
    for i in range(1,51):
        a = randint(1,6)
        f.write(str(a)+" ")
    f.close()
feladat17()

def feladat18():
    mondatvegi= ".!?"
    f = open("mondat.txt","w")
    while True:
        szo= input("Kérek egy szót a  mondat!")
        if szo[-1] in mondatvegi:
            f.write(szo)
            break
        else:
            f.write(szo+" ")
    f.close()

#feladat18()



def feladat19():
    generaltak = []
    f= open("kicsik.txt","w")
    for i in range(1,11):
        a = randint(1,50)
        if a in generaltak:
            i=i-1
            print("valami")
        else:
            generaltak.append(a)
            f.write(str(a)+" ")
    f.close()


    f=open("kicsik2.txt","w" )
    generaltak.clear()
    while len(generaltak) !=10:
        a = randint(1,50)
        if a not in  generaltak:
            generaltak.append(a)
            f.write(str(a)+" ")
        
    f.close()

feladat19()
def feladat20():
    f = open("orszagok.txt","w", encoding="utf8")
    while True:
        orszagok=input("Kérek egy országot!( magyarország) az exit ")
        if orszagok=="magyarország":
            f.write(str(orszagok)+"*")
            break
        else:
            f.write(str(orszagok)+"*")
    f.close()
#feladat20()

def feladat21():
    f= open("toto.txt","w",encoding="utf8")
    for i in range(1,14):
        a = randint(0,2)
        if a==1:
            f.write("1"+",")
        elif a==0:
            f.write("x"+",")
        elif a==2:
            f.write("2"+",")
    f.close()
#feladat21()


def feladat22():
    f = open("tengerszint.txt","w")
    f.close()


def feladat27():
    f = open("vercsoportok.txt" , "w")
    for i in range(1,100):
        a = randint(0,3)
        b = randint(0,1)
        if a == 0 and b == 0:
            f.write("A +"+",")
        elif a == 0 and b == 1 :
            f.write("A -"+",")
        elif a == 1 and b == 0 :
            f.write("B +" +",")
        elif a == 1 and  b == 1 :
            f.write("B -" + " ,")
        elif a == 2 and b == 0 :
            f.write("AB +" +",")
        elif a == 2 and  b == 1 :
            f.write("AB -" + " ,")
        elif a == 3 and b == 0 :
            f.write("0 +" +",")
        elif a == 3 and  b == 1 :
            f.write("0 -" + " ,")
    f.close()

    f = open("vercsoportok2.txt","w")
    vercsoportok = ["A","B","AB","0","+","-"]
    for i in range(1,100):
        a = randint(0,3)
        b = randint(4,5)
        f.write(vercsoportok[a]+" " +vercsoportok[b])
        f.write("\n")
    f.close()
feladat27()



def feladat26():
    f = open("fogyasztas.txt","w")
    
    for i in range(1,12):
        a = randint(480,540)
        b = randint(367,398) /10
        f.write("km"+" "+str(a)+" liter"+" "+str(b))
        f.write("\n")
    f.close()
feladat26()

def feladat28():
    f= open("kopapirollo.txt","w", encoding="utf8")
    lista = ["Kő","Papír","Olló"]
    for i in range(1,10+1):
        tomi=randint(0,2)
        zoli=randint(0,2)
        f.write(lista[tomi]+" "+ lista[zoli])
        f.write("\n")


    f.close()

feladat28()


def feladat29():
    peti_dobasok=[]
    peti = randint(1,7)
    mezo = 0 
    while peti  < 100 and mezo <100:
        mezo += peti
        peti_dobasok.append(mezo)
    print(peti_dobasok)

def feladat29():
    f = open("tarsas.txt","w")
    peti_lista = []
    klari_lista = []
    zoli_lista = []
    while True:
        for i in range(1,100):
            peti = randint(1,6)
            peti_lista.append(peti)
            klari = randint(1,6) 
            klari_lista.append(klari)
            zoli = randint(1,6)
            zoli_lista.append(zoli)
        f.write(str(peti)+" "+ str(klari)+" "+ str(zoli))
        f.write("\n")
        
    f.close()
feladat29()


