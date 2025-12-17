v1 = int (input ('Entrez v1 : '))
v2 = int (input ('Entrez v2 : '))
v3 = int (input ('Entrez v3 : '))
print(f'Valeurs initiales : v1 = {v1} , v2={v2} , v3={v3}')
if v1 > v2 :
    v1 , v2 = v2 , v1
if v1 > v3 :
    v1 , v3 = v3 , v1
if v2 > v3 :
    v2 , v3 = v3 , v2
print(f'Valeurs finales : v1 = {v1} , v2={v2} , v3={v3}')