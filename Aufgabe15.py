class zaehler:
    def __init__(self, startwert):
        self.zaehlerstand = startwert
    
    def weiter ( self ):
        self.zaehlerstand += 1

    def zurueck ( self ):
        self.zaehlerstand -= 1

    def wert ( self ):
        return self.zaehlerstand