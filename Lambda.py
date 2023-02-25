slova = ["kočka", "pes", "kachna", "krokodýl", "hroch", "tygr", "lev", "slepice", "králík", "krokodýl"]
a = input("Zadej první písmeno, které chceš hledat v seznamu slov: ")
b = input("Zadej druhé písmeno, které chceš hledat v seznamu slov: ")

vysledek = list(filter(lambda x: a in x, slova))
vysledek2 = list(filter(lambda y: b in y, slova))

print("Slova kde je obsaženo písmeno " + str(a) + " " + str(vysledek))
print("Slova kde je obsaženo písmeno " + str(b) + " " + str(vysledek2))
