from PicoPet.base import Beduerfnisse


class Dino(Beduerfnisse):
    """Tamagotchi-Tier vom Typ Dino.
        Erbt die komplette Bedürfnis- und Gesundheitslogik von Beduerfnisse
        und ergänzt nur die dino-typischen Rückmeldungstexte für die Aktionen."""

    def __init__(self, hunger, muedigkeit, langeweile, dreck, gesundheit, alter, name):
        """Erstellt einen neuen Dino mit den angegebenen Startwerten."""
        super().__init__(hunger, muedigkeit, langeweile, dreck, gesundheit, alter, name)
# Rückmeldungstexte für die Aktionen
        self.laut_geben_text = "Rawr"
        self.schlafen_text = "Kuschelt sich ein und schläft."
        self.spielen_text = "Sucht den Ball und bringt ihn dir."
        self.putzen_text = "Lässt sich genüsslich putzen."
        self.fressen_text = "Frisst ein fettes Stück Fleisch."