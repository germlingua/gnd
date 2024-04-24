# documentation
Wie bekommen wir am meisten GND-Identifier für die Namenslisten aus den Schriftstellerlexika (Brümmer und Pataky)?
1. im JSON-Schema von lobid nachsehen, welche Informationen vorhanden sind, was davon required ist: [JSON-Schema](https://github.com/hbz/lobid/blob/master/schemas/person.json).
2. Es handelt sich immer um Personen, davon ausgehend andere Kategorien berücksichtigen, wie etwa Zeitraum, Beruf, Gender, Orte.
3. In Python filtern oder durch Query parameter steuern? 

Allgemeine Informationen zur [Datenstrukturierung von lobid](https://github.com/hbz/lobid/blob/master/doc/lobid.md).


Statt APIS, selbstgebasteltes Tool: Daten in Github, Texte einbinden, dann mit [hypthesis](https://web.hypothes.is/) annotieren.

## Suche und Filter:

+ Ids finden über obligatorische Kategorien: Type: Person und name (hier preferredName und variantName verwenden).
+ nicht obligatorisch: zeitlicher Filter: Geburtsdatum zwischen 1749 (Geburtsjahr Goethe) und 1890. Die dadurch entstandenen Treffer verwenden. Wenn es nicht gefunden wird, trotzdem behalten und neu suchen nach Beruf.
+ Beruf: Autor OR Autorin (als Oberbegriff von Schriftsteller etc.). 
+ Wenn es dann einen Treffer gibt, diesen nehmen.
+ Wenn es mehrere Treffer gibt, die jeweiligen Links zu den Einträgen aufführen für eine manuelle Überprüfung. 
+ Wenn es keinen Treffer gibt, notieren: kein Treffer.

+ Bei mehreren Treffern, bei denen das Geburtsdatum stimmt und kein Eintrag zum Beruf gefunden wird: Optionen auflisten. 
Die Filterreihenfolge sollte so sein, wie Karin es beschreibt: erst Geburtsdatum, dann Beruf. Es gibt nämlich mehr Einträge, die das Geburtsdatum beinhalten und es soll versucht werden, die Treffer nicht zu früh einzuschränken.

Adler Helene Schriftstellerin 1649 würde dann also schon beim ersten Filter rausfallen. Treffer im Untersuchungszeitraum sollten auch dann erhalten bleiben, wenn die berufliche Zuordnung nicht eindeutig ist. Also, wenn es z.B. auch eine Adler Helene Ehefrau von Adler Heinrich gibt, ohne Beruf, aber im Zeitraum, dann sollte das auch mit angeführt werden (ist wahrscheinlich nur selten der Fall).

## Umgebauter Code von Karin, 24.03.2024: die neuen Tabellen sind in der Cloud hochgeladen. Ich habe den Code
nochmal grundlegend umgebaut und neu strukturiert, deswegen hat alles
länger gedauert. Im github hab ich den neuen Code noch nicht
hochgeladen, das mache ich die Tage mal.

Ein paar Anmerkungen zu den Filtern und den Tabellen:
- ich habe mir von der api nur die Namen, den Beruf und das Geburtsjahr
bzw. Wirkungsjahr geholt. Die Auslagerung der Filterung an die api
Abfrage habe ich zeitlich nicht geschafft
- die Daten, die die api zurückgibt, werden folgendermaßen gefiltert:

Filter nach Jahr:
- wenn die api kein Ergebnis zu dem Namen gefunden hat, dann wird
"kein Eintrag von api" zurückgegeben
- wenn ein oder mehrere Einträge Treffer möglich sind, dann wird
überprüft, ob das Jahr im gewünschten Zeitfenster liegt. Wenn ja, dann
werden eine oder mehrere passende Einträge zurückgegeben. Werden keine
passenden Einträge gefunden, wird der ganze Eintrag zurückgegeben, weil
die Möglichkeit besteht, dass einfach kein Jahr erfasst ist (hier bin
ich noch nicht zufrieden mit dem Filter, aber ich dachte, lieber gebe
ich mehr Einträge zurück, als dass wir welche verlieren. Ein möglicher
Fall wäre z.b. wir haben nur einen Treffer, der außerhalb des
Zeitfensters liegt. Die Funktion würde in diesem Fall den ganzen Eintrag
zurückgeben).
- der Filter gibt eine Liste zurück, die entweder einen String mit
"kein Eintrag von api" oder eine Liste mit >= 1 Einträgen mit
potentiellen Treffern enthält

Filter nach Autor:in:
- die nach Zeitfenster vorgefilterte Liste wird daraufhin geprüft, ob
die Einträge pro Namen eine Berufsbezeichnung aufweisen. Liegt eine vor,
werden nur die Einträge pro Name behalten, die entweder
"Autorin"/"Autor" oder "Schriftstellerin"/"Schriftsteller" als
Berufsbezeichnung haben. Liegt keine Berufsbezeichnung vor, wird der
entsprechende Eintrag zurückgegeben.
- im Fall, dass nur ein Treffer in der Liste war, dieser also im
Untersuchungzeitraum liegt, aber klar nicht "Autorin"/"Autor" oder
"Schriftstellerin"/"Schriftsteller" als Berufsbezeichnung haben, wird
der String "im Untersuchungszeitraum, aber Beruf eindeutig nicht als
"Autor:in" gelabeled" zurückgegeben. (Auch mit dieser Lösung bin ich
nicht happy..)
- der Filter gibt eine Liste zurück, die entweder einen String mit "kein
Eintrag von api", einen String mit "im Untersuchungszeitraum, aber Beruf
eindeutig nicht als "Autor:in" gelabeled" oder eine Liste mit >= 1
Einträgen mit potentiellen Treffern enthält

Aus dieser Liste werden dann im letzten Schritt die gnd Daten
extrahiert, wenn kein eindeutiges Ergebnis vorliegt, werden die Links zu
den Einträgen zurückgegeben und das ganze als csv Dokument abgespeichert
(und dann noch aufgesplittet in gefunden/nicht gefunden.

## Fragen zu Version 23.03.:
In der Liste mit GND nicht gefunden, sind Treffer enthalten, die eigentlich gefunden werden müssten , zb Adlersfeld-Ballestrem, Eufemia von (im Zeitraum, als Schriftstellerin verzeichnet) oder Wilhelm Ahrens - woran könnte das liegen? 

## Liste der Berufsbezeichnungen 

Problem: bei der Abfrage werden bestimmte Resultate verworfen, weil dre Beruf "Schriftsteller" nicht gefunden wurde bzw. die Teil-Synonyme nicht als zugehörig erkannt wurden (z.B. Dramatiker, Lyriker etc.).
Anscheinend ist Schriftsteller (https://lobid.org/gnd/4053309-8) der Oberbegriff für folgende Berufsbezeichungen: 
Theaterdichter, Theaterdichterin, Dramatiker, Dramatikerin, Lyriker, Lyrikerin, Bestsellerautor, Bestsellerautorin, 
weitere Synonyme: Dichter, Dichterin, Autor, Autorin

