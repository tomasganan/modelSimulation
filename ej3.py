"""
Autor: GAÑAN, Tomas
Ejercicio 3: Método de Montecarlo
"""

# Importacion de librerias/modulos

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as pyplot
import random
import math

# Sistema

visitas = [33,18,27,36,25,24,30,23,29,38,23,22,19,21,18,28,12,20,22,22,22,34,32,15,14,16,32,17,22,37,11,22,37,15,29,11,36,24,18,19,23,
            12,21,7,30,6,26,31,24,31,25,21,25,21,24,30,29,18,19,16,17,20,24,18,19,43,9,37,32,26,25,18,16,14,23,37,31,34,21,22,26,16,24,
            14,25,32,11,30,30,17,18,36,14,31,24,35,12,19,17,21,28,14,22,39,27,18,33,39,30,32,26,32,19,35,26,20,23,23,23,23,11,20,15,19,
            33,23,40,25,18,16,20,23,20,31,23,20,38,30,19,15,6,23,23,21,17,27,19,23,44,19,23,20,24,22,18,23,21,16,10,23,26,27,29,21,13,32,
            22,27,28,35,24,16,14,25,32,22,32,24,33,32,32,25,24,28,23,16,27,27,10,32,13,29,27,22,17,25,33,46,17,35,17,20,22,30,31,27,21,32,
            18,19,25,26,20,33,19,30,11,34,34,32,24,30,26,28,29,19,21,21,30,26,25,18,22,21,37,24,25,35,18,16,29,25,20,26,28,32,16,15,42,29]

# Calculos Estadisticos Datos Historicos

media = np.mean(visitas)
varianza = np.var(visitas)
desviacion = np.std(visitas)

print("Datos Historicos")
print("Media: %.3f " % media + "| Varianza: %.3f " % varianza + "| Desviacion: %.3f " % desviacion)

# Min/Max

vis_min = min(visitas)
vis_max = max(visitas)

# Distribucion Normal

distr_norm = []
for values in range(vis_min,vis_max):
        den = desviacion * math.sqrt(2*3.14159)
        miem = pow(2.71828,-0.5*pow((values-media)/desviacion,2))
        distr_norm.append(round((1/den)*miem,3)) #Calculo de Distr. Norm manualmente

# Distribucion Acumulada

acum = 0
distr_acum = []

for ac in range(0,40):
        acum = acum + distr_norm[ac]
        distr_acum.append(round(acum,3))

# Generacion de 100 randoms 

list_rand = []
for ran in range(100): # 100 randoms entre 0-1
        list_rand.append(round(random.uniform(0,1),3)) # Funcion round para truncar decimales

comparacion = [item for item in list_rand if item in distr_acum]

if len(comparacion) > 0:
        print('|-----------------------------------------------------|')
        print ('Ambas listas contienen estos elementos: ')
        for item in comparacion: print(item)
        print('|-----------------------------------------------------|')
        print ('Respecto a su posicion, sus visitas estimadas son: ')
        for item in comparacion: print(comparacion.index(item)+6)
        print('|-----------------------------------------------------|')
else:
        print('No existe ningun elemento igual en las listas')

# Calculos Estadisticos Datos Generados

mediaGen = np.mean(list_rand)
varianzaGen = np.var(list_rand)
desviacionGen = np.std(list_rand)

print("Datos Generados")
print("Media: %.3f " % mediaGen + "| Varianza: %.3f " % varianzaGen + "| Desviacion: %.3f " % desviacionGen)

# Distribucion Normal

pyplot.subplot(212)
pyplot.plot(distr_norm, color='blue', linewidth=3)
pyplot.grid(True)
pyplot.title('Distribucion Normal')

# Distribucion Acumulada

pyplot.subplot(211)
pyplot.plot(distr_acum, color='red', linewidth=3)
pyplot.grid(True)
pyplot.title('Distribucion Acumulada')

pyplot.show()














"""

for j in range(10): # 10 intervalos
    for i in range(10): # 10 randoms por intervalo entre 0-1
        list_rand.append(round(random.uniform(0,1),5)) # Funcion round para truncar decimales

        -----


list_rand2 = []
for x in range(vis_min,vis_max+1):
        
        list_rand2.append(np.random.normal(media, desviacion, 1))

Generacion de 40 randoms (6-46) calculandole la normal y metiendolos en una lista
"""



