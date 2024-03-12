# documentation
Wie bekommen wir am meisten GND-Identifier für die Namenslisten aus den Schriftstellerlexika (Brümmer und Pataky)?
1. im JSON-Schema von lobid nachsehen, welche Informationen vorhanden sind, was davon required ist: [JSON-Schema](https://github.com/hbz/lobid/blob/master/schemas/person.json).
2. Es handelt sich immer um Personen, davon ausgehend andere Kategorien berücksichtigen, wie etwa Zeitraum, Beruf, Gender, Orte.
3. In Python filtern oder durch Query parameter steuern? 

Allgemeine Informationen zur [Datenstrukturierung von lobid](https://github.com/hbz/lobid/blob/master/doc/lobid.md).


Statt APIS, selbstgebasteltes Tool: Daten in Github, Texte einbinden, dann mit [hypthesis](https://web.hypothes.is/) annotieren.

## Suche und Filter:

+ Ids finden über obligatorische Kategorien: Type: Person und name (hier preferredName und variantName verwenden).
+ nicht obligatorisch: zeitlicher Filter: Geburtsdatum zwischen 1749 (Geburtsjahr Goethe) und 1890. Die dadurch entstandenen Treffer verwenden, wenn es nicht gefunden wird, trotzdem behalten und neu suchen nach Beruf.
+ Beruf: Autor OR Autorin (als Oberbegriff von Schriftsteller etc.). 
+ Wenn es dann einen Treffer gibt, diesen nehmen.
+ Wenn es mehrere Treffer gibt, die jeweiligen Links zu den Einträgen aufführen für eine manuelle Überprüfung. 
+ Wenn es keinen Treffer gibt, notieren: kein Treffer. 
