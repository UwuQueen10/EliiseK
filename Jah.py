punktid=0
print("Mis keelt räägitakse maailmas kõige rohkem?")
vastus1=input()
õige1="mandarini"
if vastus1 == õige1:
    print("Õige!")
    punktid +=1
else:
    print("Vale")
print("Kumb on populaarsem Apple või Samsung?")
print("1 Apple")
print("2 Samsung")
vastus2 = input()
õige2="2"
if vastus2 == õige2:
    print("Õige!")
    punktid+=1
else:
    print("Vale")
print("Mis on Viimsi pindala ruutkilomeetrites?")
print("1 2,63 ruutkilomeetrit")
print("2 5,72 ruutkilomeetrit")
print("3 1,62 ruutkilomeetrit")
vastus3 = input()
õige3 = "3"
if vastus3 == õige3:
    print("Õige!")
    punktid +=1
else:
    print("Vale")
    
if punktid ==3:
    print("owo tubli, kõik oli õige")
else:
    print("proovi uuesti")
