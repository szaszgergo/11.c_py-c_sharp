print(f"3.feladat: Mondat")

a = input("Kérek egy mondatot:")
b = input("Kérek egy karaktert:")
 
def megszamol():
    c = a.count(b)
    print(f" \t A mondat {c} helyen tartalmaz {b} karaktert.")
megszamol()


def leghoszabbkeres():
    print(f"7.feladat:") 
    leghoszabb = ''
    for szo in a.split(' '):
        if len(szo) > len(leghoszabb):
              leghoszabb = szo
    print(f"\t A leghosszabb szó : {leghoszabb}")
  


leghoszabbkeres()    