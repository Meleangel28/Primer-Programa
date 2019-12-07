# Libreria de matematicas.
from math import sqrt

def d(X2, X1, Y2, Y1):
    d = sqrt(((X2 - X1)**2) + ((Y2 - Y1)**2))
    return d

# Declaracion de variables.
X1 = X2 = X3 = 0.0
Y1 = Y2 = Y3 = 0.0
d_lado_uno = d_lado_dos = d_lado_tres = 0.0 # Distancia de cada uno de los lados.
cateto_uno = cateto_dos = hipotenusa_calculada = hipotenusa_real = 0.0
punto_uno = punto_dos = punto_tres = (0,0)

#Entrada del usuario
X1 = int(input("Ingrese X de P1: "))
Y1 = int(input("Ingrese Y de P1: "))

X2 = int(input("\nIngrese X de P2: "))
Y2 = int(input("Ingrese Y de P2: "))

X3 = int(input("\nIngrese X de P3: "))
Y3 = int(input("Ingrese Y de P3: "))

punto_uno = (X1, Y1)
punto_dos = (X2, Y2)
punto_tres = (X3, Y3)

print("El punto uno es {}".format(punto_uno))
print("El punto dos es {}".format(punto_dos))
print("El punto tres es {}".format(punto_tres))

# Procedimiento.
# Distancia entre puntos.

d_lado_uno = d(X2, X1, Y2, Y1)
d_lado_dos = d(X3, X2, Y3, Y2)
d_lado_tres = d(X3,X1, Y2, Y1)

print("\nLa distancia del lado uno es: {} ".format(d_lado_uno))
print("La distancia del lado dos es: {} ".format(d_lado_dos))
print("La distancia del lado tres es: {} ".format(d_lado_tres))

# Determinar cual es la hipotenusa (Distancia mayor = Hipotenusa)
if (d_lado_tres > d_lado_dos) and (d_lado_tres > d_lado_uno):
    hipotenusa_calculada = d_lado_tres
elif (d_lado_dos > d_lado_uno) and (d_lado_dos > d_lado_tres):
    hipotenusa_calculada = d_lado_dos
elif (d_lado_uno > d_lado_dos) and (d_lado_uno > d_lado_tres):
    hipotenusa_calculada = d_lado_uno


if d_lado_uno == hipotenusa_calculada:
    cateto_uno = d_lado_dos
    cateto_dos = d_lado_tres
elif d_lado_dos == hipotenusa_calculada:
    cateto_uno = d_lado_uno
    cateto_dos = d_lado_tres
elif d_lado_tres == hipotenusa_calculada:
    cateto_uno = d_lado_uno
    cateto_dos = d_lado_dos

print("\nLa hipotenusa calculada tiene una distancia de: {}".format(hipotenusa_calculada))
print("El cateto uno tiene una distancia de: {}".format(cateto_uno))
print("El cateto dos tiene una distancia de: {}".format(cateto_dos))

# Determinar hipotenusa real y decir que tipo de triangulo es.
hipotenusa_real = sqrt(((cateto_uno)**2)+((cateto_dos)**2))
print("\nLa hipotenusa real es de: {}".format(hipotenusa_real))

if hipotenusa_calculada == hipotenusa_real:
    print("Debido a que la hipotenusa calculada y la hipotenusa real son iguales entonces:")
    print("Es un triangulo rectangulo.")
    if cateto_uno == cateto_dos:
        print("Y debido a que ambos catetos son iguales entonces: ")
        print("Es un triangulo rectangulo isosceles.")
    else:
        print("Y debido a que ambos catetos no tienen el mismo valor entonces: ")
        print("Es un triangulo rectangulo escaleno.")
else:
    print("Debido a que la hipotenusa calculada no es igual a la hipotenusa real entonces: ")
    print("No es un triangulo rectangulo.")

print("Programa finalizado.")








