# 1. Initialisation de la salle de cinéma
cinema = [[0 for _ in range(4)] for _ in range(5)]

# 2. Réservation d'une place à la rangée 2, siège 3
cinema[1][2] = 1
print("Salle après la réservation de la place à la rangée 2, siège 3 :")
for row in cinema:
    print(row)

# 3. Vérification de la disponibilité de la place à la rangée 4, siège 1
if cinema[3][0] == 0:
    print("\nLa place à la rangée 4, siège 1 est disponible.")
else:
    print("\nLa place à la rangée 4, siège 1 est déjà prise.")

# 4. Comptage du nombre total de places libres
places_libres = sum(row.count(0) for row in cinema)
print(f"\nNombre total de places libres : {places_libres}")

# 5. Réservation de 3 places côte à côte à la rangée 5
rangée_5 = cinema[4]
for i in range(len(rangée_5) - 2):
    if rangée_5[i] == rangée_5[i+1] == rangée_5[i+2] == 0:
        rangée_5[i] = rangée_5[i+1] = rangée_5[i+2] = 1
        break

print("\nSalle après la réservation de 3 places côte à côte à la rangée 5 :")
for row in cinema:
    print(row)