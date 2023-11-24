import random

print("Stein-Papier-Schere\n")


while True:
    
    liste = ['Stein', 'Papier', 'Schere']
    
    meine_auswahl = input("Stein, Papier oder Schere? ").lower()

    computer_auswahl = (random.choice(liste))
    print(f"Computer: {computer_auswahl}\n")

    

    if meine_auswahl.lower() == computer_auswahl.lower():
            print("Unentschieden")
       
    if meine_auswahl == "Stein".lower() and computer_auswahl == "Schere":
        print("Du hast gewonnen.")
       
    if meine_auswahl == "Schere".lower() and computer_auswahl == "Stein":
        print("Du hast leider verloren.")
       
    if meine_auswahl == "Papier".lower() and computer_auswahl == "Stein":
        print("Du hast gewonnen.")
     
    if meine_auswahl == "Stein".lower() and computer_auswahl == "Papier":
        print("Du hast leider verloren.")
       
    if meine_auswahl == "Schere".lower() and computer_auswahl == "Papier":
        print("Du hast gewonnen.")
       
    if meine_auswahl == "Papier".lower() and computer_auswahl == "Schere":
        print("Du hast leider verloren")
       

    noch_eine_Runde = input("Noch eine Runde (ja/nein)? ").lower()

    if noch_eine_Runde != "ja".lower():
            print("Auf wiedersehen.")
            break
    

    

    