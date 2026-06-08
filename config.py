class Werte:
    """Hier sind Zeiten und Werte definiert. Keine Magic Numbers.
        Args: 
            threading_ticker: Die Zeit in der die Bedürfnisse sinken
            kritischer_wert: Ab dem Wert wirken Bedürfnisse auf Gesundheit
            bedürfniss_sinkt_um_wert: Um Diesen Wert sinken die Bedüftnisse 
            Kritische_beduerfniss_runden: Durchläufe Bleiben bis das Pet stirbt
            gesundheits_abzug: Um diesen Wert sinkt die Gesundheit nach Kritischen Bedürfnisse"""
    threading_ticker = 720.0
    kritischer_beduerfniss_wert = 75
    bedüfniss_sinkt_um_wert = 5
    kritische_beduerfniss_runden = 5
    gesundheits_abzug = 20