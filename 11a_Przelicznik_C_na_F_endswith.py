""" C = (F-32) * 5/9
    F = C * (9/5) + 32
"""

temperatura = input("Wprowadz temperature np. 55F lub 4C: ")

if temperatura.endswith("C"):
    F = float(temperatura[0:-1])* 9/5 +32
    print (F)

elif temperatura.endswith("F"):
    C = (float(temperatura[0:-1]) - 32) * 5 / 9
    print(C)

else:
    print("Cos poszlo nie tak!")