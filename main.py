from PicoPet.dino import Dino

def main():
    """Startet das Spiel."""
    
    name = input("Gib deinem Pet einen Namen: ")
    dino = Dino(0, 0, 0, 0, 100, name=name)
    
    print(f"Dein Pet heißt: {dino.name}")
    print(f"Hunger: {dino.hunger_punkte_wert}")
    print(f"Müdigkeit: {dino.muedigkeit_punkte_wert}")
    print(f"Langeweile: {dino.langeweile_punkte_wert}")
    print(f"Dreck: {dino.dreck_punkte_wert}")
    print(f"Gesundheit: {dino.gesundheit_punkte_wert}")

if __name__ == "__main__":
    main()
