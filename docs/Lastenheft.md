# Lastenheft – Tamagotchi Desktop-Anwendung

| Feld | Inhalt |
| --- | --- |
| **Auftraggeber** | PixelPet GmbH, Hamburg |
| **Auftragnehmer** | Tim K. |
| **Datum** | 04.06.2026 |
| **Version** | 0.1 |
| **Status** | In Abstimmung |

---

## Inhaltsverzeichnis

1. Ausgangssituation
2. Projektziel
3. Zielgruppe
4. Anforderungen
5. Nicht-Ziele
6. Technische Rahmenbedingungen
7. Spielkonzept
8. Bekannte Risiken
9. Liefergegenstände
10. Versionsverlauf

---

## 1. Ausgangssituation

Die PixelPet GmbH möchte ein eigenständiges Desktop-Spiel entwickeln lassen, das das Konzept klassischer Tamagotchi-Handhelds aus den 1990er Jahren als moderne PC-Anwendung neu interpretiert. Das Produkt soll als lauffähige Grundversion ausgeliefert werden und als Basis für spätere Erweiterungen dienen.

Der Auftraggeber verfügt über kein eigenes Entwicklungsteam und beauftragt die Umsetzung extern.

---

## 2. Projektziel

Entwicklung einer stabilen Desktop-Anwendung, in der der Nutzer ein virtuelles Haustier (Tamagotchi) pflegen, füttern und bespielen kann. Das Haustier reagiert auf Vernachlässigung mit sinkenden Statuswerten und stirbt bei vollständiger Vernachlässigung.

Die Anwendung soll intuitiv bedienbar sein und ohne technische Vorkenntnisse genutzt werden können.

---

## 3. Zielgruppe

| Nutzergruppe | Beschreibung |
| --- | --- |
| Hauptzielgruppe | Kinder und Jugendliche (8–16 Jahre) |
| Sekundärzielgruppe | Nostalgisch interessierte Erwachsene (25–40 Jahre) |
| Betriebssystem | Windows 10/11, macOS |

---

## 4. Anforderungen

### 4.1 Funktionale Anforderungen

| ID | Anforderung |
| --- | --- |
| FA-01 | Der Nutzer kann ein neues Tamagotchi erstellen und benennen |
| FA-02 | Das Tamagotchi besitzt Statuswerte: Hunger, Müdigkeit, Hygiene, Langeweile, Gesundheit |
| FA-03 | Der Nutzer kann das Tamagotchi füttern, schlafen legen, waschen, bespielen und heilen |
| FA-04 | Statuswerte sinken automatisch mit der Zeit |
| FA-05 | Bei kritischen Werten erhält der Nutzer eine Warnanzeige |
| FA-06 | Das Tamagotchi stirbt bei Gesundheit = 0; Todesursache wird angezeigt |
| FA-07 | Nach dem Tod kann ein Neustart erfolgen |
| FA-08 | Der Spielstand wird beim Beenden automatisch gespeichert und beim Start geladen |
| FA-09 | Das Tamagotchi durchläuft mindestens drei Entwicklungsstufen (Baby → Kind → Erwachsener) |
| FA-10 | Das Spiel kann pausiert und fortgesetzt werden |

### 4.2 Nicht-funktionale Anforderungen

| ID | Anforderung |
| --- | --- |
| NFA-01 | Die Anwendung startet in unter 5 Sekunden |
| NFA-02 | Die Benutzeroberfläche ist auf Deutsch |
| NFA-03 | Die Steuerung erfolgt ausschließlich per Maus und Tastatur |
| NFA-04 | Der Quellcode ist modular und wartbar strukturiert |
| NFA-05 | Die Anwendung stürzt bei einem beschädigten Spielstand nicht ab |

---

## 5. Nicht-Ziele

Folgende Features sind ausdrücklich **nicht** Bestandteil der beauftragten Grundversion:

- Multiplayer- oder Online-Funktionen
- Ingame-Shop oder Währungssystem
- KI-gesteuerte Verhaltenslogik
- Mobile- oder Browserversion

---

## 6. Technische Rahmenbedingungen

| Bereich | Vorgabe |
| --- | --- |
| Programmiersprache | Python |
| Benutzeroberfläche | `tkinter` |
| Zeitmechanik | `threading` |
| Persistenz | JSON-Datei (lokales Speichern) |
| Versionskontrolle | Git / GitHub |

---

## 7. Spielkonzept

### 7.1 Verfügbare Tiertypen (Grundversion)

| Typ | Bewegung | Charakterlaut |
| --- | --- | --- |
| Dino | Laufen | „Rawr" |
| Vogel | Fliegen | „Pieps" |

### 7.2 Statuswerte und Aktionen

| Aktion | Betroffener Wert | Änderung |
| --- | --- | --- |
| Füttern | Hunger | +20 |
| Schlafen legen | Müdigkeit | +50 |
| Waschen | Hygiene | +25 |
| Spielen | Langeweile | +50 |
| Heilen | Gesundheit | +50 |

### 7.3 Zeitbasierte Mechanik

- Alle Statuswerte sinken alle **900 Sekunden** um `5`
- Warnhinweis bei einem Wert ≥ 70 (kritischer Bereich)
- Tod bei Gesundheit = 0

---

## 8. Bekannte Risiken

| Bereich | Risiko | Einschätzung |
| --- | --- | --- |
| Balancing | Werte- und Zeitbalancing schwer vorab kalkulierbar | Mittel |
| Bibliotheken | `tkinter` und `threading` können plattformabhängig abweichen | Mittel |
| Persistenz | Spielstand-Speicherung in frühen Versionen noch nicht stabil | Hoch |
| Scope | Wachsende Anforderungen könnten Grundversion verzögern | Niedrig |

---

## 9. Liefergegenstände

| Gegenstand | Beschreibung |
| --- | --- |
| Quellcode | Vollständiger, kommentierter Python-Quellcode auf GitHub |
| Dokumentation | Projektdokumentation inkl. Pflichtenheft, Diagramme, Testprotokolle |
| Ausführbare Anwendung | Lauffähige Version für Windows und/oder macOS |
| README | Installations- und Bedienungsanleitung auf GitHub |

---

## 10. Versionsverlauf

| Version | Datum | Änderung |
| --- | --- | --- |
| 0.1 | 04.06.2026 | Erstversion des Lastenhefts |

---

*Dieses Lastenheft wurde im Rahmen eines Lernprojekts der Umschulung zum Fachinformatiker Anwendungsentwicklung (FIAE) an der IBB Wilhelmshaven erstellt. Der Auftraggeber „PixelPet GmbH" ist fiktiv.*