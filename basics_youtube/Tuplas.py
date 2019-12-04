# Las Tuplas son Listas que no pueden ser editadas.  (No remove, no append, no extend.)
# Si se puede ubicar un elemento en la tupla.
# Las tuplas se hacen con parentesis ()

Tupla = (5, 6, 7, "Angel")
print(Tupla[2])

# Creamos una lista con los datos de la tupla. list
Lista = list(Tupla)
print(Tupla)
print(Lista[:])

# Creamos una tupla con los datos de una lista. tuple
tupla2 = tuple(Lista)

# Cuantos elementos que senalemos existen en una tupla.
print(tupla2.count("Angel"))

# CUANTOS ELEMENTOS TIENE LA TUPLA (SIN CONTAR 0)
print(len(tupla2))

# Se pueden establecer variables con los valores dentro de una tupla.
TuplaEjemplo = ("Angel Melean", 28, 12, 2001, 30404963)
nombre, dia, mes, agno, cedula = TuplaEjemplo
print(nombre, mes, dia, agno, cedula)



