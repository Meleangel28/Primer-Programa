#Inicializacion de variables.
"""año de nacimiento"""
cedula = ano_nacimiento  = 0
ano_dosprimerosdigitos = 2
N1 = N2 = N3 = CODIGO = 0
temp = 0.0
temp2 = ""

#Entrada de datos.
cedula = int(input("Ingrese la cedula del empleado: "))
ano_nacimiento = int(input("Ingrese año de nacimiento del empleado: "))
print("Procesando... \n")

temp = ano_nacimiento
# Primeros dos digitos del codigo, dos primeros digitos del ano.
for i in range(0, 2):
    N1 = temp // 10
    temp = N1
str(N1)

temp = ano_nacimiento
#Ultimos dos digitos del codigos, dos ultimos numeros de ano.
for i in range (0, 2):
    N3 = temp % 10 #6
    temp2 = str(N3) + str(temp2)
    temp = temp // 10
N3 = temp2
str(N3)

#Cuatro primeros digitos impares y/o completar con 0
temp = 0
temp2 = ""
for i in range(0, cedula):
    temp = cedula % 10
    if temp == 1 or temp == 3 or temp == 7 or temp == 9:
        temp2 = temp2 + str(temp)
    cedula = cedula //10
for i in range(len(temp2), 4):
    temp2 = temp2 + "0"
N2 = temp2

CODIGO = (str(N1) + str(N2) + str(N3))
print("Codigo del empleado: {}".format(CODIGO))
print("Programa finalizado.")
