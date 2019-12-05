
"""
edad_angel = 17
agno_nacimiento = 2001

print("La edad de Angel es {}, y el nacio en {}.".format(edad_angel, agno_nacimiento))
print('La edad de Angel es', edad_angel, 'y nacio en', agno_nacimiento, '.')
"""

number_to_guess = 4
attemps = 5
while attemps != 0:
    user_number = int(input("Adivina un numero: "))
    if user_number == number_to_guess:
        print("Usted gano la adivinanza.")
        break
    elif user_number != number_to_guess:
        attemps -= 1
        print("No adivino el numero, tiene un intento menos.")