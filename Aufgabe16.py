import math
import statistics

class Statisik:
    def __init__(self):
        self.daten = []
    
    def hinzufuegen(self, zahl):
        if isinstance(zahl, (int, float)):
            self.daten.append(zahl)
        elif isinstance(zahl, list):
            self.daten.append(zahl)
        else:
            print("Falsche Daten angegeben")

    def KomplettLoeschen(self):
        self.daten = []
    
    def Minimalwert(self):
        minimum = min(self.daten)
        print(minimum)

    def Maximalwert(self):
        maximum = max(self.daten)
        print(maximum)
    
    def Mittelwert(self):
        Summe = sum(self.daten)
        Anzahl = len(self.daten)
        mittelwert = Summe / Anzahl
        print(mittelwert)

    def Median(self):
        median = statistics.median(self.daten)
        print (median)

    def Standardabweichung(self):
        standardabw = statistics.stdev(self.daten)
        print (standardabw)

    




erstertest = Statisik()
erstertest.hinzufuegen(15)
erstertest.hinzufuegen(5)
erstertest.hinzufuegen(2)
erstertest.hinzufuegen(10)
erstertest.Minimalwert()
erstertest.Mittelwert()
erstertest.Median()
erstertest.Standardabweichung()