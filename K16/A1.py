class Haus():
  def __init__(self, strasse, hausnr, qm, preis):
    self.strasse = strasse
    self.hausnr = hausnr
    self.qm = qm
    self.preis = preis

  @property
  def preis(self):
    return self.__preis

  @preis.setter
  def preis(self, val):
    if val > 0:
      self.__preis = val
    else:
      print('Du musst einen Wert über 0 eingeben!')

mein_haus = Haus('Peterstraße', 13, 190, 400_000)
mein_haus.preis = 1
