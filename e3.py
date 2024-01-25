"""
Jofre Aleman Serra i Adam Ben Ahmed Belachi
22/01/24
ASIXc1 MO3-UF1 Pr5
Exercici 3:  Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en
català i afegir la traducció en castellà, anglès i klingon
"""
import deep_translator

traductor = deep_translator.GoogleTranslator(source='es', target='en')
resultado = traductor.translate("La educación es el arma más poderosa para cambiar al mundo")
print(resultado)

