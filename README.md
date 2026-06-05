# 🦕 Tamagotchi

Ein textbasiertes Tamagotchi-Spiel mit grafischer Oberfläche, entwickelt in Python.  
Lernprojekt im Rahmen der Umschulung zum Fachinformatiker Anwendungsentwicklung (FIAE).

---

## 📋 Projektübersicht

| | |
|---|---|
| **Version** | v0.1 (Entwicklungsversion) |
| **Sprache** | Python |
| **GUI** | tkinter |
| **Autor** | Tim K. |
| **Status** | 🚧 In Entwicklung |

---

## 🎮 Features

- Wähle dein Tamagotchi: **Dino** 🦕 oder **Vogel** 🐦
- Kümmere dich um Hunger, Müdigkeit, Hygiene, Langeweile und Gesundheit
- Werte sinken automatisch mit der Zeit – pass gut auf!
- Dein Tamagotchi kann krank werden und sterben 💀
- Spielstand wird automatisch gespeichert

---

## 🚀 Installation

### Voraussetzungen

- Python 3.10 oder höher
- pip

### Schritte

```bash
# Repository klonen
git clone https://github.com/DEIN-NAME/tamagotchi.git

# In den Projektordner wechseln
cd tamagotchi

# Abhängigkeiten installieren (falls vorhanden)
pip install -r requirements.txt

# Spiel starten
python main.py
```

---

## 📁 Projektstruktur

```
PicoPet/
├── main.py                  # Einstiegspunkt
├── config.py                # Zentrale Spielwerte
├── tamagotchi/
│   ├── __init__.py
│   ├── base.py              # Basisklasse Tamagotchi
│   ├── dino.py              # Dino-Klasse
│   └── vogel.py             # Vogel-Klasse
├── gui/
│   ├── __init__.py
│   └── app.py               # tkinter GUI
├── data/
│   └── save.json            # Spielstand (automatisch erstellt)
├── tests/
│   ├── __init__.py
│   └── test_tamagotchi.py   # pytest Unittests
├── docs/
│   ├── Klassendiagramm.png
│   ├── Tamagotchi.pdf
│   └── Lastenheft.md       
├── .gitignore
└── README.md
```

---

## 🧪 Tests ausführen

```bash
pytest tests/
```

---

## 🗺️ Roadmap

### Grundversion (v1.x)
- [x] Projektstruktur
- [ ] Tamagotchi Basisklasse
- [ ] Dino & Vogel
- [ ] tkinter GUI
- [ ] Zeitbasierter Werteverfall
- [ ] Spielstand speichern (JSON)
- [ ] Unittests

### Update (v2.x)
- [ ] Schlange als neues Tamagotchi
- [ ] Toilettengang
- [ ] Weitere Futterarten
- [ ] Gehäuseanpassungen
- [ ] Weitere Spielarten
---

## 📚 Lernziele

Dieses Projekt dient dem Erlernen und Anwenden von:

- **OOP** – Vererbung, Kapselung, Modularisierung
- **tkinter** – GUI-Entwicklung in Python
- **threading** – Zeitbasierte Mechaniken
- **pytest** – Automatisiertes Testing
- **Git/GitHub** – Versionskontrolle, Branches, Mergen
- **Clean Code** – Lesbarkeit, keine Magic Numbers

---

## 📄 Lizenz

Dieses Projekt ist ein privates Lernprojekt und nicht für den kommerziellen Einsatz bestimmt.
