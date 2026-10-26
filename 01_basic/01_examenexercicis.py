# EXERCICI: Formatatge de Registre de Sistema
# Escriu el codi necessari sota de cada pas per complir amb les restriccions basades en els apunts:

# 1. Imprimeix el text inicial 'Iniciant diagnòstic...' utilitzant cometes simples o dobles tradicionals.
print("iniciant diagnostic...")

# 2. Imprimeix els valors "NodeA", "NodeB" i "NodeC" dins d'un mateix print() 
# utilitzant el paràmetre 'sep' perquè a la consola apareguin separats per un guió (ex: NodeA-NodeB-NodeC).
print("NodeA","NodeB","NodeC",sep="-")

# 3. Utilitza dos print() diferents per imprimir "Estat del sistema: " i "Operatiu", 
# però fes servir el paràmetre 'end' al primer print() per evitar el salt de línia automàtic, 
# de manera que el resultat complet es llegeixi a la mateixa línia.
print("Estat del sistema: ",end="")
print("Operatiu")

# 4. Imprimeix el resultat d'una operació matemàtica directament a dins d'un print() 
# (per exemple, sumar els ports disponibles: 12 + 12) per mostrar el número sense usar text.
print(12+5)

# 5. Imprimeix exactament la frase següent, incloent-hi les cometes dobles interiors:
# El rack fa "19" polzades d'amplada.
# Fes servir un dels mètodes vistos a classe per evitar l'error de sintaxi al combinar cometes.
print("""El rack fa "19" polzades d'amplada""")