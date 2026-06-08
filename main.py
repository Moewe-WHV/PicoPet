from PicoPet.dino import Dino

def main():
    """Startet das Spiel."""
    
    name = input("Gib deinem Pet einen Namen: ")
    dino = Dino(0, 0, 0, 0, 100, 0, name=name )
    
    print(f"\n\nDein Pet heißt: {dino.name}")
    print(f"Alter: {dino.alter}")
    print("-" * 20)
    print(f"Gesundheit: {dino.gesundheit}")
    print(f"Hunger: {dino.hunger}")
    print(f"Müdigkeit: {dino.muedigkeit}")
    print(f"Langeweile: {dino.langeweile}")
    print(f"Dreck: {dino.dreck}")

    

if __name__ == "__main__":
    main()