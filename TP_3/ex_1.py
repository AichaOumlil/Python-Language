nbr_entier = int (input ("Veuillez entrer un nombre entier (positif) : "))
som = 0
while nbr_entier >= 0 :
    nbr_entier = int (input ("Veuillez entrer un nombre entier (positif) : "))
    som += nbr_entier
print (f"La somme des nombres entiers saisie est : {som}")