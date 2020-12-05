def generarMC():
  while True:
      try:
          seed=int(input("Ingrese la semilla: "))
          if len(str(seed)) > 3:
              break
      except ValueError:
          print("OPCIÓN INVÁLIDA!!....")

  while True:
      try:
          num=int(input("Cuántos números aleatorios desea?: "))
          break
      except ValueError:
          print("OPCIÓN INVÁLIDA!!....")

  list=[]
  for _ in range(num):
      x1=int(seed)**2
      if(len(str(x1))==8):
          list.append(str(x1)[2:-2])
      else:
          aux=8-len(str(x1))
          list.append(("0"*aux+str(x1))[2:-2])
      seed=list[-1]

  print("\n | Números aleatorios generados: |")
  print([int(i)/10000 for i in list])
  return [int(i)/10000 for i in list]
  
def generarMixto():
  x = int(input("Ingrese la semilla: "))
  a= int(input("Ingrese a: "))
  c = int(input("Ingrese c: "))
  m = int(input("Ingrese m: "))

  list=[]
  listx1=[]
  listx2=[]
  listx1.append(x)

  for _ in range(m):
      res=((a*x)+c)%m
      #res = ((a * x)) % m
      listx2.append(res)
      list.append(res/(m))
      x = res
      listx1.append(res)
      if(listx1.count(x)>1):
          break
  return list

def generarMultiplicativo():
  x = int(input("Ingrese la semilla: "))
  a= int(input("Ingrese a: "))
  m = int(input("Ingrese m: "))
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
  return list