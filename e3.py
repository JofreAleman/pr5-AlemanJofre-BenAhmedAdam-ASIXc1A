"""
Jofre Aleman Serra i Adam Ben Ahmed Belachi
22/01/24
ASIXc1 MO3-UF1 Pr5
Exercici 3:  Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en
català i afegir la traducció en castellà, anglès i klingon
"""
listainsults = {
    "CAT": ("MOCOS", "CAPSIGRANY", "CALAMAR", "ECTOPLASMA", "CAPOLL", "CAGAMANDURRIES", "BABAU", "CABRA", "CARAGIRAT", "CAP D'ESCROT", "CASCALL", ""),
    "ESP": ("MOCOSO", "ALCAUDON", "CALAMAR", "ECTOPLASMA", "CAPULLO", "CAGAMANDURRIAS", "BOB", "CABRA", "CARAGIRADO", "CABEZA DE ESCROTO", "CASCARRABIAS", "JAVIER EL MEJOR"),
    "ENG": ("SNUFFLY", "SHRIKE", "SQUID", "ECTOPLASM", "COCOON", "DUNDERHEAD", "NINCOMPOOP", "GOAT", "FACE-TURNED", "SCROTUM HEAD", "CURMUDGEON", "JAVIER THE BEST"),
    "KLI": ("Bach", "mup", "Qlp", "Qlb", "ghoS", "Hlq", "Hut'", "runpl'", "tlheD", "paw'", "teq", "Hlvje\"e'nlHwl")
}
idiomes = ["CAT", "ESP", "ENG", "KLI"]
palabra = input()
for i in idiomes:
    if palabra.upper() in listainsults[i] and i != "KLI":
        posicion = idiomes.index(i)
        aux = listainsults[idiomes[posicion]].index(palabra.upper())
        idiomes.pop(idiomes.index(idiomes[posicion]))
    elif palabra in listainsults["KLI"] and i == "KLI":
        posicion = idiomes.index(i)
        aux = listainsults[idiomes[posicion]].index(palabra)
        idiomes.pop(idiomes.index(idiomes[posicion]))
if len(idiomes) == 4:
    for x in idiomes:
        print(listainsults[x][11])
else:
    for x in idiomes:
        print(listainsults[x][aux])