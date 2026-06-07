from threading import Thread


class beduerfnisse: 
    def __init__(self, hunger, muedigkeit, langeweile, dreck):
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