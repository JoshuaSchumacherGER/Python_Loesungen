# ===== Aufgabe 1 =====
# Erstelle eine Klasse Haus inkl. Konstruktor, welches über folgende Attribute verfügt: Straße, Hausnummer, Farbe, Preis, Stockwerksanzahl, Quadratmeter.
class Haus:
  def __init__(self, strasse, hausnummer, farbe, preis, stockwerke, qm):
    self.strasse = strasse
    self.hausnummer = hausnummer
    self.farbe = farbe
    self.preis = preis
    self.stockwerke = stockwerke
    self.qm = qm

  def introduce_house(self):
    print(f'Ich wohne in der {mein_haus.strasse} {mein_haus.hausnummer}. Mein Haus ist {mein_haus.farbe} und hat {mein_haus.stockwerke} Stockwerke. Für die {mein_haus.qm}m3 haben wir {mein_haus.preis}€ bezahlt')

  def neuer_anstrich(self, farbe):
    self.farbe = farbe

# ===== Aufgabe 2 =====
# Erstelle ein Objekt der Klasse Haus mit beliebigen Werten. Gebe danach alle Werte auf der Konsole wieder aus.
mein_haus = Haus ('Musterstraße', 187, 'blau', 750_000, 3, 120)
mein_haus.introduce_house()

# ===== Aufgabe 3 =====
# Erstelle 3 verschiedene Hausobjekte und speichere diese in einer Liste. Lösche danach das letzte Haus in der Liste und gebe die Liste entsprechend auf der Konsole aus.
haus1 = Haus('Hildegardisstraße', 210, 'gelb', 1_750_000, 5, 240)
haus2 = Haus('An der Weed', 1337, 'grün', 420_420, 4, 140)
haus3 = Haus('Bahnhofsstraße', 1, 'grau', 100_333, 2, 100)

häuser = [haus1, haus2, haus3]
häuser.pop()
print(häuser)

# ===== Aufgabe 4 =====
# Füge der Klasse die Methode neuer_anstrich(farbe) hinzu, die eine neue Farbe nimmt und den Wert entsprechend abändert. Erstelle dann ein Objekt, dessen Farbe nachträglich geändert wird und gebe diesen Wert auf der Konsole erneut aus.
# Methode s.o. in Klasse
print(haus3.farbe)
haus3.neuer_anstrich('gelb')
print(haus3.farbe)

# ===== Aufgabe 5 =====
# Erstelle eine neue Hausliste mit 3 Hausobjekten. Danach soll überprüft werden, ob ein Haus über 200.000€ kostet. Falls ja, wird das Haus aus der Liste entfernt. Gebe anschließend die Liste auf der Konsole aus.
häuser_alt = [haus1, haus2, haus3]
häuser_unter_200000 = [x for x in häuser_alt if x.preis < 200_000]
print(häuser_alt)
print(häuser_unter_200000)






