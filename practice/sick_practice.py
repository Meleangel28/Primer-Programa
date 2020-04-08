peso_persona = 70
consumo_calorias_sentado = 1.66
consumo_calorias_dormido = 1.08
activity = ""
calorias_consumidas = 0
tiempo_actividad = 0  #Tiempo que duro realizando la actividad.

actividad = input("What activity are u doing?").lower()
tiempo_actividad = int(input("During how much time did you do that? (minutes)").lower())

if activity== "sleep":
    calorias_consumidas = consumo_calorias_dormido * tiempo_actividad
    print(calorias_consumidas, "calories consumed in your activity.")
elif activity == "sit":
    calorias_consumidas = consumo_calorias_sentado * tiempo_actividad
    print(calorias_consumidas, "calories consumed in your activity.")
else:
    print("Activity has not been recognized.")
print("Program ended.")