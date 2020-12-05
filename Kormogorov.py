
import numpy as np
import math
'''
NSA=[0.03991,0.10461,0.93716,0.16894,0.98953,
0.38555, 0.95554, 0.32886, 0.59780, 0.09958,
0.17546, 0.73704, 0.92052, 0.46215, 0.15917,
0.32643, 0.52861, 0.95819, 0.06831, 0.19640,
0.69572, 0.68777, 0.39510, 0.35905, 0.85244,
0.24122, 0.66519, 0.27699, 0.06494, 0.03152,
0.61196, 0.30231, 0.92962, 0.61773, 0.22109,
0.30532, 0.21704, 0.10274, 0.12202, 0.94205,
0.03788, 0.97599, 0.75867, 0.20717, 0.82037,
0.48228, 0.63379, 0.85783, 0.47619, 0.87481,
0.88618, 0.19161, 0.41290, 0.63312, 0.71857,
0.71299, 0.23853, 0.05870, 0.01119, 0.92784,
0.27954, 0.58909, 0.82444, 0.99005, 0.04921,
0.80863, 0.00514, 0.20247, 0.81759, 0.45197,
0.33564, 0.60780, 0.48460, 0.85558, 0.15191,
0.90899, 0.75754, 0.60833, 0.25983, 0.01291,
0.78038, 0.70267, 0.43529, 0.06318, 0.38384,
0.55986, 0.66485, 0.88722, 0.56736, 0.66164,
0.87539, 0.08823, 0.94813, 0.31900, 0.54155,
0.16818, 0.60311, 0.74457, 0.90561, 0.72848]'''




def operacion(NSA):
  print("----------------------Kormogorov--------------------")
  Fo=np.array(NSA);
  Fo.sort();
  #print(Fo)

  FN=[]
  for i in range(len(NSA)):
    div=(i+1)/(len(NSA))
    FN.append(div)
    #print(FN[i])

  Dnmas= np.max(abs(FN-Fo))
  print("Valor",Dnmas)

  aux=[]

  for j in range (len(NSA)):
    j+1
    aux.append(abs(Fo[j]-((j-1)/len(NSA))))
    #print("datos: ", aux[j])


  Dnmenos= max(aux)
  print("aux", Dnmenos)

  Dn=max(Dnmas,Dnmenos)
  print("DN: ", Dn)

  tabla=0
  #tabla = 0.134 if len(NSA)==100 else (1.36/math.sqrt(len(NSA)) if len(NSA)>100 else 1)
  if len(NSA)==100:
    
    tabla=0.134
  elif len(NSA)>100:
    tabla=1.36/math.sqrt(len(NSA))



  if Dn < tabla:
    print("Proviene de una distribución uniforme y son aleatorias")
    print("DN:",Dn,"Tabla:", tabla)
  else:
    print("No proviene de una distribución uniforme y no son aleatorias")
    print("DN:",Dn,"Tabla:", tabla)

  