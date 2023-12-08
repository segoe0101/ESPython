#Berechnung nicht richtig!

def berechne_note(punkte, maximale_punktzahl=100):
    if not (0 <= punkte <= maximale_punktzahl):
        return -1  # Ungültige Punktzahl

    bestehensgrenze = 0.5  # 50% der maximalen Punktzahl

    notenstufen = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]

    punkte_pro_note = maximale_punktzahl / len(notenstufen)

    for i, note in enumerate(notenstufen, start=1):
        grenze = maximale_punktzahl - i * punkte_pro_note
        if punkte >= grenze:
            return note

    return 5.0  # Prüfung nicht bestanden

# Beispielaufrufe
punktezahl = float(input("Geben Sie die Punktezahl ein: "))
maximale_punktzahl = float(input("Geben Sie die maximale Punktzahl ein (optional, Enter für Standard): ") or 100)

ergebnis = berechne_note(punktezahl, maximale_punktzahl)

if ergebnis == -1:
    print(f"Ungültige Punktzahl. Bitte geben Sie eine Punktzahl zwischen 0 und {maximale_punktzahl} ein.")
else:
    print(f"Die Note für {punktezahl} Punkte (maximal {maximale_punktzahl} Punkte) ist: {ergebnis}")
