import pickle

# Beispiel-Datenliste mit unterschiedlichen Datentypen
datenliste = ['Test', 324, [1, 2, 3]]

# Datenliste in eine Datei speichern (pickle.dump)
datei = open('datenliste.pkl', 'wb')
pickle.dump(datenliste, datei)
datei.close()

#Alternativ zu den 3 Zeilen drüber kann man with benutzen:
#with open('datenliste.pkl', 'wb') as datei:
#    pickle.dump(datenliste, datei)

# Inhalt der generierten Datei anzeigen
with open('datenliste.pkl', 'rb') as datei:
    inhalt_der_datei = datei.read()
    print(f"Inhalt der Datei:\n{inhalt_der_datei}")

# Datenliste aus der Datei lesen (pickle.load)
with open('datenliste.pkl', 'rb') as datei:
    geladene_datenliste = pickle.load(datei)

# Ausgabe der geladenen Datenliste
print("\nGeladene Datenliste:")
print(geladene_datenliste)

