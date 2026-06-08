from PicoPet.base import Beduerfnisse

class Dino(Beduerfnisse):
    def __init__(self, hunger, muedigkeit, langeweile, dreck, gesundheit):
        """Erstellt einen neuen Dino mit den angegebenen Startwerten."""
        super().__init__(hunger, dreck, muedigkeit, langeweile, gesundheit)
        self.laut_geben = "Rawr"
        self.bewegen = "Läuft umher."
        self.spielen = "Sucht den Ball und bringt in dir."
        self.fressen = "Frisst ein fettes Stück Fleich"