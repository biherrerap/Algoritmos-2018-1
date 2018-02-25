import random
import matplotlib.pyplot as plt
from time import time
import numpy as np

arreglo = [0 for x in range(100)]
principal = 1

for principal in range(100):

    tiempo_inicial = time()

    matriz1 = np.zeros((principal,principal))
    matriz2 = np.zeros((principal,principal))
    matrizf = np.zeros((principal,principal))


    for i in range(principal):
        for j in range(principal):
            matriz1[i,j]=random.randint(1,2)

    for i in range(principal):
        for j in range(principal):
            matriz2[i,j]=random.randint(1,2)

    for i in range(0,principal):
        for j in range(0,principal):
            for k in range(0,principal):
                matrizf[i,j] += matriz1[i,k]*matriz2[k,j]

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    arreglo[principal] = tiempo_ejecucion

plt.plot(arreglo, color='red', linewidth=3)

plt.show()



"""
arreglo = [0 for x in range(100)]

for principal in range(100):

    tiempo_inicial = time()

    for i in range(principal):
        matriz.append([])
        for j in range(principal):
            x = random.randint(1,2)
            matriz[i].append(x)

    matriz2 = []
    for i in range(principal):
        matriz2.append([])
        for j in range(principal):
            x = random.randint(1,2)
            matriz2[i].append(x)

    matrizf = []
    for i in range(principal):
        matrizf.append([])
        for j in range(principal):
            matrizf[i].append(0)


    for i in range(0,principal):
        for j in range(0,principal):
            for k in range(0,principal):
                matrizf[i][j] += matriz[i][k]*matriz2[k][j]

    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    arreglo[principal] = tiempo_ejecucion

plt.plot(arreglo, color='red', linewidth=3)

plt.show()
"""
