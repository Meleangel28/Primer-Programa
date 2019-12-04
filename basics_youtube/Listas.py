#Inventario American Bucks

productos = ["Irish Spring", "Nescafe 200g", "Nutella 950gr", "Nutella 200gr", "HeadAndShoulders"]

#Cuando es negativo cuenta desde el final (desde -1 para adelante)
print(productos[0])
print(productos[-1])

#Porciones
print(productos[0:3])
print(productos[:3])

#Desde el elemento de indice 2 (3er elemento) hasta el final de la lista.
print(productos[2:])

#
#Agregar elementos a la lista.
#Agregar al final de la lista.
productos.append("Josefa")
print(productos[:])

#Agregar en algun indice en concreto.
productos.insert(2, "Josefina")
print(productos[:])

#Agregar mas items (Enlazar otra parte a una lista) (Lista+Lista)
print("Anadimos 3 items.")
productos.extend(["Angel", "Carlos", "Valeria"])
Lista1 = ["Angel", 5 , False, "Pedro"]
Lista2 = ["Carlos", 18, True, "Juan"]
Lista3 = Lista1 + Lista2
print(Lista3[:])
#


#Ubicar cual es el indice de un valor.
print(productos.index("Angel"))

#Comprobar si un elemento esta en la lista. True or False.
print("Angel" in productos)

#Eliminar elementos. .remove
print(productos[:])
productos.append ("Melchor")
print("Melchor agregado.")
print(productos[:])
print("Melchor removido.")
productos.remove("Melchor")
print(productos[:])

#Eliminar el ultimo elemento de una lista. .pop
print(productos[:])
productos.append ("Melchor")
print("Melchor agregado.")
print(productos[:])
print("Melchor removido.")
productos.pop()
print(productos[:])

#Repetidor de listas.
Lista1 = ["Angel", 5 , True] * 3
print(Lista1[:])