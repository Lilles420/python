#M.Lilles
#17.10.22
#harjutus04

#müük













#juubel
sp = "5.6.2002"
p,k,a = sp.split(".")
vanus = 2022-int(a)
if vanus%5 == 0:
    print ("JAH juubel")

else:
    print("ei")







#matem
a,b =10,20
tehe = input("Vali tehe (+ - * /):")
if tehe=="+":
    vastus = a + b
elif tehe=="-":
    vastus= a - b

else:
    vastus = "n/a"
print(f"{a} {tehe} {b} = {vastus}")


#ruut
a,b = 10,20
if a==b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} teevad kokku ristküliku")