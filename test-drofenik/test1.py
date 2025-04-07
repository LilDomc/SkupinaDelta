#pravilni paralerogram

while True:
    n = int(input("Vnesi velikost (minimum je 3, maximum je 99 in lahko je samo liho število): "))
    if n in range(3, 100) and n % 2 != 0:
        break
    else:
        print("Neveljaven vnos")

sredina = (n // 2) + 1  # Najdem mediano števila, mediana bo največ zvezdic

# Izris zgornjega dela paralelograma
for i in range(sredina):
    print(" " * (sredina - i - 1) + "*" * (2 * i + 1))

# Izris spodnjega dela paralelograma
for i in range(sredina - 1):
    print(" " * (i + 1) + "*" * (2 * (sredina - 1 - i) - 1))
