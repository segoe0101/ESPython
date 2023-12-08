from datetime import datetime


class Logger:
    def __init__(self, dateiname):
        self.dateiname = dateiname
        self.datei = open(dateiname, 'a') #die Datei wird durch das 'a' im append-modus geöffnet

    def __del__ (self):
        self.datei.close()

    def EintragSchreiben(self):
        inhalt = input("Hier angeben was in die log datei rein soll: ")
        zeitstempel = datetime.now()
        zeitstempel = zeitstempel.strftime ( '%d.%m.%Y, %H:%M:%S' )
        zeitstempel = str(zeitstempel)
        inhalt = "\n" + zeitstempel + ":\n" + inhalt
        print("Folgendes wird in die Logdatei eingefügt: " + "\n" + inhalt)
        self.datei.write(inhalt)
        self.datei.close()


testdatei = Logger('Logdatei.txt')
testdatei.EintragSchreiben()