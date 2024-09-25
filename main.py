sols = []
typesVegetation = ["Culture", "Pâturage", "Boisé", "Lac", "Marécage"]
nombreSols = 0

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

while True:
    vegetation = None
    pente = None
    classHydro = None
    pourcentageSol = None
    # Numéro du sol
    nombreSols += 1
    print("********** Sol " + str(nombreSols) + " **********")

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
        # Classification Hydrologique
        while True:
            classHydro = input("Quelle est la classification hydraulique du sol: ")
            if classHydro.upper() not in ["A", "B", "C", "D"]:
                print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
                continue
            break

    # Pourcentage de l'aire totale occupée par ce sol
    while True:
        pourcentageSol = input("Quel pourcentage de l'aire totale occupe ce sol: ")
        try:
            pourcentageSol = float(pourcentageSol)
            if not 0 < pourcentageSol <= 100:
                raise Exception
            break
        except Exception:
            print("\nNOPE, PAS UNE OPTION!\nRÉESSAYE DUMBASS\n")
            continue

    nouveauSol = [vegetation, pente, classHydro, pourcentageSol]
    sols.append(nouveauSol)
    if pente is None:
        pente = "N/A"
    if classHydro is None:
        classHydro = "N/A"
    print("Nouveau sol ajouté:\n"
          "Végétation: " + typesVegetation[vegetation - 1] + "\n"
          "Pente: " + str(pente) + "\n"
          "Classification Hydrologique: " + str(classHydro) + "\n"
          "Pourcentage du sol: " + str(pourcentageSol))
    print(sols)
