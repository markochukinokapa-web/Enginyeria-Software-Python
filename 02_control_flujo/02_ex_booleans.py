# EXERCICI: Lògica booleana en el monitoratge de xarxes
# Resol els passos següents aplicant els operadors de 02_booleans.py:

# 1. Operadors de comparació numèrica:
# Tens el ping d'un servidor (ping_ms = 45) i el llindar màxim permès (ping_maxim = 50).
# Crea una variable 'latencia_ok' que emmagatzemi el resultat booleà de comprovar
# si el ping és menor o igual que el màxim. Imprimeix el resultat de la variable.
ping_ms=45
ping_maxim=50
latencia_ok=ping_ms<ping_maxim
print(latencia_ok)

# 2. Comparació de cadenes de text (case-sensitive):
# Un tècnic intenta accedir al router amb el nom "Admin", però el sistema espera "admin".
# Fes un print que compari directament si ambdues cadenes són exactament iguals (==) 
# per comprovar si l'accés retorna True o False.
print("Admin==admin","Admin"=="admin")


# 3. Operador lògic 'and' i 'not':
# Perquè un enllaç òptic funcioni, el làser ha d'estar actiu (laser_on = True)
# i no hi ha d'haver talls al cable (cable_tallat = False).
# Crea una variable 'enllac_operatiu' que avaluï que el làser estigui encès 
# I (and) que el cable NO (not) estigui tallat. Imprimeix el resultat.
laser_on = True
cable_tallat = False
enllaç_operatiu=laser_on and not cable_tallat
print(enllaç_operatiu)
# 4. Operador lògic 'or':
# El sistema de seguretat d'un rack s'activa si la temperatura passa de 75 graus (temp = 80)
# O si el sensor de fum detecta fum (fum = False).
# Avalua directament dins d'un print() si (temp > 75) or (fum == True).
temp=80
fum=False
print("s'activa el sistema de seguretat?: ", temp>75 or not fum)


