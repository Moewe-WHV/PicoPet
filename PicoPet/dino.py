from base import Beduerfnisse

class Dino(Beduerfnisse):
    def __init__(self, hunger, muedigkeit, langeweile, dreck, laut_geben, laufen):
        super().__init__(hunger, muedigkeit, langeweile, dreck)

        