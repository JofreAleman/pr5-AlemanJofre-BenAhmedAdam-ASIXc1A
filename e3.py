"""
Jofre Aleman Serra i Adam Ben Ahmed Belachi
22/01/24
ASIXc1 MO3-UF1 Pr5
Exercici 3:  Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en
català i afegir la traducció en castellà, anglès i klingon
"""
from translate import Translator
import langdetect

listainsults = {
    "CAT": ("MOCOS", "CAPSIGRANY", "CALAMAR", "CARAMULL", "CAPOLL", "CAGAMANDURRIES", "CARRINCLÓ", "CABRA", "CARAGIRAT", "COLLONS", "CASCALL", "CAGALERA", "CACAFUTI"),
    "ESP": ("Mocoso", "Cabezon", "Calamar", "Caramull", "Capullo", "Cagamandurrias", "Carrinchón", "Cabra", "Caragirado", "Collons", "Cascarrabias", "Cagalera", "Cacafuti"),
    "ENG": ("Snuffly", "Big", "Squid", "Blockhead", "Jerk", "Dunderhead", "Nincompoop", "Goat", "Blockhead", "Balls", "Fool", "Loon", "Noodle"),
    "KLI": ("Bach", "p", "Q'Pla", "QI'yaH", "nIQ", "Hurgh", "Qapla'", "Saj", "QI'yaH", "bIQ", "tIQ", "lo'", "ghIl")
}
palabra = input()
if palabra.upper() in listainsults["CAT"]:
    aux = listainsults["CAT"].index(palabra.upper())
    print(listainsults["ESP"][aux])
    print(listainsults["ENG"][aux])
    print(listainsults["KLI"][aux])
else:
    aux2 = langdetect.detect_langs(palabra)[0].split(":")
    traduccion = Translator(to_lang="es", from_lang=aux2[0])
    otrabyna = traduccion.translate(palabra)
    print(otrabyna)