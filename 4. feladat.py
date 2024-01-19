f = open("adatok.txt","r",encoding="utf-8")

#Feltaláló

print("Lehetőségeid :","Thomas Edison","James Watt","Henry Ford")
TesztKérdés1 = input("Ki találta fel a gőzgépet? : ")
if TesztKérdés1 == "James Watt" :
    print("Helyes válasz!")
elif TesztKérdés1 == "Thomas Edison" :
    print("Helytelen válasz. James Watt volt.")
elif TesztKérdés1 == "Henry Ford" :
    print("Helytelen válasz. James Watt volt.")
else :
    print("Kérlek a lehetőségek közül válassz!")


#Évszám


print("Lehetőségeid :","1870","1712","1765")
TesztKérdés2 = input("Melyik évben? : ")
if TesztKérdés2 == "1765" :
    print("Helyes válasz!")
elif TesztKérdés2 == "1870" :
    print("Helytelen válasz.volt.")
elif TesztKérdés2 == "1712" :
    print("Helytelen válasz.  volt.")
else :
    print("Kérlek a lehetőségek közül válassz!")


"""
TesztKérdés2 = input("Melyik évben? : ")
"""
f.close()
