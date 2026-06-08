import threading 
from config import Werte

class Beduerfnisse: 
    """Verwaltet die Bedürfnisse eines Tamagotchi-Tieres (Hunger, Dreck, Müdigkeit, Freude).
        Alle Werte steigen automatisch alle 12 Minuten um 5 Punkte.
        Bei einem Wert von 70 oder höher wird eine Warnung ausgegeben."""
    
    def __init__(self, hunger, muedigkeit, langeweile, dreck, gesundheit):
        """Initialisiert die Bedürfniswerte, Gesundheitswerte und startet die automatischen Timer.
                Args:
                    hunger: Anfangswert für Hunger (0–100).
                    dreck: Anfangswert für Verschmutzung (0–100).
                    muedigkeit: Anfangswert für Müdigkeit (0–100).
                    langeweile: Anfangswert für Langeweile (0–100, hoher Wert = gelangweilt)."""          
        
        self.__gesundheit = gesundheit
        self.__beduerfnisse = {
            "hunger":{
                "wert": hunger, 
                "nachricht": "Ich habe hunger!", 
                "runden_ueber_80": 0
            },
            "muedigkeit": {
                "wert": muedigkeit, 
                "nachricht": "Ich bin müde!",
                "runden_ueber_80": 0
            },
            "langeweile":{
                "wert": langeweile, 
                "nachricht": "Mir ist langweilig",
                "runden_ueber_80": 0
            },
            "dreck":{
                "wert": dreck,
                "nachricht": "Ich bin dreckig",
                "runden_ueber_80": 0
            }
        }

        timer = threading.Timer(Werte.threading_ticker, self.beduerfnisse_steigen)
        timer.start()
        
    def beduerfnisse_steigen(self):
        """Erhöht alle Bedürfniswerte beinhaltet Gesundheitlogik und den Timer."""
        
        for etikett in self.__beduerfnisse:
            self.__beduerfnisse[etikett]["wert"] += Werte.bedüfniss_sinkt_um_wert
            
            if self.__beduerfnisse[etikett]["wert"] >= Werte.kritischer_beduerfniss_wert:
                self.__beduerfnisse[etikett]["runden_ueber_80"] += 1
                print(self.__beduerfnisse[etikett]["nachricht"])   
            
            if self.__beduerfnisse[etikett]["runden_ueber_80"] >= Werte.kritische_beduerfniss_runden: 
                self.__gesundheit -= Werte.gesundheits_abzug
            elif self.__beduerfnisse[etikett]["wert"]  < Werte.kritischer_beduerfniss_wert:
                self.__beduerfnisse[etikett]["runden_ueber_80"] = 0  
        
        if self.__gesundheit > 0:
            timer = threading.Timer(Werte.threading_ticker, self.beduerfnisse_steigen)
            timer.start()          
        elif self.__gesundheit < 20:
            print("Ich werde Krank") 
        if self.__gesundheit <= 0:
            print("Dein Pet ist gestorben!!!!")
            
    @property # Hunger
    def hunger_punkte_wert(self):
        """Gibt den aktuellen Hungerwert zurück."""
        return self.__beduerfnisse["hunger"]["wert"]
    @hunger_punkte_wert.setter
    def hunger_punkte_wert(self, wert): 
        self.__beduerfnisse["hunger"]["wert"] = wert     
    @property # Müdigkeit
    def muedigkeit_punkte_wert(self):
        """Gibt den aktuellen Müdigkeitswert zurück."""
        return self.__beduerfnisse["muedigkeit"]["wert"]  
    @muedigkeit_punkte_wert.setter
    def muedigkeit_punkte_wert(self, wert): 
        self.__beduerfnisse["muedigkeit"]["wert"] = wert   
    @property # Langeweile
    def langeweile_punkte_wert(self):
        """Gibt den aktuellen Langeweilewert zurück."""            
        return self.__beduerfnisse["langeweile"]["wert"]
    @langeweile_punkte_wert.setter
    def langeweile_punkte_wert(self, wert): 
        self.__beduerfnisse["langeweile"]["wert"] = wert           
    @property # Dreck
    def dreck_punkte_wert(self):
        """Gibt den aktuellen Dreckwert zurück."""
        return self.__beduerfnisse["dreck"]["wert"]
    @dreck_punkte_wert.setter
    def dreck_punkte_wert(self, wert): 
        self.__beduerfnisse["dreck"]["wert"] = wert
    @property # Gesundheit
    def gesundheit_punkte_wert(self):
        """Gibt den aktuellen Gesundheitswert zurück."""
        return self.__gesundheit
    @gesundheit_punkte_wert.setter
    def gesundheit_punkte_wert(self, wert): 
        self.__gesundheit = wert
