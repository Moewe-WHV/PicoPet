# Lastenheft – Tamagotchi (Grundversion v. 1.x)  

## **Autor:** Tim K.

**Datum:** 04.06.2026

**Version:** 0.1

**Projekttyp:** Lernprojekt / Umschulungsprojekt

---

## 1. Projektübersicht

Ziel dieses Projekts ist die Entwicklung eines textbasierten Tamagotchi-Spiels mit grafischer Oberfläche. Das Projekt dient gleichzeitig als Lernprojekt und als Nachweis für das Verständnis des Softwareentwicklungsprozesses im Rahmen der Umschulung.

---

## 2. Ziele

- Entwicklung einer lauffähigen Grundversion eines Tamagotchi-Spiels
- Dokumentation des gesamten Entwicklungsprozesses
- Anwendung von OOP, Modularisierung und Clean Code in Python
- Einsatz von Git/GitHub zur Versionskontrolle
- Nachweis von Projektmanagement-Kompetenzen (Kanban, User Stories, Versionsverlauf)

---

## 3. Nicht-Ziele (Wird nicht eingebaut)

Folgende Features sind bewusst **ausgeschlossen** und werden nicht Teil der Grundversion:

- Multiplayer-Funktionen
- Ingame-Shop
- KI-Integration
- Onlinefunktionen jeglicher Art

---

## 4. Zielgruppe / Nutzer

| Rolle | Beschreibung |
| --- | --- |
| Spieler | Nutzt das Spiel interaktiv über die GUI |
| Entwickler (Tim) | Entwickelt, testet und dokumentiert das Projekt |
| Prüfer | Bewertet den Entwicklungsprozess und die Umsetzung |

---

## 5. Technische Anforderungen

| Bereich | Details |
| --- | --- |
| Sprache | Python |
| Oberfläche | Eigenes Fenster via tkinter |
| Zeitmechanik | threading |
| Steuerung | Maus und Tastatur |
| Sprache (UI) | Deutsch |
| Tools | VS Code, Git, GitHub, Notion, Draw.io |

---

## 6. Tamagotchi-Typen (Grundversion)

| Typ | Bewegung | Laut |
| --- | --- | --- |
| Dino | Laufen | "Rawr" |
| Vogel | Fliegen | "Pieps" |

---

## 7. Spielmechanik

### 7.1 Bedürfnisse

| Bedürfnis | Beschreibung |
| --- | --- |
| Hunger | Sinkt mit der Zeit, steigt durch Füttern |
| Müdigkeit | Sinkt mit der Zeit, steigt durch Schlafen |
| Hygiene | Sinkt mit der Zeit, steigt durch Putzen |
| Langeweile | Sinkt mit der Zeit, steigt durch Spielen |
| Gesundheit | Sinkt bei Vernachlässigung, steigt durch Spritze |

### 7.2 Funktionen & Werte

| Funktion | Wertanstieg |
| --- | --- |
| Füttern | +20 |
| Schlafen legen | +50 |
| Putzen | +25 |
| Spielen | +50 |
| Spritze | +50 |

### 7.3 Zeitbasierte Mechanik

- Werte sinken **kontinuierlich** alle 900 Sekunden um -5
- Bei einem Bedürfniswert >= 70: Hinweisausgabe
- Bei Gesundheit = 0: Tamagotchi stirbt

---

## 8. User Stories (Grundversion)

### Spieler

| ID | Titel | Kurzbeschreibung |
| --- | --- | --- |
| US-01 | Tamagotchi erstellen | Name vergeben, Startwerte setzen, Anzeige nach Erstellung |
| US-02 | Füttern | Hungerwert steigt, Überfressen möglich, Hinweis bei vollem Hunger |
| US-03 | Spielen | Glückswert steigt, Energie/Hunger sinkt leicht |
| US-04 | Schlafen | Energie steigt, keine anderen Aktionen im Schlaf möglich |
| US-05 | Heilen | Nur bei Krankheit verfügbar, Gesundheitswert steigt |
| US-06 | Pflegen | Hygienewert steigt, niedriger Wert erhöht Krankheitsrisiko |
| US-07 | Statuswerte einsehen | Alle Werte jederzeit sichtbar, Aktualisierung nach jeder Aktion |
| US-08 | Alter sehen | Alter in Tagen, steigt automatisch, auch beim Tod sichtbar |
| US-10 | Tod | Tod bei Hunger oder Gesundheit = 0, Todesursache angezeigt |
| US-11 | Neustart | Nach Tod verfügbar, alle Werte zurückgesetzt, neuer Name möglich |
| US-12 | Kritische Werte | Warnung unter Schwellenwert, visuelle oder textliche Anzeige |

### Entwickler

| ID | Titel | Kurzbeschreibung |
| --- | --- | --- |
| US-16 | Spielstand speichern | Automatisch als JSON beim Beenden, laden beim Start |
| US-17 | Zeitbasierter Werteverfall | Intervalle und Raten zentral konfigurierbar |
| US-19 | Konfigurierbare Spielwerte | Keine Magic Numbers, Änderungen in Konfigurationsdatei |
| US-20 | Automatische Krankheit | Tritt bei Vernachlässigung auf, heilbar, sonst Tod |
| US-21 | Unittests | Tests für Kernlogik via pytest, müssen grün sein vor Merge |
| US-22 | Fehlerbehandlung | Korrupter Spielstand wird abgefangen, Programm startet neu |

---

## 9. Bekannte Risiken & Probleme

| Bereich | Problem |
| --- | --- |
| Coding | Zu volle Module, Dirty Code |
| Balancing | Zeit- und Wertebalancing schwer abzuschätzen |
| Funktionen | Funktionen könnten falsch implementiert oder fehlerhaft agieren |
| Bibliotheken | tkinter und threading können unerwartetes Verhalten zeigen |
| Persistenz | Keine funktionierende Persistenz in frühen Versionen |

---

## 10. Dokumentation & Tools

| Tool | Verwendungszweck |
| --- | --- |
| Notion | Dokumentation, Kanban, Projekt-Wiki |
| GitHub | Quellcode, Versionskontrolle |
| Draw.io | Diagramme (UML, Klassendiagramm, Anwendungsdiagramm) |
| VS Code | Entwicklung, Debugging, Testing |

---

## 11. Versionsverlauf

| Phase | Version | Beschreibung |
| --- | --- | --- |
| Entwicklung | v. 0.x | Entwicklungsversion, instabil |
| Grundversion | v. 1.x | Stabile Grundversion, nach erfolgreichem Testing |
| Release | – | Push auf main Branch, README anpassen, Präsentation |

---

## 12. Lernziele des Projekts

| Bereich | Themen |
| --- | --- |
| Projektmanagement | Kanban, User Stories, Zeitmanagement, Netzplan |
| Programmierung | OOP (Vererbung, Kapselung), Modularisierung, Clean Code |
| Bibliotheken | tkinter, threading |
| Git/GitHub | Versionskontrolle, Branches, Mergen, Push/Pull |
| Dokumentation | Schreiben, Verstehen, Zerlegen, Schätzung |

---