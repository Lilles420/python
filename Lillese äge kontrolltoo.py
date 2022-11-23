#M.Lilles


import random



def tehe():
        for i in range(10):
            t = random.randint(1,11)
            r = random.randint(1,11)
            y = t * r
            print(f"{t}*{r}")
            x = int(input("sisesta vastus: "))
            if y==x:
                print("oige vastus")
            else:
                print("õpi arvutama")
            
            
        
tehe()
   