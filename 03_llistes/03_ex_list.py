# EXERCICI: Gestió d'inventari i configuració de xarxa amb Llistes
# Resol els passos següents aplicant els conceptes de l'arxiu 01_list.py:

# 1. Creació i accés per índex:
# Tens una llista d'equips: equips = ["Router_Core", "Switch_A", "Firewall", "AP_1", "AP_2"]
# Imprimeix el primer equip (índex 0) i l'últim equip fent servir un índex negatiu.
equips = ["Router_Core", "Switch_A", "Firewall", "AP_1", "AP_2"]
print(equips[0])
print(equips[-1])

# 2. Slicing (talls):
# Fent servir la mateixa llista 'equips', imprimeix una subllista que contingui
# només els equips del mig (des de "Switch_A" fins a "AP_1" inclòs).
# Després imprimeix la llista completa però en ordre invers.
print(equips[1:4])

# 3. Modificació i longitud:
# L'equip "Firewall" s'ha espatllat i l'has substituït per "Firewall_V2".
# Modifica aquest element a la llista accedint-hi pel seu índex.
# Després, imprimeix la quantitat total d'equips fent servir la funció len().
equips[2]="Firewall_V2"
print(len(equips))

# 4. Afegir elements:
# Han arribat dos equips nous: ["AP_3", "AP_4"].
# Afegeix-los a la llista original fent servir la sintaxi curta i eficient (+=).
# Imprimeix la llista resultant.
equips+=["AP_3","AP_4"]
print(equips)


# 5. Llistes de llistes (Matrius):
# Tens una matriu que representa l'estat dels ports d'un switch de 2 pisos:
# ports_switch = [[1, 2, 3, 4], [5, 6, 7, 8]]
# Accedeix i imprimeix el número 7 fent servir la doble indexació [][].
ports_switch = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(ports_switch[1][2])

