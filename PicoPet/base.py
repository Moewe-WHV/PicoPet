import threading 
from config import Werte
import os

class Beduerfnisse: 
    """Verwaltet die Bedürfnisse eines Tamagotchi-Tieres (Hunger, Dreck, Müdigkeit, Freude).
        Alle Werte steigen automatisch alle 12 Minuten um 5 Punkte.
        Bei einem Wert von 70 oder höher wird eine Warnung ausgegeben."""

    def __init__(self, hunger, muedigkeit, langeweile, dreck, gesundheit, alter, name):
        """Initialisiert die Bedürfniswerte, Gesundheitswerte und startet die automatischen Timer.
                Args:
                    hunger: Anfangswert für Hunger (0–100).
                    dreck: Anfangswert für Verschmutzung (0–100).
                    muedigkeit: Anfangswert für Müdigkeit (0–100).
                    langeweile: Anfangswert für Langeweile (0–100)
                    gesundheit: Anfangswert für Gesundheit (0-100)"""          
        
        self.__gesundheit = gesundheit
        self.__alter = alter
        self.__name = name
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
        timer = threading.Timer(Werte.threading_werte, self.beduerfnisse_steigen)
        timer.start()
        timer_alter = threading.Timer(Werte.threading_alter, self.alter_steigt)
        timer_alter.start()
# Bedürfnisse       
    def beduerfnisse_steigen(self):
        """Erhöht alle Bedürfniswerte beinhaltet Gesundheitlogik und den Timer."""
# Bedürfniss
        for etikett in self.__beduerfnisse:
            self.__beduerfnisse[etikett]["wert"] += Werte.bedüfniss_sinkt_um_wert
            if self.__beduerfnisse[etikett]["wert"] >= Werte.kritischer_beduerfniss_wert:
                self.__beduerfnisse[etikett]["runden_ueber_80"] += 1
                print(self.__beduerfnisse[etikett]["nachricht"])   
# Kritischer Bereich
            if self.__beduerfnisse[etikett]["runden_ueber_80"] >= Werte.kritische_beduerfniss_runden: 
                self.__gesundheit -= Werte.gesundheits_abzug
            elif self.__beduerfnisse[etikett]["wert"]  < Werte.kritischer_beduerfniss_wert:
                self.__beduerfnisse[etikett]["runden_ueber_80"] = 0  
# Gesundheit
        if self.__gesundheit > 0:
            timer = threading.Timer(Werte.threading_werte, self.beduerfnisse_steigen)
            timer.start()      
        elif self.__gesundheit <= 0:
            print(f"{self.__name} ist im Alter von {self.__alter} gestorben.")
            if os.path.exists("savegame.json"):
                os.remove("savegame.json")# <- JSON wird gelöscht
        if 0 < self.__gesundheit <= 20:
            print("Ich werde krank")
# Altern 
    def alter_steigt(self):
        """Erhöht das Alter um 1 und startet den Timer für den nächsten Schritt."""
        if self.__alter >= 0:
            self.__alter += 1
            timer = threading.Timer(Werte.threading_alter, self.alter_steigt)
            timer.start()  
# Propertys
## Hunger
    @property 
    def hunger(self):
        """Gibt den aktuellen Hungerwert zurück."""
        return self.__beduerfnisse["hunger"]["wert"]
    @hunger.setter
    def hunger(self, wert): 
        self.__beduerfnisse["hunger"]["wert"] = wert   
## Müdigkeit 
    @property 
    def muedigkeit(self):
        """Gibt den aktuellen Müdigkeitswert zurück."""
        return self.__beduerfnisse["muedigkeit"]["wert"]  
## Langeweile
    @muedigkeit.setter
    def muedigkeit(self, wert): 
        self.__beduerfnisse["muedigkeit"]["wert"] = wert   
    @property 
    def langeweile(self):
        """Gibt den aktuellen Langeweilewert zurück."""            
        return self.__beduerfnisse["langeweile"]["wert"]
    @langeweile.setter
    def langeweile(self, wert): 
        self.__beduerfnisse["langeweile"]["wert"] = wert  
## Dreck
    @property 
    def dreck(self):
        """Gibt den aktuellen Dreckwert zurück."""
        return self.__beduerfnisse["dreck"]["wert"]
    @dreck.setter
    def dreck(self, wert): 
        self.__beduerfnisse["dreck"]["wert"] = wert
## Gesundheit
    @property 
    def gesundheit(self):
        """Gibt den aktuellen Gesundheitswert zurück."""
        return self.__gesundheit
    @gesundheit.setter
    def gesundheit(self, wert): 
        self.__gesundheit = wert
## Name
    @property 
    def name(self):
        """Gibt den aktuellen Namen zurück."""
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
## Alter
    @property 
    def alter(self):
        """Gibt das aktuelle Alter zurück."""
        return self.__alter
    @alter.setter
    def alter(self, wert):
        self.__alter = wert