class Mnenje:
    def __init__(self, uporabnik, ocena, komentar):
        self.uporabnik = uporabnik
        self.ocena = ocena
        self.komentar = komentar

    def prikazi(self):
        print(f"Uporabnik: {self.uporabnik}")
        print(f"Ocena: {self.ocena} / 5")
        print(f"Komentar: {self.komentar}")
        print("--------------------------")


vsa_mnenja = []

while True:
    print("\nIzberite možnost:")
    print("1. Dodaj mnenje")
    print("2. Prikaži vsa mnenja")
    print("3. Izhod")

    izbira = input("Vaša izbira: ")

    if izbira == "1":
        uporabnik = input("Vnesi svoje ime: ")

        ocena_vnos = input("Vnesi oceno (1 do 5): ")

        if not ocena_vnos.isdigit():
            print("Vnesi prosim samo celo število (npr. 3).")
            continue

        ocena = int(ocena_vnos)

        if ocena < 1 or ocena > 5:
            print("Ocena mora biti med 1 in 5.")
            continue

        komentar = input("Vnesi komentar: ")

        novo_mnenje = Mnenje(uporabnik, ocena, komentar)
        vsa_mnenja.append(novo_mnenje)
        print("Hvala za vaše mnenje!")

    elif izbira == "2":
        if not vsa_mnenja:
            print("Ni še nobenih mnenj.")
        else:
            print("\n--- Mnenja uporabnikov ---")
            for mnenje in vsa_mnenja:
                mnenje.prikazi()

    elif izbira == "3":
        print("Hvala, se vidimo naslednjič!")
        break

    else:
        print("Poskusi znova.")
