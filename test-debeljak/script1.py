import random

nakljucno_stevilo = random.randint(0,999)
konec = False

while konec == False:
    poskus_ugibanja = int(input("Vnesite število, ki mislite, da si ga je izbral program med 0 in 999: "))
    if poskus_ugibanja > nakljucno_stevilo:
        print(f"Število {poskus_ugibanja} je večje od števila, ki si ga je izbral program.")
    elif poskus_ugibanja < nakljucno_stevilo:
        print(f"Število {poskus_ugibanja} je manjše od števila, ki si ga je izbral program.")
    elif poskus_ugibanja == nakljucno_stevilo:
        print(f"Število {poskus_ugibanja} je enako kot število, ki si ga je izbral program. \n Čestitke!")
        konec = True