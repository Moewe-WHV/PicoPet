from unittest.mock import patch

def test_startwerte_werden_gesetzt():
    from base import Beduerfnisse
    with patch("base.threading.Timer"):
        pet = Beduerfnisse(10, 20, 30, 40, 80)
    assert pet.hunger_punkte_wert == 10