# 🦕 PicoPet

> *"Ein virtuelles Tier am Leben zu erhalten ist einfacher als eine Pflanze zu gießen. Wahrscheinlich."*

---

## 📖 Das Projekt

PicoPet ist ein OOP-Projekt lernprojekt in Python, entstanden während der Umschulung zum Fachinformatiker.

**Die Challenge:** Ein virtuelles Haustier mit echten Bedürfnissen (Hunger, Dreck, Müdigkeit, Einsamkeit), das in Echtzeit wegstirbt, wenn man es ignoriert.

**Der Haken:** Null Copy-Paste, kein YouTube-Tutorial. Der Dozent; Claude liefert keine einzige Zeile Code, sondern schickt einen mit einem *"Lies bei Google nach und melde dich, wenn du fertig bist"* in die Wüste. Das hier ist pures, schmerzhaftes Lernen der OOP-Grundlagen. 🛠️

---

## 🎮 Features

* 🍖 **Hunger** — Sinkt stetig. Tier meckert, wenn der Magen knurrt.
* 🛁 **Sauberkeit** — Wer nicht wäscht, kriegt die Seuche (Krankheitsrisiko).
* 😴 **Müdigkeit** — Burnout-Gefahr für Pixeltiere.
* 💚 **Gefühl** — Ohne Liebe wird das Ding depressiv.
* ❤️ **Gesundheit** — Berechnet sich dynamisch aus allen vier Werten.
* ⏱️ **Echtzeit-Terror** — Dank `Threading` sinken die Werte im Hintergrund weiter. Immer.
* 🦕 **Artenschutz** — Dino und Vogel sind dank Vererbung schon am Start.

---

## 🏗️ Projektstruktur

```
PicoPet/
├── main.py                 # Einstiegspunkt, startet das Spiel
├── tamagotchi.py           # Kernklasse: Tamagotchi (Attribute, Methoden)
├── game_manager.py         # Spiellogik, Zeitmanagement, Status-Checks
├── save_manager.py         # Speichern & Laden (JSON)
├── gui.py                  # Grafische Oberfläche (tkinter)
├── actions.py              # Spieleraktionen: feed(), play(), sleep(), heal()
├── config.py               # Konstanten, Startwerte, Einstellungen
└── tests/
    ├── test_tamagotchi.py
    └── test_save_manager.py

```

> ⚠️ Struktur wächst. Stand: Erste Lebenszeichen vorhanden (Implementierung I fertig).

---

## 🧱 OOP-Konzepte im Einsatz

| Konzept | Wo es wehtut |
| --- | --- |
| **Kapselung** | `__hunger` & Co. sind privat. Wer ran will, muss an den Properties vorbei. |
| **Vererbung** | `Dino` und `Vogel` schnorren sich alles von `Tier` via `super().__init__()`. |
| **Polymorphie** | Jeder macht Krach, aber anders (`laut_geben()`). |
| **Properties** | `@property` und `@setter` regeln den kontrollierten Zugriff. |
| **Berechnete Property** | `zustand_gesundheit` wird on-the-fly berechnet. Kein Datenmüll. |

---

## 🚀 Starten statt Warten

```bash
# Code klauen
git clone https://github.com/TimKlein-WHV/PicoPet.git
cd PicoPet

# Starten (Nur Python 3.x nötig, kein externer Müll)
python main.py

```

---

## 🐾 Der Zoo

| Kreatur | Sound | Status |
| --- | --- | --- |
| 🦕 Dino | `"Rawr"` | ✅ Lebt |
| 🐦 Vogel | `"Pieps"` | ✅ Fliegt |
| Mehr Opfer... | — | 🔜 Geplant |

---

## 🗺️ Roadmap in den Wahnsinn

| Meilenstein | Fokus | Status | Zeit |
| --- | --- | --- | --- |
| **M1 — Core** | Klassen, Logik, Timer-Thread | ✅ Überlebt | ~19h |
| **M2 — Loop** | Save/Load & Game Loop | 🔜 Offen | — |
| **M3 — Optik** | Pixel Art (Damit man das Elend sieht) | 🔜 Offen | — |
| **M4 — Finale** | Polieren bis es glänzt | 🔜 Offen | — |

---

## 🛠️ Tech Stack

* **Sprache:** Python 3.x (Pure Standard-Library: `threading`, `time`)
* **Werkzeuge:** VS Code & Git

---

## 💡 Schmerztagebuch

Implementierung I hat statt 14 stolze 19 Stunden gefressen. 10 Stunden davon waren reines Verzweifeln, Googeln und Verstehen. Code schreiben dauerte nur 9 Stunden.

> *Das ist kein Bug. Das ist der Schmerz, wenn Wissen das Gehirn betritt.* 🌿

---

## 👤 Autor

Umschüler Fachinformatiker | IBB Wilhelmshaven | Start: Februar 2026
