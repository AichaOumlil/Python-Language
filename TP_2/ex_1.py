liste_temperature = [20,22,19,23,21,18,20]
temp_max = liste_temperature[0]
for temp in liste_temperature :
    if temp > temp_max :
        temp_max = temp
print(f'Température la plus élevée  est : {temp_max} ')
temp_min = liste_temperature[0]
for temp in liste_temperature :
    if temp < temp_min :
        temp_min = temp
print(f'Température la plus basse est : {temp_min} ')
som = 0
for temp in liste_temperature :
    som += temp
nbr_jr = 0
for _ in liste_temperature :
    nbr_jr += 1
moy = som / nbr_jr
print(f'Température moyenne est : {moy:.2f} ')
jr_sous_moy = 0
for temp in liste_temperature :
    if temp < moy :
        jr_sous_moy += 1
print(f'Nombre de jours en dessous de la moyenne : {jr_sous_moy}')
liste_temperature[2] = 25
print('Nouvelle liste des températures :', liste_temperature)