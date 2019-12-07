from math import sqrt
a = b = c = d = 0.0
sol_uno = sol_dos = 0.0 #Solucion uno y dos.

print("Para ejecutar exitosamente el programa solo puede haber UN valor igual a 0.")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = (b**2 - 4*a*c)

if (a!=0 and b!=0 and c!=0):
    print("Ecuacion de segundo grado completa.")
    if d > 0:
        print("Existen dos soluciones reales diferentes.")
        sol_uno = (-b + (sqrt( (b**2)-(4*a*c) ))) / (2*a)
        sol_dos = (-b - (sqrt( (b**2)-(4*a*c) ))) / (2*a)
        print("X1= {} y X2 = {}".format(sol_uno, sol_dos))
        
    elif d == 0:
        print("Existen dos soluciones reales identicas.")
        sol_uno = -b/a
        sol_dos = sol_uno
        print("X1= {} y X2 = {}".format(sol_uno, sol_dos))
        
    elif d < 0:
        print("No existen soluciones reales para la ecuacion.")
        
elif (a != 0 or b!= 0 or c != 0):
    print("Ecuacion de segundo grado incompleta.")
    
    if(a == 0 and b!=0 and c !=0) :
        print("Tenemos una solucion real.")
        sol_uno = -c/b
        print("X1= {}".format(sol_uno))
              
    elif(b == 0 and a!=0 and c!=0):
        print("Tenemos dos soluciones.")
        sol_uno = sqrt(-c/a)
        sol_dos = -(sqrt(-c/a))
        print("X1= {} y X2 = {}".format(sol_uno, sol_dos))
              
    elif(c == 0 and a != 0 and b != 0):
        print ("Tenemos dos soluciones. ")
        sol_uno = 0
        sol_dos = -b/a
        print("X1= {} y X2 = {}".format(sol_uno, sol_dos))
              
print("\n Programa finalizado.")
