import numpy as np
from scipy.stats import chi2

def operacion(NSA):
  
  ## recorrida por columna
  '''test = np.array(NSA)
  w=test.reshape(20,5)
  listc=[]
  for index, x in np.ndenumerate(w.T):
      listc.append(x)
      ##print(index, x)
  print(listc)
  NSA=listc
  ## fin'''
  

  lista2 =[]
  for i in range(len(NSA)-1):
    x,y = NSA[i],NSA[i+1]
    lista2.append([x,y])

  k = 1/int(input("Ingrese el intervalo: "))
  intervalos = np.arange(k,1+k,k)

  cont=0
  #lista2 numpy array como tal no es una matriz tiene la siguiente forma 
  '''''
  [1,2
  3,4]
  matrixCom[0] = error  
  pero en numpy
  array numpy = [[1,2],[3,4]]
  lista2[0] = [1,2]
  lista2[1] = [3,4]
  lista2[0][0] = 1
  lista2[0][1] = 2
  lista2[1][1] = 4
  99 parejas 
  cont porque el cont debe guardar el valor total de cada cuadrante
  
  '''''


  contador=[]
  for i in range (len(intervalos)):
    for j in range(len(intervalos)):
      for z in range(len(lista2)):
        if lista2[z][0] <= intervalos[i] and lista2[z][1] <= intervalos[j] and lista2[z][0] > (intervalos[i]-k) and lista2[z][1] > (intervalos[j]-k):
          cont=cont+1
        # print(lista2[z])
      print("intervalo x", intervalos[i], "intervalo y", intervalos[j])
      print(cont)
      contador.append(cont)
      print("--------------------------------------------------")
      cont=0
      
  """ 
  #gaylex
  def contadorrango(x, y, intervaloc):
      x = np.floor(x/intervaloc).astype(int) 
      y = np.floor(y/intervaloc).astype(int) 
      counts = np.zeros(shape=(max(x)+1, max(y)+1), dtype=int)
      for i in range(x.shape[0]):
          row = max(y) - y[i]
          col = x[i]
          counts[row, col] += 1
      return counts
  lista2 = np.array(lista2)
  x = np.array(lista2[:,0])
  y = np.array(lista2[:,1])
  print(contadorrango(x,y,0.2))
  """


  FEi=len(lista2)/(len(intervalos)**2)
  print("Fei:", FEi)
  #contador2=[i for i in contador if contador.count(i)<2]
  contador2=[]
  for item in contador:
      if item not in contador2:
          contador2.append(item)
  print('contador',contador2)




  cont2=0
  suma=0
  for j in range(len(contador2)):
    for m in range(len(contador)):
      if contador2[j]==contador[m]:
        cont2=cont2+1
    suma=suma+(((contador2[j]-FEi)**2)*cont2)
    cont2=0

    
  sumatoria=suma*((len(intervalos)**2)/len(lista2))
  gradoLibertad = (len(intervalos)**2)-1
  error = 0.05
  x1=chi2.isf(df=gradoLibertad, q=error)
  print("X1:",x1)
  print("sumatoria: ", sumatoria)


  if sumatoria <= x1:
    print("Los numeros pseudoaleatorios generados cumplen con las condiciones de aleatoriedad, uniformidad e independencia  ")
  else:
    print("Los numeros pseudoaleatorios generados no cumplen con las condiciones de aleatoriedad, uniformidad e independencia  ")