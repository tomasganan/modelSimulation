"""
Autor: GAÑAN, Tomas
Ejercicio 2: El juego de la vida
"""

# Importacion de librerias/modulos

import copy
import random
import itertools
import time
import os

UNIX = True

clear = lambda: os.system('clear') if UNIX else os.system('cls')

# Como utilizaremos una clase, a lo largo del desarrollo apareceran
# varios 'self' los cuales nos ayudan a hacer referencia al lugar de
# la memoria en donde se encuentra cada objeto.

class juego_vida(object):

    def __init__(self, filas, colum):
        self.filas = filas
        self.colum = colum
        fila_viva = lambda: [random.randint(0, 1) for n in range(self.colum)]
        self.juego = [fila_viva() for n in range(self.filas)]
        self.viva = 1
        self.muerta = 1

    def __str__(self):
        tabla = ''

        for fila in self.juego:
            for celda in fila:
                tabla += ' @ ' if celda else ' . '
            tabla += '\n'
        tabla += "\n Celda Viva: {0} \n Celda Muerta: {1}".format(self.viva, self.muerta)

        return tabla

    def valuar(self, fila, col):
        espacio = list(set(itertools.permutations([-1, -1, 1, 1, 0], 2)))
        intro = lambda x, y: (x in range(self.filas) and y in range(self.colum))
        total = 0

        for r, c in espacio:
            if intro(r + fila, c + col):
                total += self.juego[r + fila][c + col]

        return total

    def test(self):
        juego_t = copy.deepcopy(self.juego)
        self.viva = 0
        self.muerta = 0

        for r in range(self.filas):
            for c in range(self.colum):
                total = self.valuar(r, c)

                if (total < 2 or total > 3) and juego_t[r][c]:
                    juego_t[r][c] = 0
                    self.muerta += 1
                elif total == 3 and not juego_t[r][c]:
                    juego_t[r][c] = 1
                    self.viva += 1

        self.juego = copy.deepcopy(juego_t)

filas, colum = int(input("Filas: ")), int(input("Columnas: "))
juego = juego_vida(filas, colum)
iteraciones = 0

while juego.viva > 0 or juego.muerta > 0:
    try:
        clear() #Liberacion de memoria
        juego.test() #Ejecucion
        print(juego) 
        time.sleep(1) #Supension de la ejecucion
        iteraciones += 1 #Contador
    except KeyboardInterrupt:
        break
print("\n Total de generaciones: ", iteraciones)
