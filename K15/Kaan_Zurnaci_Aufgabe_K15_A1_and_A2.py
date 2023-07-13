# Klasse Haus erstellen
class Haus:
    def __init__(self, strasse, hausnummer, farbe, preis, stockwerke, quadratmeter):
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.farbe = farbe
        self.preis = preis
        self.stockwerke = stockwerke
        self.quadratmeter = quadratmeter

# Objekt Haus erstellen & Werte übergeben
mein_haus = Haus("Am Judensand", "12a", "Gelb", 259.999, 3, 200)

# Alle Werte vom Haus ausgeben
print("Straße:", mein_haus.strasse)
print("Hausnummer:", mein_haus.hausnummer)
print("Farbe:", mein_haus.farbe)
print("Preis:", mein_haus.preis,"€")
print("Stockwerksanzahl:", mein_haus.stockwerke)
print("Quadratmeter:", mein_haus.quadratmeter,"m²")
