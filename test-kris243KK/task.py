import random

stevilo1 = random.randint(1, 100)
stevilo2 = random.randint(1, 100)
st3 = random.randint(1,2)
st4 = random.randint(1,2)

produkt = stevilo1 * stevilo2

print(f"Prvo naključno število: {stevilo1}")
print(f"Drugo naključno število: {stevilo2}")
print(f"Če kupiš LOTTO dobiš: {produkt}")


print(f"Recimo, da si zdel {produkt}EUR, jih želiš mogoče podvojiti na Roulette-i?")

odgovor = input("Vnesi DA ali NE:")

if odgovor == "DA":
    ugane = int(input("Vnesi število 1 ali 2:"))
    if ugane == st3:
        produkt = produkt * 2
        print(f"Čestitam! Podvojil si zadetek, zdaj imaš {produkt}. Dobro ti gre, lahko bi še podvojil svoj dobiček ;) Kaj praviš?")
        odg2 = input("Vnesi DA ali NE:")
        if odg2 == "DA":
            ugane2 = int(input("Vnesi število 1 ali 2:"))
            if ugane2 == st4:
                produkt = produkt * 2
                print(f"Čestitam! Še enkrat si podvojil zadetek, zdaj imaš {produkt}. Dosti za danes, pojdi domov.")
            else:
                print("Žal tokrat ni šlo :/")
        else:
            print(f"V redu, ostajaš pri {produkt}. Pametna odločitev!")
    else:
        print("Žal nisi uganil. Dobiček je 0.")
else:
    print("V redu, kupi si kaj lepega ali pa pojdi igrat Blackjack.")