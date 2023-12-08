a = ['a', 'b', 'c']
b = ['a', 'b', 'c', 'd']

#apppend fügt eine Element der Liste hinzu
a.append ('d')
print(a)

#pop entfernt ein Element aus der Liste: beginnt bei 0; mit minus zählt von hinten; ohne index: letztes
a.pop(3)
print(a)

#extend fügt hier Liste b hinten an Liste a dran
a.extend(b)
print (a)

#remove entfernt ein Element aus der Liste
a.remove('b')
print(a)

#index gibt den index des ersten Elements mit dem angegebene Inhalt aus
index_b = a.index('b')
print (index_b)

#insert füght ein Element beim index ein
a.insert(2, 'eingefügt')
print(a)

#sort sortiert die Liste alphabetisch
a.sort()
print(a)


#Extend ist besser zum zusammenfügen von zwei Listen

#Reverse dreht den Inhalt des Arrays um
print(a)
a.reverse()
print(a)