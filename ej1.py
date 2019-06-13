"""
Autor: GAÑAN, Tomas
Ejercicio 1: Sistema no lineal simple: Caso presa-predador
"""

# Importacion de librerias/modulos

import numpy as np
import matplotlib.pyplot as pyplot
from scipy.integrate import odeint

#np.seterr(divide='ignore', invalid='ignore')

# Definicion generica de sistema no lineal

# dx/dt = (alpha x - r x^2) - beta * x * y
# dy/dt = - gamma * y + delta * y * x

def df_dt(x, t, a, b, c, d, r):
    
    dx = a * x[0] - r * x[0]**2 - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    
    return np.array([dx, dy])

# Condiciones iniciales

x0 = 10       #Liebres (Presa)
y0 = 1        #Zorros (Predador)

cond_ini = np.array([x0, y0])

a = 0.08      #Tasa de natalidad de Liebres (Presas)
b = 0.02      #Liebres que mueren por encuentro posible (Exito en la caza del depredador)
c = 0.2       #Tasa de mortalidad de Zorros (Predadores)
d = 0.01      #Zorros por encuentro posible (Exito en la caza)
r = 0.001

tf = 1000      #Tiempo final
nc = 100       #Cantidad de muestras/ciclos

t = np.linspace(0, tf, nc) #La funcion linspace nos devuelve un vector con 100 ciclos espaciados entre 0 y 1000

# Integramos nuestro sistema

sol = odeint(df_dt, cond_ini, t, args=(a, b, c, d, r))

# Diagrama de elongacion

pyplot.subplot(121)
pyplot.plot(t, sol[:, 0], label='Presa', color='red', linewidth=3)
pyplot.plot(t, sol[:, 1], label='Depredador', color='blue', linewidth=3)
pyplot.grid(True)
pyplot.title('Diagrama de Elongacion')
pyplot.ylabel('Presas, Predadores (Poblacion)')
pyplot.xlabel('Tiempo')

# Diagrama de fase 

pyplot.subplot(122)
pyplot.plot(sol[:, 0], sol[:, 1], color='black', linewidth=3,)
pyplot.grid(True)
pyplot.title('Diagrama de Fase')
pyplot.ylabel('Predadores')
pyplot.xlabel('Presas')

pyplot.show() # Nos imprime ambos diagramas