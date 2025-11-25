def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible !"
    return a / b

def calculatrice():
    print("=== Calculatrice Python ===")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Quitter")

    while True:
        choix = input("\nChoisissez une opération : ")

        if choix == "0":
            print("Merci d'avoir utilisé la calculatrice.")
            break

        if choix not in ["1", "2", "3", "4"]:
            print("Choix invalide, réessayez.")
            continue

        try:
            a = float(input("Entrez le premier nombre : "))
            b = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : veuillez entrer des nombres valides.")
            continue

        if choix == "1":
            print("Résultat :", addition(a, b))
        elif choix == "2":
            print("Résultat :", soustraction(a, b))
        elif choix == "3":
            print("Résultat :", multiplication(a, b))
        elif choix == "4":
            print("Résultat :", division(a, b))


# Lancement du programme
calculatrice()
