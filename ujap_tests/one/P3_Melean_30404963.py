#Parte numero 5 de la evaluacion.

producto = int(input("Cuantos productos compro? "))

if producto <= 1000:
    producto = 2 * producto
    print("Verdadero")
else:
    print("Falso")

#Parte numero 6 de la evaluacion

m = a = b = 0.0
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
if b == 0:
    print("Datos invalidos.")
else:
    m = a/b
    print (m)

#Parte numero 7 de la evaluacion.
#Y = 4X**2 -16X + 15

X = 1.0
Y = 0.0
Estatus = ""

print("X           Y        Estatus")
while X <= 2.1:
    Y = (4* X**2 - 16*X + 15)
    if Y > 0:
        Estatus = "POSITIVO"
    else:
        Estatus = "NEGATIVO"
    print(f"{X:2.1f}        {Y:3.2f}        {Estatus:8}")
    X += 0.1

print("Fin del programa.")