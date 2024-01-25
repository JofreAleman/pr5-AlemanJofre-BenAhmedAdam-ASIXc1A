"""
Jofre Aleman Serra i Adam Ben Ahmed Belachi
22/01/24
ASIXc1 MO3-UF1 Pr5
Exercici 1: "SeaTemp", Fer un programa de càlcul de temperatures del mar.
            Calcular per a l’any  2022: temperatura màxima, mínima i mitjana
            Calcular per període 2000 a 2022: temperatura màxima, mínima i mitjana
"""
ANY = 2022
ANYMIN = 2000
ANYMAX = 2022

temperatures = {
    2000: (12.7, 12.4, 12.6, 12.4, 13.0, 13.6, 13.3, 13.6, 13.5, 15.9, 15.3, 14.9),
    2001: (13.8, 13.0, 12.6, 13.6, 13.5, 13.4, 14.0, 14.0, 14.2, 15.3, 16.8, 14.0),
    2002: (13.2, 12.4, 12.9, 13.4, 13.7, 13.6, 14.4, 13.8, 14.3, 14.8, 15.3, 14.2),
    2003: (13.6, 12.2, 12.5, 12.8, 14.7, 13.5, 13.6, 13.7, 14.2, 15.9, 15.3, 15.0),
    2004: (13.5, 12.7, 12.3, 12.6, 13.2, 13.1, 13.3, 13.6, 14.9, 15.3, 15.4, 14.6),
    2005: (13.3, 12.3, 12.3, 12.9, 13.4, 13.3, 13.3, 13.4, 13.9, 15.2, 17.1, 14.4),
    2006: (12.5, 12.3, 12.1, 12.9, 13.1, 13.4, 13.2, 13.2, 14.0, 15.5, 17.3, 15.8),
    2007: (14.3, 13.4, 13.2, 13.4, 14.4, 13.8, 13.8, 13.8, 14.0, 15.5, 15.5, 13.9),
    2008: (13.2, 13.0, 12.9, 12.8, 13.3, 13.6, 13.7, 13.8, 13.9, 14.3, 15.5, 13.8),
    2009: (13.3, 12.5, 12.6, 12.8, 14.2, 13.7, 13.7, 13.8, 14.0, 16.2, 15.9, 14.5),
    2010: (12.6, 11.9, 12.2, 12.8, 13.7, 13.6, 13.5, 13.5, 13.9, 15.6, 15.5, 14.0),
    2011: (13.0, 12.5, 12.5, 13.6, 13.5, 14.0, 14.1, 13.7, 13.8, 15.2, 17.6, 15.9),
    2012: (13.9, 12.4, 12.6, 13.3, 13.7, 13.5, 13.5, 13.7, 13.9, 14.8, 15.8, 13.9),
    2013: (13.2, 12.2, 12.0, 13.1, 13.5, 14.1, 13.7, 13.6, 13.6, 15.3, 15.9, 13.6),
    2014: (13.7, 13.2, 13.6, 13.6, 14.7, 14.2, 13.9, 14.0, 14.5, 15.7, 16.5, 16.0),
    2015: (14.1, 12.6, 12.9, 13.5, 14.3, 13.9, 13.7, 13.8, 14.1, 15.8, 15.8, 15.1),
    2016: (14.1, 13.6, 12.9, 13.5, 14.0, 13.9, 14.0, 14.0, 14.2, 16.3, 16.5, 15.6),
    2017: (13.7, 12.8, 13.4, 13.9, 14.0, 14.0, 13.9, 14.0, 14.0, 14.6, 14.8, 13.3),
    2018: (13.2, 12.7, 12.3, 12.9, 13.8, 13.9, 14.0, 14.1, 14.3, 17.9, 17.7, 15.9),
    2019: (13.9, 12.5, 13.3, 13.4, 14.0, 13.9, 13.8, 13.9, 14.5, 14.9, 15.5, 15.4),
    2020: (14.4, 13.9, 13.6, 13.5, 13.7, 13.9, 13.9, 14.0, 14.3, 14.7, 15.6, 14.6),
    2021: (13.3, 12.9, 13.5, 13.5, 13.7, 13.8, 13.8, 13.8, 14.2, 14.6, 16.8, 14.7),
    2022: (13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14.0, 14.3, 16.0, 15.1)
}
listaMax = []
listaMin = []
listaMit = []
aux = []
def periode (any):
    maxima = 0
    minima = 100
    mitjana = 0

    for i in temperatures[any]:
        if i > maxima:
            maxima = i
        elif i < minima:
            minima = i
        mitjana += i
    mitjana = mitjana / 12
    return(maxima,minima,mitjana)

for j in range(ANYMIN, ANYMAX+1):
    aux = periode(j)
    listaMax.append(aux[0])
    listaMin.append(aux[1])
    listaMit.append(aux[2])

maxTotal = 0
minTotal = 100
mitTotal = 0

for k in listaMax:
    if k > maxTotal:
        maxTotal = k
for l in listaMin:
    if l < minTotal:
        minTotal = l
for m in listaMit:
    mitTotal += m
mitTotal = mitTotal / 22

valors22 = periode(ANY)

print(f'⚪ Any {ANY}:\n     ⚫ Màxima:{valors22[0]}\n     ⚫ Mìnima:{valors22[1]}\n     ⚫ Mitjana:{round(valors22[2], 1)}\n')
print(f'⚪ Període {ANYMIN} a {ANYMAX}:\n     ⚫ Màxima:{maxTotal}\n     ⚫ Mìnima:{minTotal}\n     ⚫ Mitjana:{round(mitTotal, 1)}')