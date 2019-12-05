# Clave:Valor
diccionario = {"Alemania":"Berlin", "Francia":"Paris", "Venezuela":"Caracas", "Espanga":"Madrid"}

# Agnadir un valor a un diccionario.
diccionario["Italia"] = "Lisboa"
print(diccionario)

# Como modificar/reemplazar un valor de un diccionario.
diccionario["Italia"] = "Roma"
print(diccionario["Francia"])
print(diccionario)

# Como eliminar un elemento.
del diccionario ["Venezuela"]
print(diccionario)

diccionario_dos = {23:"Jordan", "Angel":28, 30404963:"Cedula"}
print(diccionario_dos)

# Ponerle clave a los valores del diccionario con una tupla.
tupla_uno = ("Espanga", "Francia", "Venezuela", "Argentina")
diccionario_tres = {tupla_uno[0]:"Madrid", tupla_uno[1]:"Paris", tupla_uno[2]:"Caracas", tupla_uno[3]:"Buenos Aires"}
print(diccionario_tres)
print(diccionario_tres["Francia"])
print(diccionario_tres[tupla_uno[1]])

# Como crear un diccionario con un elemento que sea una tupla.
diccionario_cuatro = {23:"Jordan", "Nombre":"Michael","Equipo":"Chicago", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(diccionario_cuatro["anillos"])

# Diccionario con diccionario dentro.
diccionario_cinco = {23:"Jordan", "Nombre":"Michael","Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(diccionario_cinco["anillos"])

# Funciones de los diccionarios keys, values, len
print(diccionario_cinco.keys())
print(diccionario_cinco.values())
print(len(diccionario_cinco))