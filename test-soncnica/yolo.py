print("Hello World, Sandra was here.!.")

#Napiši program, ki se začne s seznamom ovir in številko stolpca in izpiše številko vrstice s prvo oviro.
#Predpostaviti smeš, da bo kolesar vedno naletel na oviro.

ovire = [(1, 3, 6), (2, 4, 3), (4, 6, 7),
         (3, 4, 9), (6, 9, 5), (9, 10, 2), (9, 10, 8)]
minimum = len(ovire)
koordinata_x = int(input("Koordinata x: "))

for koordinate in ovire:
    x1, x2, y = koordinate
    if x1 <= koordinata_x and koordinata_x <= x2:
        if y < minimum:
            minimum = y
print("Kolesar je naletel na oviro na koordinati x, y: " + str(koordinata_x) + ", " + str(minimum))