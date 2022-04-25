class Fahrzeug:
  def __init__(self, name, tank_prozent, geschwindigkeit):
    self.name = name
    self.tank_prozent = tank_prozent
    self.geschwindigkeit = geschwindigkeit

  def beschleunigen(self):
    self.geschwindigkeit += 10
    print(f'Du hast auf {self.geschwindigkeit}km/h beschleunigt!')
    return self

  def bremsen(self):
    self.geschwindigkeit -= 10
    print(f'Du hast auf {self.geschwindigkeit}km/h gebremst!')
    return self

  def tanken_bis_prozent (self, val):
    self.tank_prozent = val
    print(f'Du hast deinen Tank auf {self.tank_prozent}% getankt!')
    return self

class Motorrad(Fahrzeug):
  def __init__(self, name, tank_prozent, geschwindigkeit, hat_gepäckträger):
    super().__init__(name, tank_prozent, geschwindigkeit)
    self.hat_gepäckträger = hat_gepäckträger

  def mach_wheelie(self):
    print('WROOOOM')
    return self

class Auto(Fahrzeug):
  def __init__(self, name, tank_prozent, geschwindigkeit, hat_kindersitze):
    super().__init__(name, tank_prozent, geschwindigkeit)
    self.hat_gepäckträger = hat_kindersitze

  def mach_drift(self):
    print('QUIEETTTSCH')
    return self

# Test Data: Motorrad mit 60% Tank, 70km/h, keinem Gepäckträger
print("===== MOTORRAD =====")
yzfr = Motorrad('Yamaha YZF-R', 60, 70, False)
yzfr.beschleunigen().bremsen().tanken_bis_prozent(90).mach_wheelie()

# Test Data: Auto mit 20% Tank, 40km/h, Kindersitzen
print("===== AUTO =====")
e30 = Auto('BMW E30', 20, 40, True)
e30.beschleunigen().beschleunigen().mach_drift().bremsen().bremsen().tanken_bis_prozent(66)


  
