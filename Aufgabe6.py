#Oben beschriftet mit 1 bis 10
print('    ', end='') 
for i in range(1, 11):
    print('{:4}'.format(i), end='') 
print() 

#abtrennung von oben zu tabelle
for i in range(23):
    print('-', end=' ')
print() 


for i in range(1, 11):
    print('{:2} |'.format(i), end=' ')
    for j in range(1, 11):
        multipliziert = i * j
        print('{:4}'.format(multipliziert), end='')
    print() 
