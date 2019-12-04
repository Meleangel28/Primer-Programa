def valorXY():
    X = int(input("Valor X: "))
    Y = int(input("Valor Y: "))
    return X, Y

def suma():
    C = A + B
    print("La suma de estos dos valores es ", C)


(A, B) = valorXY()
# Aca ya esta establecido el valor de A y B gracias a la funcion.
suma()
"""
def suma2(num1, num2):
    resultado = (num1 + num2)
    return resultado

X = int(input("Valor de X: "))
Y = int(input("Valor de Y: "))

print("La suma de los datos suministrados es ", suma2(X, Y))

"""
