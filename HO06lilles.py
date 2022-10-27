#M.LILLES
#27.10.22
#tekstifailiga mässamine

failike=open("s6pru_l6ustaraamatus.txt","r")

reformikad = 0
kesikud = 0
erakonnad = []


for i in failike.readlines():
    ee,pe,er,kyl = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
    with open("julla.txt","a") as julla:
        julla.write(ee+" "+pe+"\n")
        
    
    
        
        

print(f"reformikaid kokku  {reformikad}")
print(f"kesikud kokku  {kesikud}")
print(f"erakonnad kokku {erakonnad}")
failike.close()