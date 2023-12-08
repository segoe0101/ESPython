Punktzahl = int(input("Hier die Punktzahl angeben: "))

if (Punktzahl >= 0 and Punktzahl <= 100):
    print("Eingabe möglich")

    if Punktzahl >= 95:
        print("Note ist: 1.0")
    elif Punktzahl >= 90:
        print("Note ist: 1.3")
    elif Punktzahl >= 85:
        print("Note ist: 1.7")
    elif Punktzahl >= 80:
        print("Note ist: 2.0")
    elif Punktzahl >= 75:
        print("Note ist: 2.3")
    elif Punktzahl >= 70:
        print("Note ist: 2.7")
    elif Punktzahl >= 65:
        print("Note ist: 3.0")
    elif Punktzahl >= 60:
        print("Note ist: 3.3")
    elif Punktzahl >= 55:
        print("Note ist: 3.7")
    elif Punktzahl >= 50:
        print("Note ist: 4.0")
    else:
        print("Note ist: 5.0")



else:
    raise Exception('Die Punktangabe ist fehlerhaft und so nicht möglich')