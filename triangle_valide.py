a = float(input ('Entrez la longueur du côté a :'))
b = float(input ('Entrez la longueur du côté b :'))
c = float(input ('Entrez la longueur du côté c :'))
if (a+b >c and a+c>b and b+c>a) :
    print ('Triangle valide')
else :
    print ('Triangle invalide')