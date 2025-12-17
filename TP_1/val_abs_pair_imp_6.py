x = int (input ("Veuillez entrer un entier : "))
if x < 0:
    val_abs = -x 
else :
    val_abs = x 
print(f"La valeur absolue de ({x})  est {val_abs}")
if val_abs % 2 == 0 :
    print (f"La valeur absolue de ({x}) est pair ")
else :
    print (f"La valeur absolue de ({x}) est impair")