def LétezikE(filenév):
    try:
        f=open(filenév,"r")
        f.close()
        return 1
    except:
            print("A fájl nem létezik")
            return 0




def primek12ig():
    filename="primek12ig.txt"
    if LétezikE(filename):
        f=open(filename , "r")
       
        beolvas=f.readlines()
        primek=[]

        f.close()
       

        for i in beolvas:
            primek.append(i.strip("\n"))
            
        for i in primek:
            print(i)
#primek12ig()


def nemek():
    filename="nemek.txt"
    if LétezikE(filename):
        f=open(filename , "r")
        beolvas=f.readline()
        f.close()
        print(beolvas)
        nemek2 = []
        nemek2 = beolvas.strip(",").split(",")
        print("Az elemek száma:",len(nemek2))
        ferfi = nemek2.count("f")
        no = nemek2.count("n")  # len(nemek2)-ferfi
        print("A férfiak száma:", ferfi)

#nemek()



def cipomeret():
    filename="cipomeret.txt"
    if LétezikE(filename):
        f = open(filename,"r")
        cipomeretek = []
        beolvas=f.readline()
        cipomeretek.append(beolvas)
        f.close()
        print(beolvas)
        meret1 = beolvas.count("36")
        print(meret1,"36-os cipő van az osztályban.")
        
            
cipomeret()

        