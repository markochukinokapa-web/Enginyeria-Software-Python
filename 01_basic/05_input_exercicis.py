###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom,xarxa = input("com et dius i com es diu la xarxa que estas instal·lant?\n").split()
print(f"em dic {nom} i la xarxa es diu {xarxa}\n")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
km,Gbps = input("com de llarga es la la fibra en quilòmetres i quina es la seva velocitat?\n").split()
km = int(km)
Gbps = int(Gbps)
temps = 8/Gbps
print(f"es tardara {temps}s per a transmetre 1 GB de dades\n")
# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hora,preu = input("quantes hores has fet de feina i quin es el preu per hora\n").split()
hora = int(hora)
preu = int(preu)
cost = hora * preu
print(f"el cost total es {cost}")