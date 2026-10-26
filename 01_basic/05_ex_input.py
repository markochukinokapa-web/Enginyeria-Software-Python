# EXERCICI: Configuració interactiva d'equips de xarxa
# Resol els passos següents aplicant els conceptes de 05_input.py:

# 1. Entrada de text bàsica:
# Demana a l'usuari (el tècnic) que introdueixi el nom del router utilitzant input()
# i guarda-ho en una variable. Després, imprimeix un missatge de confirmació 
# fent servir un f-string (ex: "S'ha accedit al router: [nom]").
nom=input("intrpdueix el nom del router")
print(f"confirmat el nom {nom}")

# 2. Entrada amb conversió de tipus (càsting):
# Demana a l'usuari el nombre de ports disponibles actualment al switch.
# Com que l'input() retorna text, converteix-lo a enter (int) i suma-li 4 ports 
# d'un mòdul d'expansió nou. Imprimeix el resultat total calculat.
nombres=input("introdueix el nombre de ports disponibles actualment")
nombres=int(nombres)
print(f"{nombres+4}")

# 3. Múltiples valors amb split():
# Demana a l'usuari que introdueixi l'adreça IP i la Màscara de subxarxa separades per un espai.
# Utilitza .split() per assignar aquestes dades a dues variables de cop (ex: ip, mascara).
# Imprimeix un missatge que mostri les dues dades llegides.
IP, mascara=input("introdueix el IP i la mascara separades per un espai\n").split()
print(f"{IP} {mascara}")


