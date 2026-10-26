# EXERCICI: Automatització i monitoratge amb bucles while
# Resol els passos següents aplicant els conceptes de 01_loop_while.py:

# 1. Bucle infinit amb 'break':
# Crea una variable 'intents_connexio' a 0.
# Fes un 'while True:' que vagi sumant 1 a 'intents_connexio' i imprimeixi "Intentant connectar...".
# Si arriba a 3 intents, imprimeix "Connexió fallida, avortant" i trenca el bucle amb 'break'.
intens_connexio=0
while True:
    intens_connexio+=1
    if intens_connexio !=3:
        print("intentant connectar...")
    else:
        print("connexio fallida,avortant")
        break
    

# 2. Bucle amb 'continue':
# Crea una variable 'port' a 0.
# Fes un bucle 'while port < 5:'. Suma 1 a 'port' al principi del bucle.
# Si el port és el número 3 (reservat per gestió), fes servir 'continue' per saltar-lo i no fer res més.
# A la resta de ports, imprimeix "Configurant el port número {port}".
port=0
while port<5:
    port+=1
    if port == 3:
        continue
    print(f"configurant el port numero {port}")

# 3. Bucle amb 'else':
# Crea una variable 'paquets_enviats' a 0.
# Fes un bucle que s'executi mentre 'paquets_enviats < 3'.
# A cada iteració, imprimeix "Enviant paquet", i suma 1 a la variable.
# Afegeix un bloc 'else' al final del bucle que imprimeixi "Tots els paquets s'han enviat correctament".
paquets_enviats=0
while paquets_enviats<3:
    print("enviant paquet")
    paquets_enviats+=1
else:
    print("tots els paquets s'han enviat correctament")


# 4. Validació de dades d'entrada:
# Fes servir un bucle while per demanar a l'usuari una VLAN vàlida (entre 1 i 4094).
# Crea una variable 'vlan' inicialitzada a 0.
# Mentre la vlan sigui menor que 1 o major que 4094, torna a demanar l'input (recorda el càsting a int!).
# Quan surti del bucle, imprimeix "VLAN {vlan} configurada correctament."
vlan=int(input("introdueix una vlan valida"))
while vlan>4094 or vlan<1:
    vlan=int(input("introdueix una vlan valida"))
else:
    print(f"VLAN {vlan} configurada correctament")



