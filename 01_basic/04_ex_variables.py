# EXERCICI: Gestió de variables en un node de xarxa
# Resol els passos següents segons els conceptes de 04_variables.py:

# 1. Assignació i tipatge dinàmic:
# Crea una variable anomenada 'estat_node' (fent servir la convenció snake_case) i assigna-li el text "Actiu".
# Imprimeix-la i després mostra'n el tipus de dada amb la funció type().
estat_node="activo"
print(estat_node)
print(type(estat_node))

# 2. Reassignació (comprovant el tipatge dinàmic):
# A la mateixa variable 'estat_node', assigna-li ara el número 1 (simulant l'estat en format enter).
# Torna a imprimir-ne el tipus per comprovar que efectivament ha canviat a 'int'.
estat_node=1
print(type(estat_node))

# 3. Ús de f-strings (cadenes formatades):
# Crea una variable 'amplada_banda' amb el valor 500.
# Fes servir un f-string per imprimir exactament aquesta frase (fent la multiplicació a dins de les claus {}):
# "L'amplada de banda actual és de 500 Mbps, si la dupliquem serà de 1000 Mbps."
amplada_banda=500
print(f"L'amplada de banda actual es de {amplada_banda}Mbps,si la dupliquem sera de {amplada_banda*2}")

# 4. Constants (Convenció):
# Les constants en Python no existeixen nativament, però hi ha una convenció per indicar-les.
# Crea una "constant" anomenada VELOCITAT_LLUM i assigna-li el valor 300000.
VELOCITAT_LLUM=3000

# 5. Anotacions de tipus:
# Crea una variable 'fibra_connectada' utilitzant l'anotació de tipus per indicar explícitament 
# que és un booleà (bool) i assigna-li el valor True.
fibra_connectada: bool=True
print(fibra_connectada)

# 6. Noms no vàlids:
# Escriu un nom de variable que comenci per un número (ex: 1_router) i assigna-li un valor.
# Deixa aquesta línia comentada amb un '#' al davant perquè el programa no doni error, 
# i explica breument al costat per què és incorrecte.
#1_numero=10

