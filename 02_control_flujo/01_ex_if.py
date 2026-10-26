# EXERCICI: Control de flux d'un tallafocs (Firewall) i sensors
# Resol els passos següents aplicant els conceptes de 01_if.py:

# 1. Condicionals simples (if, elif, else):
# Tens una variable 'senyal_db' amb el valor -65.
# Escriu una estructura condicional on:
# - Si el senyal és major o igual a -50, imprimeixi "Senyal excel·lent".
# - Si és major o igual a -70 (però menor que -50), imprimeixi "Senyal bo".
# - Si és inferior, imprimeixi "Senyal feble".
senyal_db=-65
if senyal_db>=-50:
    print("excel·lent")
elif senyal_db>=-70 and senyal_db<-50:
    print("bo")
else:
    print("feble")

# 2. Condicions múltiples (and, or, not):
# Tens 'admin = True' i 'te_token = False'.
# Escriu un condicional que permeti l'accés (imprimeix "Accés permès") 
# només si és admin O té el token. Si no compleix cap de les dues, "Accés denegat".
# Després, fes un altre condicional separat fent servir 'not' per comprovar 
# si NO té token, i si és així, imprimeix "Cal renovar el token".
admin=True
te_token=False
if admin or te_token:
    print("acces permes")
else:
    print("acces denegat")

if not te_token:
    print("cal renovar el token")

# 3. Avaluació de Truthy/Falsy:
# Tens la variable 'ip_origen = ""'. 
# Fes servir un 'if' per comprovar directament la variable (sense fer servir '=='). 
# Si la variable té contingut (és True), imprimeix la IP. 
# Si està buida (és False), fes servir un 'else' per imprimir "IP desconeguda".
ip_origen=""
if ip_origen:
    print("es True")
else:
    print("es False")


# 4. Expressió condicional (if-else en una sola línia):
# Tens 'temperatura = 85'.
# Crea una variable 'estat_refrigeracio' que valgui "Activat" si la temperatura és >= 80, 
# o "Desactivat" si és menor. Tot això ho has de fer en una sola línia.
# Finalment, imprimeix 'estat_refrigeracio'.
temp=85
estat_refrigeracio="activat" if temp>=80 else "desactivat"
print(estat_refrigeracio)