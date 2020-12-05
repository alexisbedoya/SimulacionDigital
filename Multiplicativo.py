
x = int(input("Ingrese la semilla: "))
a= int(input("Ingrese a: "))
m = int(input("Ingrese m: "))
vi=x
aux=0
list=[]
listx1=[]
listx2=[]
listx1.append(x)

for _ in range(m):
    res = ((a * x)) % m
    listx2.append(res)
    list.append(res/(m))
    x = res
    listx1.append(res)
    if(listx1.count(x)>1):
        break


##print(list)
print("Periodo",len(list))

