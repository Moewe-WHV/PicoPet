# 🦕 PicoPet

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
git clone https://github.com/Moewe-WHV/PicoPet.git

# In den Projektordner wechseln
cd PicoPet

# Spiel starten
python main.py
```

---

## 📁 Projektstruktur

```
PicoPet/                     # Root
├── main.py                  # Einstiegspunkt
├── config.py                # Zentrale Spielwerte (keine Magic Numbers)
├── conftest.py              # pytest Pfad-Konfiguration
├── PicoPet/                 # Kern-Paket
│   ├── __init__.py
│   ├── base.py              # Basisklasse (Bedürfnisse, Gesundheit, Timer)
│   └── dino.py              # Dino-Subklasse
├── gui/                     # GUI-Paket (in Entwicklung)
│   └── __init__.py
├── data/                    # Persistenz (in Entwicklung)
│   └── __init__.py
├── tests/                   # pytest Unittests
│   └── test_tamagotchi.py
├── docs/                    # Projektdokumentation
│   ├── Klassendiagramm_PicoPet.mmd
│   ├── Entwickler_Use_Case.png
│   ├── Spieler_Use_Case.png
│   ├── Lastenheft.md
│   └── Tamagotchi.pdf
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

- [x] Projektstruktur aufgesetzt
- [x] config.py – zentrale Spielwerte
- [x] Basisklasse `Beduerfnisse` mit Threading & Gesundheitslogik
- [x] Dino-Subklasse
- [ ] Vogel-Subklasse
- [ ] tkinter GUI (`app.py`)
- [ ] Spielstand speichern/laden (JSON)
- [ ] Unittests grün

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
