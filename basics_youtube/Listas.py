#Inventario American Bucks

Productos = ["Irish Spring","Nescafe 200g", "Nutella 950gr","Nutella 200gr", "HeadAndShoulders"]

#Cuando es negativo cuenta desde el final (desde -1 para adelante)
print(Productos[0])
print(Productos[-1])

#Porciones
print(Productos[0:3])
print(Productos[:3])

#Desde el elemento de indice 2 (3er elemento) hasta el final de la lista.
print(Productos[2:])

#
#Agregar elementos a la lista.
#Agregar al final de la lista.
Productos.append("Josefa")
print(Productos[:])

#Agregar en algun indice en concreto.
Productos.insert(2,"Josefina")
print(Productos[:])

#Agregar mas items (Enlazar otra parte a una lista) (Lista+Lista)
print("Anadimos 3 items.")
Productos.extend(["Angel", "Carlos", "Valeria"])
Lista1 = ["Angel", 5 , False, "Pedro"]
Lista2 = ["Carlos", 18, True, "Juan"]
Lista3 = Lista1 + Lista2
print(Lista3[:])
#


#Ubicar cual es el indice de un valor.
print(Productos.index("Angel"))

#Comprobar si un elemento esta en la lista. True or False.
print("Angel" in Productos)

#Eliminar elementos. .remove
print(Productos[:])
Productos.append ("Melchor")
print("Melchor agregado.")
print(Productos[:])
print("Melchor removido.")
Productos.remove("Melchor")
print(Productos[:])

#Eliminar el ultimo elemento de una lista. .pop
print(Productos[:])
Productos.append ("Melchor")
print("Melchor agregado.")
print(Productos[:])
print("Melchor removido.")
Productos.pop()
print(Productos[:])

#Repetidor de listas.
Lista1 = ["Angel", 5 , True] * 3
print(Lista1[:])