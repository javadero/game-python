import random

def raad_het_getal():
    te_raden_getal = random.randint(1, 100)
    pogingen = 0
    print("Welkom bij het spel 'Raad het Getal'!")
    print("Ik heb een getal gekozen tussen 1 en 100.")
    
    while True:
        try:
            gok = int(input("Voer je gok in: "))
            pogingen += 1
            if gok < te_raden_getal:
                print("Te laag! Probeer het opnieuw.")
            elif gok > te_raden_getal:
                print("Te hoog! Probeer het opnieuw.")
            else:
                print(f"Gefeliciteerd! Je hebt het getal {te_raden_getal} geraden in {pogingen} pogingen.")
                break
        except ValueError:
            print("Voer alstublieft een geldig getal in.")
raad_het_getal()