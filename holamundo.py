
edad = 0
NI = 0
AD = 0
AD_M = 0
ini = 0

while ini < 10:
    edad = int(input("Ingrese edad: "))
    while edad > 0 and edad < 130:
        ini = ini + 1
        while edad > 0 and edad <= 17:
            NI = NI + 1
        while edad >= 18 and edad <=60:
            AD = AD + 1
        while edad >= 61 and edad <= 130:
            AD_M = AD_M + 1
    else:
        print ("Ingrese una edad dentro del rang0 1 - 130")

print("Niños: ",NI,"Adultos:", AD, "Abuelos:", AD_M)