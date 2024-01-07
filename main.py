adatok = [
    [1712, "Vízkerék", "Thomas Newcomen", "Egyesült királyság"],
    [1760, "Textilgyártás mechanizálása", "Sir Richard Arkwright", "Egyesült királyság"],
    [1764, "Fonógép", "James Hargreaves", "Egyesült királyság"],
    [1765, "Gőzgép", "James Watt", "Egyesült királyság"],
    [1804, "Gőzvontatású vasút", "Richart Trevithick", "Egyesült királyság"],
    [1856, "Acélgyártás", "Henry Bessemer", "Egyesült királyság"],
    [1867, "Dinamó", "Werner von Siemens", "Németország"],
    [1870, "Telepített gépgyártás", "Henry Ford", "Amerikai Egyesült Államok"],
    [1876, "Telefon", "Alexander Graham Bell", "Amerikai Egyesült Államok"],
    [1879, "Elektromos izzó", "Thomas Edison", "Amerikai Egyesült Államok"],
    [1895, "Rádió", "Guglielmo Marconi", "Olaszország"],
    [1903, "Repülőgép", "Wright testvérek", "Amerikai Egyesült Államok"],
    [1908, "Ford T-Modell", "Henry Ford", "Amerikai Egyesült Államok"],
    [1913, "Tömegtermelés és szalaggyártás", "Henry Ford", "Amerikai Egyesült Államok"],
    [1917, "Fordson traktor", "Henry Ford", "Amerikai Egyesült Államok"],
    [1958, "Mikroelektronika", "Jack Kilby", "Amerikai Egyesült Államok"],
    [1969, "Internet", "Arpanet", "Amerikai Egyesült Államok"],
    [1970, "Asztali számítógép", "Intel corp.", "Amerikai Egyesült Államok"],
    [1973, "Mobiltelefon", "Martin Cooper", "Amerikai Egyesült Államok"],
    [1981, "Személyi számítógép", "IBM", "Amerikai Egyesült Államok"]
]

print("Üdv!\n1. Adatok listázása\n2. Adatok listázása fájlba...\n3. Keresés...")
valasz = int(input("A menüpontok közül válasszon egyet: "))
if valasz == 1:
    for i in adatok:
        for j in i:
            print(j, end=" - ")
        print()
elif valasz == 2:
    fajlnev = input("Adj meg egy fájlnevet: ")
    fajlnev = fajlnev + ".txt"

    with open(fajlnev, "a", encoding="utf-8") as file:
        for i in adatok:
            for j in i:
                print(j, file=file)
            print("", file=file)

elif valasz == 3:
    while True:
        eredmeny = []
        startyr = int(input("Add meg a kezdő évszámot: "))
        endyr = int(input("Add meg a befejező évszámot: "))
        if startyr < endyr:
            for i in adatok:
                if startyr <= i[0] <= endyr:
                    eredmeny.append(i)
            break
        else:
            print("A kezdő évszám nem lehet nagyobb a befejezőnél")
    print("A keresés eredménye:")
    for i in eredmeny:
        for j in i:
            print(j, end=" - ")
        print("")
