# Napišite program, ki uporabnika vpraša po imenu. Če je ime dolgo vsaj 6 znakov, naj program
# uporabnika obvesti, da je čas za skrajšanje imena.
# Dodatno: Program naj predlaga novo ime z največ 5 znaki

print("Program za rezanje imen v1.0.2-2024")

ime = input("Vnesi ime: ")

if len(ime) >= 6:
    print("Bil bi že čas za skrajašnje tvojega imena.")
    print(f"Recimo {ime[:5]} je lepo ime.")
