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
        eingabe = input("Was möchtest du tun?")
        if eingabe == "Ende": 
            laeuft = False
            daten = {"hunger": dino.hunger, 
             "muedigkeit": dino.muedigkeit , 
             "langeweile": dino.langeweile, 
             "dreck": dino.dreck, 
             "gesundheit": dino.gesundheit, 
             "alter": dino.alter, 
             "name": dino.name 
            }
        
    print(f"\n\nDein Pet heißt: {dino.name}")
    print(f"Alter: {dino.alter}")
    print("-" * 20)
    
    with open("savegame.json", "w") as sg: 
        json.dump(daten, sg)
if __name__ == "__main__":
    main()
    
    
    