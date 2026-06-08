from PicoPet.dino import Dino 

dino = Dino(0,0,0,0,100)

def main():
    """Startet das Spiel."""
    #Gui()
    pass
    
if __name__ == "__main__":
    print(f"Hunger: {dino.hunger_punkte_wert}")
    print(f"Müdigkeit: {dino.muedigkeit_punkte_wert}")
    print(f"Langeweile: {dino.langeweile_punkte_wert}")
    print(f"Dreck: {dino.dreck_punkte_wert}")
    print(f"Gesundheit: {dino.gesundheit_punkte_wert}")
    main()
