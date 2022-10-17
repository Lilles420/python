#M.Lilles
#11.10.22
#Harjutus03

#tundide ajad
a1,a2 = "8:30","14:15"
h1,m1 = a1.split(":")
minut1 = int(h1)*60+int(m1)
h2,m2 = a2.split(":")
minut2 = int(h2)*60+int(m2)
ajavahe = minut2-minut1
hh = ajavahe//60
mm = ajavahe%60
print (ajavahe)






#email
email = "sdfsdfg@asdfasf.rer"
print("@" in email)

#Vandumine
tekst = input("Ütle kurat küll")
print(tekst.lower().replace("kurat","***"))

print(f"ajavahe on {hh}:{mm}")
