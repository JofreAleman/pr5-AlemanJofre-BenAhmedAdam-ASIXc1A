"""
Jofre Aleman Serra i Adam Ben Ahmed Belachi
22/01/24
ASIXc1 MO3-UF1 Pr5
Exercici 2: Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles
i la mitja del nombre de les posicions senars.
"""
import random

mitjanaPar = 0
mitjanaSen = 0

llista_rdm = [random.randint(1, 50) for i in range(100)]

for j in range(100):
    if j % 2 == 0:
        mitjanaPar += llista_rdm[j]
    else:
        mitjanaSen += llista_rdm[j]

mitjanaPar = mitjanaPar / 50
mitjanaSen = mitjanaSen / 50

print(f'La mitjana dels parells és: {mitjanaPar}\nLa mitjana dels senar és: {mitjanaSen}')