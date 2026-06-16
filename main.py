from PicoPet.dino import Dino
import json
import os

def main():
    """Startet das Spiel, lädt ein vorhandenes Savegame oder erstellt ein neues Pet und speichert den Zustand."""


    if os.path.exists("savegame.json"): 
        with open("savegame.json", "r") as sg:
            data = json.load(sg)
            dino = Dino(data["hunger"], data["muedigkeit"], data["langeweile"], data["dreck"], data["gesundheit"], data["alter"], data["name"])
    else: 
        name = input("Wie soll dein Pet heißen?\n")
        dino = Dino(0, 0, 0, 0, 100, 0, name = name)
    
    laeuft = True
    while laeuft:
        print(
            "\nWas möchtest du tun?\n"
            "  füttern  - stillt den Hunger (macht etwas dreckig)\n"
            "  spielen  - vertreibt die Langeweile (macht hungrig und müde)\n"
            "  schlafen - nimmt die Müdigkeit (macht hungrig)\n"
            "  putzen   - entfernt den Dreck\n"
            "  status   - zeigt die Werte\n"
            "  Ende     - speichern und beenden"
        )
        eingabe = input("> ").strip().lower()

        if eingabe == "füttern":
            dino.fuettern()
            print(dino.fressen_text)
        elif eingabe == "spielen":
            dino.spielen()
            print(dino.spielen_text)
        elif eingabe == "schlafen":
            dino.schlafen()
            print(dino.schlafen_text)
        elif eingabe == "putzen":
            dino.putzen()
            print(dino.putzen_text)
        elif eingabe == "status":
            print(
                f"{dino.name}: Hunger {dino.hunger}, Müdigkeit {dino.muedigkeit}, "
                f"Langeweile {dino.langeweile}, Dreck {dino.dreck}, "
                f"Gesundheit {dino.gesundheit}, Alter {dino.alter}"
            )
        elif eingabe == "ende":
            laeuft = False
        else:
            print("Das verstehe ich nicht.")

    daten = {"hunger": dino.hunger,
             "muedigkeit": dino.muedigkeit,
             "langeweile": dino.langeweile,
             "dreck": dino.dreck,
             "gesundheit": dino.gesundheit,
             "alter": dino.alter,
             "name": dino.name
            }
    with open("savegame.json", "w") as sg:
        json.dump(daten, sg)
if __name__ == "__main__":
    main()