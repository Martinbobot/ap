while True:
    clen1 = int(input("Zadejte prvni clen"))
    clen2 = int(input("Zadejte prvni clen"))
    
    """
    print("1. Součet")
    print("1. Rozdíl")
    print("1. Součin")
    print("1. Podíl")
   """
    print("1. Součet \n2. Součin\n3. Rozdíl \n4. Podíl")

    operace = int(input("Vyberte číslo početní operace, kterou chcete"))

    match operace:
        case 1:
            soucet = clen1 + clen2
            print("Součet je: " + str(soucet))
        case 2:
            soucin = clen1 * clen2 
            print("Soucin je: " + str(soucin))
        case 3: 
            rozdil = clen1 - clen2
            print("Rozdíl je:" + str(rozdil))
        case 4:
            if clen2 == 0:
                print("Nelze dělit 0")
            else:
                podil = clen1 / clen2
                print("Podíl je: " + str(podil))
              
            
    konec = input("Prejete si ukoncit program? Y/N")
    if konec == "Y" or konec == "y":
        break
    elif konec == "N" or konec == "n":
        print("Jdeme na další výpočet")
    else:
        print("Neplatné zadání, program se zhroutí")
        break

