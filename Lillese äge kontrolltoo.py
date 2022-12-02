#M.Lilles
#25.11.2022

import random

def tehe():
        d=0
        b=0
        q=0
        print(input("mitut tehet soovite :"))
       
       
        for i in range(p):
            t = random.randint(1,11)
            r = random.randint(1,11)
            y = t*r
            q+=1
            print(f"{q}. {t}*{r}")
            x = int(input("sisesta vastus :"))
            if y==x:
                print("oige vastus")
                b+=1
            else:
                print("õpi arvutama")
                d+=1
        print("Oigeid vastuseid",b,"Valesi vastuseid",d,)
           
           

       
tehe()
lp=int(input("Soovite uuesti harjutada?(1=ja, 2=ei): "))
for l in range (1):
    if lp==1:
        print(tehe())
    else:
        print("kumm")
       
def kt():
        d=0
        b=0
        q=0
       
        for i in range(10):
            t = random.randint(1,11)
            r = random.randint(1,11)
            y = t * r
            q+=1
            print(f"{q}. {t}*{r}")
            x = int(input("sisesta vastus :"))
            if y==x:
                print("oige vastus")
                b+=1
            else:
                print("õpi arvutama")
                d+=1
        print("Oigeid vastuseid",b,"Valesi vastuseid",d,)
        for w in range(1):
            if b>=9:
                print("hinne 5")
            elif b>=7:
                print("Hinne 4")
            elif b>=5:
                print("Hinne 3")
            elif b<5:
                print("Hinne 2")
   
ko=int(input("Kas soovite kontrolltööd?(1=ja, 2=ei)"))
for p in range(1):
    if ko==1:
        print(kt())
    else:
        print(tehe())
