import numpy as np
from scipy.stats import chi2
"""
NSA=[0.7896, 0.0523 ,0.1070, 0.5588, 0.1415,

0.7609, 0.1208, 0.2774, 0.6573, 0.7927,

0.8055, 0.8265 ,0.2945 ,0.2085, 0.4299,

0.5852, 0.9861, 0.3449 ,0.3436 ,0.1154,

0.8990 ,0.5788 ,0.6762 ,0.0501, 0.0012,

0.2827, 0.7306, 0.7012, 0.1828, 0.4996,

0.3862, 0.7691, 0.6833, 0.5517 ,0.1085,

0.7998, 0.4568, 0.2163 ,0.8762, 0.5574,

0.5896 ,0.3322, 0.0319 ,0.6117 ,0.0926,

0.6962 ,0.1703, 0.0548, 0.9151, 0.7626,

0.2993 ,0.3086, 0.8336, 0.5178 ,0.0327,

0.5741, 0.2659, 0.8590 ,0.4331 ,0.3529,

0.2400 ,0.6556 ,0.3851, 0.9083, 0.9419,

0.9365 ,0.8881 ,0.8177, 0.3698, 0.1990,

0.5433, 0.6240 ,0.0913, 0.4168, 0.3395,

0.5824, 0.8585, 0.8875 ,0.3373 ,0.1551,

0.2395 ,0.5356, 0.3338, 0.4938, 0.7510,

0.1996 ,0.6500, 0.7458 ,0.7911, 0.6345,

0.1915, 0.4064, 0.0813, 0.7343, 0.2272,

0.2229, 0.0728, 0.6418 ,0.4425
7 ,0.7210
]

"""
def operacion(NSA):
  print("----------------------Distancia------------")
  """"
  # recorrida por columna
  test = np.array(NSA)
  w=test.reshape(20,5)
  listc=[]
  for index, x in np.ndenumerate(w.T):
      listc.append(x)
      ##print(index, x)
  print(listc)
  NSA=listc
  ## fin"""

  ls = float(0.7)
  li = float(0.3)
  aux=False
  distancia=[]
  cont2=0
  for q in range (len(NSA)):
      if NSA[q] < ls and NSA[q] > li:
          if(aux==True):
              print(cont2)
              distancia.append(cont2)
              cont2=0
          aux=True
      if (NSA[q] > ls or NSA[q] < li ) and aux:
          cont2 = cont2 + 1

  print("distanciaaaa", len(distancia))

  sum0 = 0
  count = [False, False, False, False]
  for w in range(len(distancia)):
      if distancia[w] == 0 and (count[0] == False):
          print("distancia ", distancia[w], "prob", ls - li)
          sum0 = sum0 + ls - li
          count[0] = True
      elif distancia[w] >= 3 and (count[1] == False):
          print("distancia ", distancia[w], "prob", (1 - (ls - li)) ** 3)
          sum0 = sum0 + (1 - (ls - li)) ** 3
          count[1] = True

      elif distancia[w] == 2 and (count[2] == False):
          print("distancia ", distancia[w], "prob", (ls - li) * ((1 - (ls - li)) ** distancia[w]))
          sum0 = sum0 + (ls - li) * ((1 - (ls - li)) ** distancia[w])
          count[2] = True

      elif distancia[w] == 1 and (count[3] == False):
          print("distancia ", distancia[w], "prob", (ls - li) * ((1 - (ls - li)) ** distancia[w]))
          sum0 = sum0 + (ls - li) * ((1 - (ls - li)) ** distancia[w])
          count[3] = True

  print("total prob: ", sum0)

  Fo = []
  cont3, aux = 0, 0
  sum = 0
  for e in range(np.amax(distancia) + 1):
      for t in range(len(distancia)):
          if distancia[t] == e:
              cont3 = cont3 + 1
              sum = sum + 1
      print("Hueco", e, " conteo ", cont3)
      if (e < 3):
          Fo.append(cont3)
      else:
          aux = aux + cont3
      cont3 = 0
  Fo.append(aux)
  print(Fo)
  print("Sumatoria FOI", sum)

  count2 = [False, False, False, False]
  sum1 = 0
  Fei = []
  aux = 0
  for y in range(len(distancia)):
      if distancia[y] == 0 and (count2[0] == False):
          aux = sum * (ls - li)
          print("FEI ", distancia[y], "frecuencia", aux)
          sum1 = sum1 + aux
          Fei.append([distancia[y], aux])
          count2[0] = True

      elif distancia[y] >= 3 and (count2[1] == False):
          aux = sum * ((1 - (ls - li)) ** 3)
          print("FEI ", distancia[y], "frecuencia", aux)
          sum1 = sum1 + aux
          Fei.append([distancia[y], aux])
          count2[1] = True

      elif distancia[y] == 1 and (count2[2] == False):
          aux = sum * (ls - li) * ((1 - (ls - li)) ** distancia[y])
          print("FEI ", distancia[y], "frecuencia", aux)
          sum1 = sum1 + aux
          Fei.append([distancia[y], aux])
          count2[2] = True

      elif distancia[y] == 2 and (count2[3] == False):
          aux = sum * (ls - li) * ((1 - (ls - li)) ** distancia[y])
          print("FEI ", distancia[y], "frecuencia", aux)
          sum1 = sum1 + aux
          Fei.append([distancia[y], aux])
          count2[3] = True
      aux = 0
  # Fei = np.array(Fei)
  Fei = sorted(Fei, key=lambda a_entry: a_entry[0])
  print("frecuencia FEI: ", sum1, "\n", Fei)

  # luego aplicar formula de la linea 72 y 73
  sumatoria = 0

  for s in range(len(Fo)):
      sumatoria = sumatoria + ((Fo[s] - Fei[s][1]) ** 2) / Fei[s][1]
      print(((Fo[s] - Fei[s][1]) ** 2) / Fei[s][1])

  print("sumatoria",sumatoria)

  error = 0.05
  x2=chi2.isf(df=3, q=error)
  if sumatoria<= x2:
      print("Los NSA estan uniformemente distribuidos y son independientes")
      print("Sumatora:", sumatoria, "Chi2:", x2)
  else:
      print("Los NSA no estan uniformemente distribuidos y no son independientes")
      print("Sumatora:", sumatoria, "Chi2:", x2)