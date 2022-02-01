from random import *
def feladat1():
    f = open("novakvo.txt" ,"w")
    for i in range(1,11):
        if i == 10:
           f.write(str(i))
        else:
            f.write(str(i)+"*")
        
    f.close()



#feladat1()

# 2 3 4 5 
def feladat2():
    f = open("negyzetszamok.txt" ,"w")
    for i in range(1,16):
            f.write(str(i*i)+" ")
    f.close()

#feladat2()


def feladat8():
    f= open("nemek.txt","w",encoding="utf8")
    for i in range(1,101):
        if randint(1,2)==1:
            f.write("F"+"*")
        else:
            f.write("N")
    f.close()
#feladat8()


def feladat3():
    f = open("veletlenek.txt" ,"w")
    for i in range(1,11):
        a = randint(100,200)
        f.write(str(a)+" ")

        
    f.close()
#feladat3()

def feladat4():
    f = open("matek.txt" ,"w")
    for i in range(1,16):
        a = randint(1,5)
        f.write(str(a)+" ")

        
    f.close()

#feladat4()



def feladat5():
    f = open("cipomeret.txt" ,"w")
    for i in range(1,29):
        a = randint(34,45)
        f.write(str(a)+" ")
    f.close
#feladat5()

def feladat6():

    f = open("parosok.txt" ,"w")
    for i in range(1,21):
        if i%2==0:
            f.write(str(i)+" ")
    f.close
#feladat6()

def feladat7():
    
    f = open("bitek.txt" ,"w")
    for i in range(1,101):
        if randint(0,1)==1:
            f.write(str(1)+" ")
        else:
            f.write(str(0)+" ")
    f.close

#feladat7()

def feladat9():
    f = open("penzdobas.txt" ,"w")
    for i in range(1,501):
        if randint(0,1)==1:
            f.write(str("fej")+" ")
        else:
            f.write(str("iras")+" ")
    f.close



#feladat9()



def feladat10():
    