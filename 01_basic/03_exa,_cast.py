# EXERCICI: Configuració d'un node de xarxa (Conversió de tipus)
# Resol els passos següents aplicant el càsting (int, str, float, bool, round):

# 1. T'arriba el port base com a text: port_base = "8000".
# Converteix-lo a enter i suma-li 80 perquè el resultat numèric sigui 8080, i imprimeix-ho.
print(int("8000")+80)

# 2. Tens una IP parcial i un identificador d'equip: ip = "192.168.1." i equip = 25.
# Converteix l'equip a cadena de text (str) per concatenar-ho amb la IP i imprimir "192.168.1.25".
print("192.168.1"+str(25))

# 3. El sensor de fibra retorna l'atenuació com a text: atenuacio = "3.1416".
# Converteix aquest valor a float i utilitza la funció type() dins del print() per comprovar-ne la classe.
atenuacio="3.1416"
atenuacio=float(atenuacio)
print(type(atenuacio))

# 4. Tens el valor de potència: potencia = 2.75.
# Imprimeix aquest valor convertit a enter (per truncar-lo) i després imprimeix-lo arrodonit (round) 
# per veure la diferència entre int() i round().
print(round(2.51))
print(int(2.51))

# 5. Avaluació booleana (True/False):
# Imprimeix l'avaluació booleana del número 0 (simulant que no hi ha errors a la xarxa).
# Imprimeix l'avaluació booleana d'una cadena amb un espai " " (simulant un camp de contrasenya mal introduït).
print(bool(0))
print(bool(""))