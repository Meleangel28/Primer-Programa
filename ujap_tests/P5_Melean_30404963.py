#Parte 1

# Cada registro tiene nombre del estudiante y nota final de este. Ejemplo: Angel, 17
# Que estructura condicional permite determinar el nombre del estudiante con mayor nota.
# En caso de mas de uno tener la misma nota, contar los demas.

nombre = ""
notaFin = 0.0
notaMax = 0.0 #Utilizado para almacenar el primer valor de la mayor calificacion.
Mnombre = "" #Nombre del estudiante con mayor calificacion.
contador = 0 # Cantidad de alumnos con la misma calificacion.

if notaFin > NotaMax:
    Mnombre = nombre
    notaMax = NotaFin
if notaFin == NotaMax:
    contador += 1

#_______________________________________________________________________________________________________________________

#Parte 2
nombre = ""
meses = 0
ventas_meses = 0
band = band2= 0
n = 2
i = 0

archivo = open("Ventas.txt")
for registro in archivo:
    Campos = registro.split (",")
    nombre = Campos[0]
    meses = Campos[1]
    n = 2
    i = ventas_meses = band = band2 = 0
    while i < len(Campos):
        i = i + 1
        band += 1
        if band > 2:
            band2 = int(Campos[n])
            n = n + 1
        ventas_meses = ventas_meses + band2

    print("{} vendio {}$".format(nombre, ventas_meses))