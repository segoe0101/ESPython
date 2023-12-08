class Zaehler:
    def __init__(self, startwert, minimalwert=None, maximalwert=None):
        self.minimalwert = minimalwert
        self.maximalwert = maximalwert
        self.setze_zaehlerstand(startwert)

    def setze_zaehlerstand(self, wert):
        if self.minimalwert is not None and wert < self.minimalwert:
            print(f"Fehler: Der Wert {wert} ist kleiner als der Minimalwert {self.minimalwert}")
            return
        if self.maximalwert is not None and wert > self.maximalwert:
            print(f"Fehler: Der Wert {wert} ist größer als der Maximalwert {self.maximalwert}")
            return
        self.zaehlerstand = wert

    def weiter(self):
        self.setze_zaehlerstand(self.zaehlerstand + 1)

    def zurueck(self):
        self.setze_zaehlerstand(self.zaehlerstand - 1)

    def wert(self):
        currentwert = self.zaehlerstand
        print(currentwert)

    def setze_maximalwert(self, maximalwert):
        self.maximalwert = maximalwert

    def setze_minimalwert(self, minimalwert):
        self.minimalwert = minimalwert

# Testen der erweiterten Klasse
a = Zaehler(5, minimalwert=0, maximalwert=5)



# Tests
print("Wert initial:", end=" ")
a.wert()
a.weiter()
print("Nach weiter:", end=" ")
a.wert()
a.zurueck()
print("Nach zurück:", end=" ")
a.wert()
a.setze_zaehlerstand(8)
print("Nach setze_zaehlerstand(8):", end=" ")
a.wert()
a.setze_maximalwert(15)
a.setze_minimalwert(5)
a.setze_zaehlerstand(2)
a.setze_zaehlerstand(20)

