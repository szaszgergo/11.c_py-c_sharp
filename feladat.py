# a választék és ezközök 
print("Boltunk választéka :")
print("\n Router ár: 5000 ft","\n Switch ár: 13000ft","\n Wifi router ár: 10000ft","\n Számítógép ár: 150000ft","\n Laptop ár: 200000ft","\n Szerver ár: 60000ft","\n Tablet ár: 18000ft","\n Okostelefon ár: 55000ft")

print(" ")
print("Az exit beírásával lehet ki lépni ")
print(" ")
# ------------   
print(" ") 
print("A clear beírásával törölni tudod a vásárlási listád")
print(" ")

ezkozok=[]
ossz=[]  
while True: 
    beker = input("Írd be a kiválasztott termék nevét: ")
    if beker.count("Router"):
        ossz.append(5000)
    if beker.count("Switch"):
        ossz.append(13000)
    if beker.count("Wifi router"):
        ossz.append(10000)
    if beker.count("Számítógép"):
        ossz.append(150000)
    if beker.count("Laptop"):
        ossz.append(200000)
    if beker.count("Szerver"):
        ossz.append(60000)
    if beker.count("Tablet"):
        ossz.append(18000)
    if beker.count("Okostelefon"):
        ossz.append(55000)
    if beker.count("clear"):
        ezkozok.clear()
    if ezkozok == "clear":
        print(" ")
    if str.lower(beker) == "exit" : 
        break 
    ezkozok.append(beker)
    
print("Az ezközeid:")
for item  in ezkozok:
    print("-",item)
    
print("Összesen: ",sum(ossz),"ft")

