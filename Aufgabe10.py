AlleNamen = []

#wenn man die 3 auf eine 10 stellt --> fertig
for i in range (3):
    Name1 = input("Namen eingeben: ")

    while Name1 in AlleNamen:
        print("ist schon drinnen")
        Name1 = input("hier einen neuen Namen eingeben: ")


    else:
        AlleNamen.append(Name1)
        AlleNamen.sort()


for i in AlleNamen:
    print(i)