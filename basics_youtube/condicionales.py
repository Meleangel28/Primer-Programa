def evaluacion(nota):
    estatus = "Evaluacion aprobada."
    if nota < 5:
        print("Evaluacion reprobada.")
    return estatus

nota = int(input("Ingrese la nota del alumno: "))
print(evaluacion(nota))
