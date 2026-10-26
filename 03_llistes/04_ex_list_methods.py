# EXERCICI: Mètodes de llistes en la gestió d'una xarxa
# Resol els passos següents aplicant els mètodes de l'arxiu 02_list_methods.py:

# 1. Afegir i Inserir (append, insert):
# Tens una llista de servidors: servidors = ["DNS", "DHCP", "Web"]
# Afegeix "Correu" al final de la llista fent servir un mètode.
# Després, insereix "Proxy" exactament a la posició 1 (segon lloc).
# Imprimeix la llista resultant.
servidors = ["DNS", "DHCP", "Web"]
servidors.append("Correu")
servidors.insert(1,"Proxy")
print(servidors)

# 2. Estendre (extend):
# Tens un altre grup de servidors per afegir: nous_servidors = ["FTP", "VPN"]
# Fes servir el mètode adequat per afegir tots aquests elements al final de la llista 'servidors'.
# Imprimeix la llista actualitzada.
nous_servidors = ["FTP", "VPN"]
servidors.extend(nous_servidors)
print(servidors)


# 3. Eliminar (remove, pop):
# El servidor "DHCP" ha caigut. Elimina'l de la llista buscant directament el seu nom.
# Després, extreu (i elimina) l'últim servidor de la llista i desa'l a una variable anomenada 'servidor_apagat'.
# Imprimeix la variable 'servidor_apagat' i, a continuació, imprimeix la llista 'servidors'.
servidors.remove("DHCP")
servidor_apagat=servidors.pop(-1)

# 4. Ordenar (sort, sorted):
# Tens les velocitats de diversos ports: velocitats = [1000, 10, 100, 10000]
# Crea una NOVA llista (velocitats_ordenades) que estigui ordenada de menor a major, 
# però SENSE modificar la llista original. Imprimeix ambdues llistes per comprovar-ho.
velocitats = [1000, 10, 100, 10000]
velocitats_ordenades=sorted(velocitats)
print(velocitats)
print(velocitats_ordenades)
# 5. Cerca i recompte (in, count):
# Tens un registre d'errors: errors = ['Timeout', 'Connexió_Rebutjada', 'Timeout', 'Ping_Perdut']
# Imprimeix directament un valor booleà (True/False) que indiqui si 'Ping_Perdut' és dins la llista.
# Imprimeix quantes vegades apareix l'error 'Timeout' fent servir el mètode corresponent.
errors = ['Timeout', 'Connexió_Rebutjada', 'Timeout', 'Ping_Perdut']
print('Ping_Perdut'in errors)
print(errors.count('Timeout'))


# ==========================================