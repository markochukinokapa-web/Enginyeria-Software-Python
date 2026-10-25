###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
comptador = 0
while comptador<10:
    comptador+=1
    print(comptador)

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
comptador = 0
suma = 0
while comptador<=20:
    comptador+=1
    if comptador%2==0:
        suma+=comptador
else:
    print(f"\n la suma es {suma}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
num=int(input("introdueix un numero enter positiu"))
i=0
mult=1
while i !=num:
    i+=1
    mult=mult*i
print(f"\n {mult}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
cont=input("\n introdueix una contrasenya")

while len(cont)<8:
     cont=input("\n introdueix una contrasenya, que aquesta es massa curta")
   

print("la contrasenya es valida")
    
# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
i=0
multip=1
num=int(input("\n introdueix un numero enter"))
while i<10:
    i+=1
    multip=i*num
    print(f"\n {num}*{i}={multip}")

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
N = int(input("Introdueix un número enter positiu: "))

numero = 2

while numero <= N:
    divisor = 2
    es_primer = True

    while divisor < numero and es_primer:
        if numero % divisor == 0:
            es_primer = False
        divisor += 1

    if es_primer:
        print(numero)

    numero += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
num=int(input("\n introdueix un numero enter"))
suma=0
while num!=0:
    suma+=num
    num=int(input("\n introdueix un numero enter"))
print(f"\n resultat es{suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
num=int(input("\nntrodueix un numero enter positiu"))
xifres=1
while num !=1:
    num=num//10
    xifres+=1
print(f"\n {xifres}")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
fibo=int(input("\nquants termes de fibonacci vols veure?"))
i=0
i0=0
i1=1
i3=0
print(i0)
print(i1)
while i<fibo:
    i3=i1+i0
    print(i3)
    i0,i1=i1,i3
    i+=1


# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
num=7
adi=int(input("\nintrodueix un numero enter"))
while adi!=num:
    if adi<num:
        print("el numero secret es mes gran")
        adi=int(input("\nintrodueix un numero enter"))
    elif adi>num:
        print("el numero secret es mes petit")
        adi=int(input("\nintrodueix un numero enter"))
print("has endivinat el numero!")