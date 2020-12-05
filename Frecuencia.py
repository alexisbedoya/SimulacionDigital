"""NSA=[0.03991,0.10461,0.93716,0.16894,0.98953,
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
0.16818, 0.60311, 0.74457, 0.90561, 0.72848]"""
from scipy.stats import chi2
def operacion(NSA):
  print("-----------------------------Frecuencia-------------------------")
  subintervalo=int(input("ingrese el intervalo: "))
  intervalo=[]

  for j in range(subintervalo):
      valor=(j+1)/subintervalo
      intervalo.append(valor)
  print("intervalos: ",intervalo)
  fei=len(NSA)/subintervalo #fei
  print("FEI: ", fei)
  cont1=0
  rest=0
  aux=0

  #foi
  foi=[]
  for z in range(len(intervalo)):
      print("Los valores inferiores a: ", intervalo[z] )
      for k in range (len(NSA)):
          if NSA[k] <= intervalo[z]:
              cont1= cont1+1

      aux=cont1
      cont1=cont1-rest
      print("total:",cont1)
      rest=aux
      foi.append(cont1)
      cont1=0
  
  sumatoria=0
  for s in range(len(intervalo)):
      sumatoria=sumatoria + ((foi[s]-fei)**2)/fei

  print("Sumatoria: ", sumatoria)

  error = 0.05
  x2=chi2.isf(df=subintervalo-1, q=error)

  if sumatoria<= x2:
      print("Los NSA estan uniformemente distribuidos y son independientes")
      print("Sumatora:", sumatoria, "Chi2:", x2)
  else:
      print("Los NSA no estan uniformemente distribuidos y no son independientes")
      print("Sumatora:", sumatoria, "Chi2:", x2)
# EL RESULTADO DE LA SUMATORIA DEBE SER MENOR AL VALOR DEL LA TABLA CHI CUADRADO, VALOR DE LIBERTAD subintervalo-1 Y ERROR 0.05