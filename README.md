Code von Karin, um GND-Identifier für die Namenslisten aus Brümmer und Pataky über lobid zu finden. 

Tabellen zu Pataky und Brümmer. 

Karin, 5.12.2024
Hinweis zu der Tabelle für Pataky: Manche der Autor:innen sind doppelt vorhanden, jedoch mit unterschiedlichen Einträgen in den Spalten Biografie und Bibliografie. Der Grund dafür liegt darin, dass das Lexikon diese Autor:innen doppelt aufführt (warum, keine Ahnung). Die beiden Bände sind alphabetisch sortiert, am Ende des 2. Bands jedoch stehen wieder Einträge, die von A starten. Daher die Doppelungen.

Karin, 09.01.2025
API Request über die lobid gnd API durchgeführt. Die Abfrage wurde über die Kategorien "Schriftstellerin" und "Schriftsteller" geführt mit den Einschränkungen "Person" "DifferentiatedPerson" und einem Geburtsdatum zwischen 1750 und 1870

Die entstandene Tabelle ist unter dem Namen "lobid-schriftstellerinnen.csv" im Ordner "data"

29.05.2025: CSV-Tabellen mit Sprachen, erkannt durch Prompt mit Claude, eingefügt.

17.6.2025: Hinweise von Nanette zu Pseudonymen: 

ja in dem Fall würde ich entweder eine Spalte für Pseudonyme nehmen, in der auch mehrere Namen drin stehen können, die dann aber mit dem immer gleichen Zeichen (;) und in der immer gleichen Art dargestellt werden: z .B. Vorname Nachname; Vorname Nachname oder Künstlername1; Künstlername2
Alternativ, wenn du wirklich Fehler in diesem System (Trennung mit Semikolon und verschiedene Schreibweisen von Vorname Nachname etc) vermeiden willst, dann kannst du auch für jeden Namen eine eigene Spalte nehmen (auch da muss die Schreibweise aber ja einheitlich sein.
Es gibt bestimmt ein paar best practices: hier hat José eine Korpustabelle erstellt, wo die Autoren einfach durch ihre VIAF (oder anderen Identifier) desambiguiert werden… https://github.com/cligs/conssa/blob/master/metadata/metadata.tsv 

17. Juni 2025:
  Liste: Pataky-Gesamt: ALLE Autorinnen, GND und nicht-GND kombiniert.
GesamtListe: alle Kategorien ID, Name, Vorname, Alternativnamen, Geburtsdatum, Sterbedatum, Ort1, Ort2, Ort3 ... , Sprache1..., Sprache2...   Publikationen (wenn möglich die Publikationen in einer Spalte, mit Semikolon getrennt). 


    

    
