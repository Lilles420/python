#M.Lilles
#25.10.22
#harjutus05


#Õpilaste nimede muutmine
"""
jrk  = 1
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk+=1
miuke = int(input("keda muudad? "))-1
Muuda = input("lisa uus mees: ")
del opilased[miuke]
opilased.insert(miuke, Muuda)
print(opilased)
"""

opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
puh_opilased = []
for opilane in opilased:
    if opilane not in puh_opilased:
        puh_opilased.append(opilane)
        
print(puh_opilased)

print()












#vanused








    


    


"""
#nimede lisamine loendisse
print("-------------")
nimed = []
for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
print(f"Viimane nimi: {nimed[-1]}")
nimed.sort()
print(nimed)
"""














