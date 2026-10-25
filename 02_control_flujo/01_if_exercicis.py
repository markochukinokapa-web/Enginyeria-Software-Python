###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num1,num2=input("introdueix dos nombres qualsevols\n").split()
num1=float(num1)
num2=float(num2)
if(num1>num2):
    print(f"\n{num1} es mes gran que {num2}")
elif(num2>num1):
    print(f"\n{num2} es mes gran que {num1}")
else:
    print("els dos son iguals")

# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
num1,num2,op=input("introdueix un dividend,un divisor i la operacio desitjada(+,-,*,/)\n").split()
num1=float(num1)
num2=float(num2)
if(op=="+"):
    num3=num1+num2
elif(op=="-"):
    num3=num1-num2
elif(op=="*"):
    num3=num1*num2
elif(op=="/"):
    if(num1 ==0):
        print("l'operacio es impossible")
        num3="invalid"
    else:
        num3=num1//num2
print(f"\n el resultat es {num3}")

# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.
any=int(input("introdueix un any\n"))

if(any%400 != 0 or(any%100 == 0 and any%4 != 0)):
    print(f"\n {any} no es de traspas")
else:
    print(f"\n {any} es de traspas")

# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edat=int(input("quans anys te\n"))
if(edat>=0 and edat<=2):
    print(f"\n es un nadó")
elif(edat>=3 and edat<=12):
    print(f"\n es un infant")
elif(edat>=13 and edat<=17):
    print(f"\n es un adolescent")
elif(edat>=18 and edat<=64):
    print(f"\n es un adult")
else:
    print(f"\n es una persona gran")


# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
qualit=int(input("\n introdueix la qualitat del senyal Wi-Fi en dBm"))
if(qualit < -75):
    print(f"\n es molt feble")
elif(qualit => -75 and qualit < -67):
    print(f"\n es feble")
elif(qualit => -67 and qualit < -50):
    print(f"\n es bona")
elif(qualit => -50):
    print(f"\n es molt bona")

# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
opt=int(input("\n introdueix la potencia optica rebuda en dBm"))
if(-27 <= opt <= -8):
    print(f"\n es acceptable")
elif(opt < -27):
    print(f"\n es massa baix")
else:
    print(f"\n es massa alt")

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
dades=float(input("\n quin es el consum de dades en GB"))
if(dades<=20):
    print("\n el consum es dins del limit")
else:
    print("\n el consum es fora del limit")
    exces = dades-20
    print(f"\n s'ha excedit {exces}Gb")

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
LOS=int(input("\n esta ences l'indicador LOS(introdueix un 1 per si i un 0 per no)"))
router=int(input("\n esta ences l'indicador router(introdueix un 1 per si i un 0 per no)"))

if(LOS==1 and router== 0):
    print("\n cal revisar el servei del proveidor")
elif(LOS==1 and router== 1):
    print("\n cal revisar el servei del cable de F.O")
else:
    print("\n tot funciona correctament")

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = int(input("Indica el percentatge de bateria disponible: "))

if bateria < 0 or bateria > 100:
    print("Valor fora del rang. Ha de ser entre 0 i 100.")
elif bateria < 20:
    print("El nivell és crític.")
elif bateria < 50:
    print("El nivell és baix.")
else:
    print("El nivell és suficient.")


# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
lat,perc=input("\nintrodueix la latencia en ms i el percentatge de paquets perduts").split()
lat=int(lat)
perc=float(perc)
if lat<0 or 100>perc<0:
    print("\n error")
elif lat<=30 and perc<=1:
    print("\n la connexio es excel·lent")
elif lat<=80 and perc<=3:
    print("\n la connexio es bona")
elif lat<=150 and perc<=5:
    print("\n la connexio es acceptable")
else:
    print("\n la connexio es deficient")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
pla,consum=input("\n introdueix el tipus de pla(basic/plus) i el consum mensual en GB").split()
consum=float(consum)
if(pla!="basic" or pla!="plus" and(consum<0)):
    print("error")
elif pla=="basic":
    if consum-10>0:
        cost=10+((consum-10)*1.5)
    else:
        cost=10
elif pla=="plus":
    if consum-30>0:
        cost=20+((consum-30)*0.75)
    else:
        cost=20
print(f"\n el cost total es {cost}")

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
contrasenya=2006
codi=3420
compte=int(input("esta actiu el compte(1/0)?"))
checkcontr=int(input("\n introdueix la contrasenya"))
if compte==0:
    print("\n el compte no esta activat, es denega el acces")
elif checkcontr!=contrasenya:
    print("\n la contrasenya es incorrecta,es denega l'access")
else:
    checkcodi=int(input("\n introdueix el codi"))
    if checkcodi!=codi:
        print("\n el codi es incorrecte,es denega l'access")
    else:
        print("\n es permet l'access")
    
    


# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router=input("\n esta ences el router?(1/0)"))
LOS=input("\n esta ences el indicator LOS?(1/0)"))
internet=input("\n esta ences el indicator internet?(1/0)"))
if router == "0":
    print("\n cal encendre el router")
elif LOS =="1":
    print("\n cal revisar el cable de fibra ")
elif internet =="0":
    print("\n cal contactar amb el proveidor")
else:
    print("\n tot funciona correctament")

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
critic=input("\n esta afectat un servei critic?(1/0)")
usuaris=int(input("\n quants usuaris estan afectats?"))
alt=input("\n hi ha alternativa?(1/0)")
if usuaris<0:
    print("\n error")
elif (critic == "1" or usuaris >= 50) and alt == "0":
    prioritat="critica"
elif usuaris>=10 or critic=="1":
    prioritat="alta"
else:
    prioritat="baixa"
    