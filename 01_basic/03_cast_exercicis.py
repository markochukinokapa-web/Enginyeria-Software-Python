###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets = int(input("introduix el nombre de paquets rebuts: "))
total = paquets + 1200
print("El total de paquets és:", total)

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat = float(input("introdueix la velocitat Mbps"))
velocitatMB = velocitat/8
print("la velocitat en MB/s es", velocitatMB)