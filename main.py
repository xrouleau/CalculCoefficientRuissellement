import os

sols = []
typesVegetation = ["Culture", "Pâturage", "Boisé", "Lac", "Marécage"]
nombreSols = 0
pourcentageRestant = 100.0

os.system("cls")


def print_reponses(nb, veg, pen, clas, pourc, fin):
    if nb is not None:
        print("********** Sol #" + str(nb) + " **********")
    print("Végétation: " + typesVegetation[veg - 1])
    if pen is not None:
        print("Pente: " + str(pen) + "%")
    else:
        if fin:
            print("Pente: N/A")
    if clas is not None:
        print("Classification hydrologique: " + clas)
    else:
        if fin:
            print("Classification hydrologique: N/A")
    if pourc is not None:
        print("Pourcentage du terrain: " + str(pourc) + "%")


# Aire totale
while True:
    aireTotale = input("Quelle est la superficie du terrain(en hectare): ")
    try:
        aireTotale = float(aireTotale)
        if aireTotale <= 0:
            raise Exception
        break
    except Exception:
        print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
        continue
os.system("cls")

while True:
    # Réinitialisation des variables
    vegetation = None
    pente = None
    classHydro = None
    pourcentageSol = None

    # Numéro du sol
    nombreSols += 1
    print("********** Sol #" + str(nombreSols) + " **********")

    # Végétation
    while True:
        vegetation = input("Quel genre de végétation parmi les choix suivants:\n1 - Culture\n2 - Pâturage\n3 - Boisé\n4 - Lac\n5 - Marécage\nEntrez le numéro correspondant: ")
        try:
            vegetation = int(vegetation)
            if not 1 <= vegetation <= 5:
                raise Exception
            break
        except Exception:
            print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
            continue
    os.system("cls")
    print_reponses(nombreSols, vegetation, pente, classHydro, pourcentageSol, False)

    if vegetation <= 3:
        # Pente
        while True:
            pente = input("Quelle est la valeur de la pente: ")
            try:
                pente = float(pente)
                if 100 < pente < 0:
                    raise Exception
                break
            except Exception:
                print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
                continue
        os.system("cls")
        print_reponses(nombreSols, vegetation, pente, classHydro, pourcentageSol, False)
        # Classification Hydrologique
        while True:
            classHydro = input("Quelle est la classification hydraulique du sol: ").upper()
            if classHydro not in ["A", "B", "C", "D"]:
                print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
                continue
            break
        os.system("cls")
        print_reponses(nombreSols, vegetation, pente, classHydro, pourcentageSol, False)

    # Pourcentage de l'aire totale occupée par ce sol
    while True:
        pourcentageSol = input("Quel pourcentage de l'aire totale occupe ce sol: ")
        try:
            pourcentageSol = float(pourcentageSol)
            if not 0 < pourcentageSol <= 100:
                print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
                raise Exception
            if pourcentageRestant - pourcentageSol >= 0:
                break
            print("\nNOPE, PAS UNE OPTION!\nPOURCENTAGE ENTRÉ EST PLUS GRAND QUE POURCENTAGE DE TERRAIN RESTANT\nIL RESTE: " + str(pourcentageRestant) + "%\n")
            raise Exception
        except Exception:
            continue
    os.system("cls")

    match vegetation:
        case 1:
            if pente < 3:
                match classHydro:
                    case 'A':
                        coefficient = 0.22
                    case 'B':
                        coefficient = 0.36
                    case 'C':
                        coefficient = 0.47
                    case 'D':
                        coefficient = 0.51
            elif pente > 8:
                match classHydro:
                    case 'A':
                        coefficient = 0.32
                    case 'B':
                        coefficient = 0.51
                    case 'C':
                        coefficient = 0.67
                    case 'D':
                        coefficient = 0.73
            else:
                match classHydro:
                    case 'A':
                        coefficient = 0.25
                    case 'B':
                        coefficient = 0.43
                    case 'C':
                        coefficient = 0.59
                    case 'D':
                        coefficient = 0.67
        case 2:
            if pente < 3:
                match classHydro:
                    case 'A':
                        coefficient = 0.08
                    case 'B':
                        coefficient = 0.17
                    case 'C':
                        coefficient = 0.34
                    case 'D':
                        coefficient = 0.43
            elif pente > 8:
                match classHydro:
                    case 'A':
                        coefficient = 0.20
                    case 'B':
                        coefficient = 0.39
                    case 'C':
                        coefficient = 0.56
                    case 'D':
                        coefficient = 0.64
            else:
                match classHydro:
                    case 'A':
                        coefficient = 0.10
                    case 'B':
                        coefficient = 0.25
                    case 'C':
                        coefficient = 0.43
                    case 'D':
                        coefficient = 0.51
        case 3:
            if pente < 3:
                match classHydro:
                    case 'A':
                        coefficient = 0.04
                    case 'B':
                        coefficient = 0.15
                    case 'C':
                        coefficient = 0.29
                    case 'D':
                        coefficient = 0.37
            elif pente > 8:
                match classHydro:
                    case 'A':
                        coefficient = 0.11
                    case 'B':
                        coefficient = 0.26
                    case 'C':
                        coefficient = 0.43
                    case 'D':
                        coefficient = 0.51
            else:
                match classHydro:
                    case 'A':
                        coefficient = 0.07
                    case 'B':
                        coefficient = 0.19
                    case 'C':
                        coefficient = 0.34
                    case 'D':
                        coefficient = 0.43
        case 4:
            coefficient = 0.95
        case 5:
            coefficient = 0.05

    nouveauSol = [vegetation, pente, classHydro, pourcentageSol]
    sols.append(nouveauSol)
    pourcentageRestant -= pourcentageSol
    print("********** Sol #" + str(nombreSols) + " ajouté au calcul **********")
    print_reponses(None, vegetation, pente, classHydro, pourcentageSol, True)
    if pourcentageRestant <= 0:
        break

print("Caalcuuuuul")

