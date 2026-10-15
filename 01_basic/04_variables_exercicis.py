###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Chuko"
ubi_encaminador = "Sant Quirze"
num_ports = 4
ences: bool = True

print(f"nom:{nom_encaminador}\n ubicació:{ubi_encaminador}\n nombre de ports:{num_ports}\n esta ences?:{ences}\n")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_consumits = int(input("introdueix els GB consumits: "))
gb_inclosos = 100
gb_restants = gb_inclosos-gb_consumits
print(f"GB restants{gb_restants}")
gb_consumits = int(input("introdueix un nou valor de GB consumits:"))
gb_restants = gb_inclosos-gb_consumits
print(f"GB restants{gb_restants}")
