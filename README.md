# GFN_Zeiterfassung

Mit diesem Programm kann die Zeiterfassung bei der GFN gestartet und beendet werden.
Eine weitere Funktion ist es, sich seine Anwesenheit anzeigen zu lassen (HomeOffice/VorOrt).

## Was wird benötigt?
- twill 3.3 
- selenium 4.26.1

Twill wird für die Prüfung der Anwesenheit benötigt.
Selenium wird für die Zeiterfassung benötigt.

# Wie stelle ich das Programm ein?
1. Öffnen der data.dat
2. Eintragen des Login-Name und Passwort
   
oder

1. Starten des Programms
2. 5 eingeben und Enter drücken, um in die Einstellungen zu kommn.
3. 4 Drücken und enter drücken, um die Login-Daten zu bearbeiten.
4. Anweisungen des Programms folgen.

## Wie funktioniert das Programm?
# Automatische Zeiterfassung
Die Automatische Zeiterfassung fragt am Anfang ab, ob man bereits angemeldet ist oder nicht.
Nach der Beantwortung liest das Programm aus einer der Dateien (t_in.dat oder t_out.dat) die Zeit aus, wo er die Zeiterfassung starten oder beenden soll.
Daraufhin prüft das Programm in der Datei day.dat ob es sich am heutigen Tag um ein HO (Home Office), VO (Vor Ort), F (Frei) handelt.

Jetzt läuft das Programm so lange, bis die Zeit erreicht wurde.
Es startet automatisch den ausgewählten Browser, meldet sich an, 
mit den hinterlegten Login-Daten und startet/beendet die Zeiterfassung.

# Manuelle Zeiterfassung starten/beenden
Liest die Login Daten aus, startet den Browser und startet/beendet die Zeiterfassung.

# Anwesenheit
Bei der Anwesenheit meldet Twill sich mit den hinterlegten Login-Daten ein.
Er Navigiert zu dem Anwesenheittab und lädt diese Temporer runter.
Jetzt wird die gesamte Datei Zeile für Zeile durchgegangen und auf die Symbole geachtet.
Diese werden zusammen gerechnet und der Prosentsatz dazu erstellt.