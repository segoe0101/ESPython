#nicht fertig

import math
import statistics

class Statisik:
    def __init__(self):
        self.daten = []
    
    def hinzufuegen(self, zahl):
        try:
            if isinstance(zahl, (int, float)):
                self.daten.append(zahl)
            elif isinstance(zahl, list):
                self.daten.extend(zahl)
            else:
                raise ValueError('Falsche Daten angegeben')
        except ValueError as e:
            print(f"Fehler: {e}")
        

    def KomplettLoeschen(self):
        self.daten = []
    
    def Minimalwert(self):
        try:
            minimum = min(self.daten)
            print(minimum)
        except ValueError:
            print("Fehler")

    def Maximalwert(self):
        try:
            maximum = max(self.daten)
            print(maximum)
        except ValueError:
            print("Fehler")
    
    def Mittelwert(self):
        try:
            Summe = sum(self.daten)
            Anzahl = len(self.daten)
            mittelwert = Summe / Anzahl
            print(mittelwert)
        except ValueError:
            print("Fehler")

    def Median(self):
        try:
            median = statistics.median(self.daten)
            print (median)
        except ValueError:
            print("Fehler")

    def Standardabweichung(self):
        try:
            standardabw = statistics.stdev(self.daten)
            print (standardabw)
        except ValueError:
            print("Fehler")

    




erstertest = Statisik()
erstertest.hinzufuegen("string")
erstertest.hinzufuegen(5)
erstertest.hinzufuegen(2)
erstertest.hinzufuegen(10)
erstertest.Minimalwert() 
erstertest.Mittelwert()
erstertest.Median()
erstertest.Standardabweichung()