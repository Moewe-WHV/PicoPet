from PicoPet.dino import Dino
import json
import os

SPEICHERDATEI = "savegame.json"

MENUE = (
    "\nWas möchtest du tun?\n---------------------\n"
    "  füttern  - stillt den Hunger (macht etwas dreckig)\n"
    "  spielen  - vertreibt die Langeweile (macht hungrig und müde)\n"
    "  schlafen - nimmt die Müdigkeit (macht hungrig)\n"
    "  putzen   - entfernt den Dreck\n"
    "  status   - zeigt die Werte\n"
    "  Ende     - speichern und beenden"
)


def spiel_laden():
    """Lädt ein vorhandenes Savegame oder erstellt ein neues Pet."""
    if os.path.exists(SPEICHERDATEI):
        with open(SPEICHERDATEI, "r") as sg:
            data = json.load(sg)
        return Dino(data["hunger"], data["muedigkeit"], data["langeweile"],
                    data["dreck"], data["gesundheit"], data["alter"], data["name"])
    name = input("Wie soll dein Pet heißen?\n")
    return Dino(0, 0, 0, 0, 100, 0, name=name)


def spiel_speichern(dino):
    """Schreibt den aktuellen Zustand des Pets in die Speicherdatei."""
    daten = {
        "hunger": dino.hunger,
        "muedigkeit": dino.muedigkeit,
        "langeweile": dino.langeweile,
        "dreck": dino.dreck,
        "gesundheit": dino.gesundheit,
        "alter": dino.alter,
        "name": dino.name,
    }
    with open(SPEICHERDATEI, "w") as sg:
        json.dump(daten, sg)


def status_anzeigen(dino):
    """Zeigt die aktuellen Werte des Pets an."""
    print(
        f"{dino.name}: Hunger {dino.hunger}, Müdigkeit {dino.muedigkeit}, "
        f"Langeweile {dino.langeweile}, Dreck {dino.dreck}, "
        f"Gesundheit {dino.gesundheit}, Alter {dino.alter}"
    )


def aktion_ausfuehren(dino, methode, text):
    """Führt eine Pet-Aktion aus und gibt die zugehörige Rückmeldung aus."""
    methode(dino)
    print(text)


def main():
    """Startet das Spiel, verarbeitet Eingaben und speichert beim Beenden."""
    dino = spiel_laden()

    aktionen = {
        "füttern": lambda: aktion_ausfuehren(dino, Dino.fuettern, dino.fressen_text),
        "spielen": lambda: aktion_ausfuehren(dino, Dino.spielen, dino.spielen_text),
        "schlafen": lambda: aktion_ausfuehren(dino, Dino.schlafen, dino.schlafen_text),
        "putzen": lambda: aktion_ausfuehren(dino, Dino.putzen, dino.putzen_text),
        "status": lambda: status_anzeigen(dino),
    }

    while True:
        print(MENUE)
        eingabe = input("> ").strip().lower()

        if eingabe == "ende":
            break
        elif eingabe in aktionen:
            aktionen[eingabe]()
        else:
            print("Unpassende Eingabe")

    spiel_speichern(dino)


if __name__ == "__main__":
    main()
