# documentation
Wie bekommen wir am meisten GND-Identifier für die Namenslisten aus den Schriftstellerlexika (Brümmer und Pataky)?
1. im JSON-Schema von lobid nachsehen, welche Informationen vorhanden sind, was davon required ist: [JSON-Schema](https://github.com/hbz/lobid/blob/master/schemas/person.json).
2. Es handelt sich immer um Personen, davon ausgehend andere Kategorien berücksichtigen, wie etwa Zeitraum, Beruf, Gender, Orte.
3. In Python filtern oder durch Query parameter steuern? 
