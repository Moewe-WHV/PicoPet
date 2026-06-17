# 🦕 PicoPet

Ein textbasiertes Tamagotchi-Spiel, gespielt über das Terminal, entwickelt in Python.  
Eine grafische Oberfläche (tkinter) ist in Planung.  
Lernprojekt im Rahmen der Umschulung zum Fachinformatiker Anwendungsentwicklung (FIAE).

---

## 📋 Projektübersicht

| | |
|---|---|
| **Version** | v0.1 (Entwicklungsversion) |
| **Sprache** | Python |
| **Bedienung** | Terminal (Texteingabe) |
| **GUI** | tkinter (geplant) |
| **Autor** | Tim K. |
| **Status** | 🚧 In Entwicklung |

---

## 🎮 Features

- Kümmere dich um deinen **Dino** 🦕 (weitere Tiere wie Vogel 🐦 sind geplant)
- Halte Hunger, Müdigkeit, Langeweile, Dreck und Gesundheit im Blick
- Bedürfnisse steigen automatisch mit der Zeit – pass gut auf!
- Bei dauerhaft vernachlässigten Bedürfnissen wird dein Tamagotchi krank und kann sterben 💀 (das Savegame wird dann gelöscht)
- Spielstand wird beim Beenden automatisch gespeichert und beim Start geladen (`savegame.json`)

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

## 🕹️ Steuerung

Beim ersten Start vergibst du einen Namen für dein Pet. Danach steuerst du das Spiel
über folgende Texteingaben:

| Befehl     | Wirkung |
|------------|---------|
| `füttern`  | stillt den Hunger (macht etwas dreckig) |
| `spielen`  | vertreibt die Langeweile (macht hungrig und müde) |
| `schlafen` | nimmt die Müdigkeit (macht hungrig) |
| `putzen`   | entfernt den Dreck |
| `status`   | zeigt die aktuellen Werte |
| `ende`     | speichert und beendet das Spiel |

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


## 🗺️ Roadmap

### Grundversion (v1.x)

- [x] Projektstruktur aufgesetzt
- [x] config.py – zentrale Spielwerte
- [x] Basisklasse `Beduerfnisse` mit Threading & Gesundheitslogik
- [x] Dino-Subklasse
- [x] Spielstand speichern/laden (JSON)
- [x] Textbasierte Steuerung im Terminal (`main.py`)
- [ ] tkinter GUI (`app.py`)
- [ ] Unittests grün

### Update (v2.x)

- [ ] Vogel als neues Tamagotchi
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
