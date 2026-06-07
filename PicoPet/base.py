import threading 

class Beduerfnisse: 
    """ Verwaltet die Bedürfnisse eines Tamagotchi-Tieres (Hunger, Dreck, Müdigkeit, Freude).
        Alle Werte steigen automatisch alle 12 Minuten um 5 Punkte.
        Bei einem Wert von 70 oder höher wird eine Warnung ausgegeben. """
    
    def __init__(self, hunger, muedigkeit, langeweile, dreck):
        """ Initialisiert die Bedürfniswerte und startet die automatischen Timer.
        Args:
            hunger: Anfangswert für Hunger (0–100).
            dreck: Anfangswert für Verschmutzung (0–100).
            muedigkeit: Anfangswert für Müdigkeit (0–100).
            langeweile: Anfangswert für Langeweile (0–100, hoher Wert = gelangweilt). """
            
        self.__beduerfnisse = {
            "hunger":{
                "wert": hunger, 
                "nachricht": "Ich habe hunger!"
            },
            "muedigkeit": {
                "wert": muedigkeit, 
                "nachricht": "Ich bin müde!"
            },
            "langeweile":{
                "wert": langeweile, 
                "nachricht": "Mir ist langweilig"
            },
            "dreck":{
                "wert": dreck,
                "nachricht": "Ich bin dreckig"
            }
        }
        timer = threading.Timer(720.0, self.beduerfnisse_steigen)
        timer.start()
        
    def beduerfnisse_steigen(self):
        """ Erhöht alle Bedürfniswerte um 5 und startet den Timer neu. """
        for etikett in self.__beduerfnisse:
            self.__beduerfnisse[etikett]["wert"] += 5
            if self.__beduerfnisse[etikett]["wert"] >= 70:
                print(self.__beduerfnisse[etikett]["nachricht"])
        timer = threading.Timer(720.0, self.beduerfnisse_steigen)
        timer.start()
        
    @property
    def hunger_punkte_wert(self):
        return self.__beduerfnisse["hunger"]["wert"]
    @hunger_punkte_wert.setter
    def hunger_punkte_wert(self, wert): 
        self.__beduerfnisse["hunger"]["wert"] = wert

    @property
    def muedigkeit_punkte_wert(self):
        return self.__beduerfnisse["muedigkeit"]["wert"]
    @muedigkeit_punkte_wert.setter
    def muedigkeit_punkte_wert(self, wert): 
        self.__beduerfnisse["muedigkeit"]["wert"] = wert
        
    @property
    def langeweile_punkte_wert(self):
        return self.__beduerfnisse["langeweile"]["wert"]
    @langeweile_punkte_wert.setter
    def langeweile_punkte_wert(self, wert): 
        self.__beduerfnisse["langeweile"]["wert"] = wert
        
    @property
    def dreck_punkte_wert(self):
        return self.__beduerfnisse["dreck"]["wert"]
    @dreck_punkte_wert.setter
    def dreck_punkte_wert(self, wert): 
        self.__beduerfnisse["dreck"]["wert"] = wert
        

