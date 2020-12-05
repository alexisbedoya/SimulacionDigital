def generarNumeros():
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

