# EXERCICI: Analitzant els tipus de dades d'una xarxa
# Fent servir print() combinat amb type(), mostra a la consola de quin tipus
# és cadascun dels valors següents:

# 1. int: Mostra el tipus del nombre de paquets perduts (per exemple: 0 o -15)
print(type(-15))

# 2. float: Mostra el tipus d'una freqüència de ràdio usant notació científica (per exemple: 2.4e9)
print(type(2.4e9))

# 3. complex: Mostra el tipus de la impedància d'una antena (per exemple: 50 + 10j)
print(type(1+2j))

# 4. str: Mostra el tipus d'un port de xarxa desat per error com a text (per exemple: "8080")
# I mostra també el tipus d'una cadena buida ("")
print(type("8080"))
print(type(""))

# 5. bool: Mostra el tipus d'una comprovació (per exemple, saber si el senyal és superior a un llindar: 85 > 20)
print(type(85>20))

# 6. NoneType: Mostra el tipus d'una variable que encara no ha rebut dades del sensor (None)
print(type(None))