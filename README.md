# Bücherverwaltung 
## 1. Problembeschreibung
Aktuell erfasse ich meine gelesenen Bücher handschriftlich.
## 2. Projektidee
Mithilfe der Webapplikation, möchte ich eine gute Übersicht von meinen Büchern erschaffen. Ich möchte bereits gelesene Bücher erfassen und Vorschläge für neue Bücher erhalten.
## 3. Workflow
![Workflow](https://user-images.githubusercontent.com/113971574/202894817-173e4bf0-c66c-4946-a20e-0c016df6896b.jpg)
## 4. Programmübersicht
### Erfassen
Hier kann der User ein neues Buch erfassen.
- Folgende Daten werden dafür benötigt: 
    - Titel (Text)
    - Author (Text)
    - Genre (Auswahl)
      - Fantasy
      - Thriller
      - Sci-Fi
      - Dystopian
      - Non-Fiction
    - Bewertung (Zahl)
- Die Eingabe kann mit dem Button "Buch erfassen" gespeichert werden. 
  - Falls eine Feld nicht ausgefüllt wird, erscheint eine Fehlermeldung.
  - Bei der Bewertung, muss eine Zahl grösser als 1 sein. Ansonsten erscheint wiederum eine Fehlermeldung.
### Abfrage
Hier werden neue Bücher für den User vorgeschlagen
- Folgende Daten werden dafür benötigt:
  - Titel (Text)
  - Author (Text)
  - Genre (Auswahl)
    - Fantasy
    - Thriller
    - Sci-Fi
    - Dystopian
    - Non-Fiction
  - Bewertung (Zahl)
- Nachdem der User den Button "Vorschläge anzeigen" ausgewählt hat, werden die Angaben des Users mit bereits Erfassten Einträgen in der Datenbank verglichen.
  - Wenn man bei Titel, Author und Bewertung nichts spezifisches Suchen möchte, kann man das Eingabefeld leer lassen.
### Übersicht
- Hier kann man die bereits gelesenen Bücher anschauen
- Die totale Anzahl wird angezeigt
## 5. Funktionen 
- Dateneingabe: neues Buch erfassen, Abfrage für ein Büchervorschlag
- Datenspeicherung: mögliche Büchervorschläge und bereits gelesene Bücher werden in JSON-Datei gespeichert
- Datenverarbeitung: Abfrage wird mittels For-Schleife mit der Datenbank Bücher verglichen, Berechnung der gesamten Bücher
- Datenausgabe: Ausgabe der Büchervorschlägen, Ausgabe der gespeicherten Bücher
## 6. Mögliche zukünftige Erweiterungen des Programms
Die Applikation könnte mit den folgenden Ideen erweitert werden:
- Grafische Darstellung von allen erfassten Büchern 
- Die Seitenanzahl von gelesenen Büchern zusammenzählen
- Grössere Auswahl von den Genres 
- Nicht nur gelesene Bücher erfassen sondern auch "Currently Reading" und "To Be Read" integrieren.
- Bewertungen farbig machen (z.B Rot = 1, schlecht)
