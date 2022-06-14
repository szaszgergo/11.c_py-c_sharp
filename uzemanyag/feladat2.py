from random import * 
randomok = []
for i in range(50):
    a = randint(10,100)
    randomok.append(a)


def primek(szam):
    osztok =0
    for i in range(1,szam+1):
        if szam%i ==0:
            osztok+=1
    if osztok ==2:
        return True
    else:
        return False

primszamok=[]
oszszamok=[]

def eldont(randomok):
    for szam in randomok:
        if primek(szam):
            primszamok.append(szam)
        else:
            oszszamok.append(szam)
eldont(randomok)
print(primszamok)
print(oszszamok)