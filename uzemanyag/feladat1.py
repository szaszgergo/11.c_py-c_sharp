mg = "aáeéiíoóöőuúüű"

szamol = 0 
a = input("Kérek egy szöveget:")
for item in a:
    if item.lower() in mg:
        szamol+=1
print(szamol)

vane = False
for sor in a :
    if sor.isupper():
        vane = True


if vane:
    print("Van")
else:
    print("nincs")
