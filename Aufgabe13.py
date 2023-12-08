#mit write: alles wird überschrieben
#mit a: es wird ohne leerzeichen alles angehängt


def JahrSchreiben():
    f = open ('Aufgabe13.txt', 'w')
    f.write ('Wir schreiben das Jahr {}.\n'.format(2023) )
    f.close()


def Lesen():
    f = open('Aufgabe13.txt', 'r')
    Inhalt = f.read (-1)
    print(Inhalt)
    f.close()
#readline: liest nur eine Zeile
#readlines: liest alle Zeilen, und gibt sie aus in einem Array


#Funktion aufrufen (# weg machen)
#JahrSchreiben()
Lesen()