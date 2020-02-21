"""
for letra in "Python":
    if letra == "h":
        continue
    print(letra)
"""

nombre = "Angel Alberto Melean Hernandez"
contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1
print("Len(nombre): {}".format(contador))