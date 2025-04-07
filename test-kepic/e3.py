import random

print("Nastavi svoje geslo.")
geslo = input("Vnesi geslo: ")

print("\nPonovi geslo, da se preveri.")
ponovljeno_geslo = input("Ponovi geslo: ")

if geslo.lower() == ponovljeno_geslo.lower():
    print("Geslo je isto.")
else:
    print("Geslo se ne ujema. Poskusi znova.")

