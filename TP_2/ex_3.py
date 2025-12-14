taches = []
taches.append ("Faire les cours")
taches.append ("Envoyer un email")
taches.append ("Etudier")
taches.append ("Nettoyer la maison")
print(f"Listes des tâches : {taches}")
touche =input ("Entrez une tâche : ")
if touche in taches :
    index = taches.index(touche)
    print (f"La tâche '{touche}' est à la position {index}")
else :
    print(f"La tâche {touche} ne se touve pas dans la liste")
touche_nv = input ("Entrez une nouvelle tâche à ajouter : ")
position = int (input ("A quelle position souhaitez-vous ajouter la tâche (entre 0 et 4) : ") )
taches.insert ( position, touche_nv)
print(taches)