utility = 0
percentage = 0
antiquity = 0
salary = 0.0

salary = float(input("How much did you get paid monthly ($): "))
antiquity = int(input("Antiquity of the employee (years): "))

if (antiquity >= 0) and (antiquity <2):
    percentage = 0.05  #5%
elif (antiquity >= 2) and (antiquity <5):
    percentage = 0.07
elif (antiquity >= 5) and (antiquity <8):
    percentage = 0.10
elif (antiquity >= 8) and (antiquity <11):
    percentage = 0.15
elif antiquity >= 11:
    percentage = 0.20  #20%

print("Your utility is ", percentage * salary, "$")
