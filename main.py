

with open("adatok.txt", "r", encoding="utf-8") as file:
    betoltott = file.readlines()

print("Üdv!\n1. Adatok listázása\n2. Adatok listázása fájlba...\n3. Keresés...")
valasz = int(input("A menüpontok közül válasszon egyet: "))
if valasz == 1:
    for i in betoltott:
        for j in i:
            print(j, end="")
        print()
elif valasz == 2:
    fajlnev = input("Adj meg egy fájlnevet: ")
    fajlnev = fajlnev + ".txt"

    with open(fajlnev, "a", encoding="utf-8") as file:
        file.writelines(betoltott)

elif valasz == 3:
    print("ok")