from scipy.stats import chi2
import math
import numpy as np

def operacion(NSA):
  lista = np.array(NSA)
  print("----------------------------varianza--------------------")
  suma=0
  for i in range(len(NSA)):
      suma=suma+NSA[i]
  res=suma/len(NSA)

  print("resultado: ", suma, " ´promedio: ", res)
  var=lista.var()
  print("varianza: ",var)
  desv=math.sqrt(var)
  print("desviacion estandar: ", desv)

  gradoLibertad = 100 -1
  error = 0.025
  x1=chi2.isf(df=gradoLibertad, q=error)
  print(chi2.isf(df=gradoLibertad, q=error))

  gradoLibertad = 100 -1
  error = 0.975
  x2=chi2.isf(df=gradoLibertad, q=error)
  print(x2)

  ls2=x2/(12*(len(NSA)-1))
  
  li2=x1/(12*(len(NSA)-1))
  print("LI: ", li2)
  print("LS: ", ls2 )
  if (li2 <=var and var<=ls2) or (ls2 <=var and var<=li2):
    print("esta dentro del rango")
    



