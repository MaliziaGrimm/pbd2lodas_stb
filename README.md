# pbd2lodas_stb
Konfigurationstool für Steuerberater für die Lodas Vorerfassung pbd2lodas

pbd2lodas ist eine Vorerfassung für Abrechnungsdaten (Bewegungsdaten) für die Lohnabrechnung mit DATEV Lodas.
Ein Personalfragebogen für neue Mitarbeiter ist auch nutzbar.

Es gibt 2 Toolpakete: pbd2lodas_stb und pbd2lodas_mdt.

pbd2lodas_stb: 
Steuerberater / Abrechnungsstelle nutzt das Konfigurationstool zur einmaligen Anlage der Stammdaten für das Erfassungstool pbd2lodas_mdt.
Es werden vom Steuerberater/Abrechnungstelle vorgegeben: Beraternummer, Mandantennummer, 5 Lohnarten für Stunden, 5 Lohnarten für Beträge.

Die erzeugte Datei "basisdaten.txt" ist im Verzeichnis /daten gespeichert. Diese Datei muss zum Mandanten / Erfassungsstelle und dort beim Tool pbd2lodas_mdt im Verzeichnis /daten gespeichert werden. 
