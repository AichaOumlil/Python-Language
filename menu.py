# Initialisation de la base de données des étudiants
base_etudiants = []

# --- Boucle principale du programme ---
choix = ""
while choix != "5":
    # Affichage du menu
    print("\n--- Menu de l'Application ---")
    print("1. Ajouter un étudiant")
    print("2. Afficher tous les étudiants")
    print("3. Calculer la moyenne d'un étudiant")
    print("4. Afficher l'étudiant ayant la meilleure moyenne")
    print("5. Quitter")
    print("-" * 25)

    choix = input("Votre choix : ")

    # 1. Ajouter un étudiant
    if choix == "1":
        print("\n--- Ajout d'un étudiant ---")
        
        # Saisie des informations
        nom = input("Nom : ")
        
        # Saisie et validation de l'Âge 
        age_valide = False
        age_str = ""
        while not age_valide:
            age_str = input("Âge : ")
            
            # Validation
            i = 0
            est_chiffre = True
            compteur_age_str = 0
            # longueur de la chaîne 
            for caractere in age_str:
                compteur_age_str += 1
                
            while i < compteur_age_str:
                caractere = age_str[i]
                # Vérifier si chaque caractère est un chiffre
                if caractere < '0' or caractere > '9':
                    est_chiffre = False
                    break
                i += 1
            
            if est_chiffre and compteur_age_str > 0:
                # Convertir la chaîne en entier
                age = int(age_str)
                if age > 0:
                    age_valide = True
                else:
                    print("Erreur : L'âge doit être un nombre entier positif.")
            else:
                print("Erreur : L'âge doit être un nombre entier.")

        notes_str = input("Notes (séparées par des espaces) : ")
        
        # Conversion des notes en liste de float 
        notes_list_str = notes_str.split()
        notes = []
        notes_valides = True
        
        # Compter le nombre d'éléments dans notes_list_str
        compteur_notes_string = 0
        for item in notes_list_str: 
            compteur_notes_string += 1
        
        j = 0
        while j < compteur_notes_string:
            note_str = notes_list_str[j]
            
            # Validation 
            nombre_points = 0
            k = 0
            est_nombre = True
            
            #  longueur de la note_str 
            compteur_note_str = 0
            for char_note in note_str:
                compteur_note_str += 1
            
            while k < compteur_note_str:
                caractere = note_str[k]
                if caractere == '.':
                    nombre_points += 1
                elif caractere < '0' or caractere > '9':
                    est_nombre = False
                    break
                k += 1
                
            if nombre_points > 1 or not est_nombre or compteur_note_str == 0:
                print(f"Erreur : La note '{note_str}' n'est pas un nombre décimal valide. L'étudiant ne sera pas ajouté.")
                notes_valides = False
                break
            
            #  convertir la chaîne en float
            notes.append(float(note_str))
            j += 1
        
        # Création et ajout de l'étudiant
        if notes_valides:
            nouvel_etudiant = {
                "Nom": nom,
                "Âge": age,
                "Notes": notes
            }
            base_etudiants.append(nouvel_etudiant)
            print(f"L'étudiant '{nom}' a été ajouté.")

    # 2. Afficher tous les étudiants
    elif choix == "2":
        print("\n--- Liste de tous les étudiants ---")
        
        # Compter le nombre d'étudiants 
        nombre_etudiants = 0
        for etu in base_etudiants:
            nombre_etudiants += 1
            
        if nombre_etudiants == 0:
            print("Aucun étudiant dans la base.")
        else:
            # Parcourir la liste
            i = 0
            while i < nombre_etudiants: 
                etudiant = base_etudiants[i]
                nom_etu = etudiant["Nom"]
                age_etu = etudiant["Âge"]
                notes_etu = etudiant["Notes"]
                
                # Format d'affichage lisible
                print(f"{nom_etu}, Âge : {age_etu}, Notes : {notes_etu}")
                i += 1

    # 3. Calculer la moyenne des notes d'un étudiant
    elif choix == "3":
        print("\n--- Calcul de la moyenne ---")
        nom_recherche = input("Nom de l'étudiant : ")
        
        etudiant_trouve = None
        
        # Compter le nombre d'étudiants 
        nombre_etudiants = 0
        for etu in base_etudiants:
            nombre_etudiants += 1
            
        # Recherche de l'étudiant
        i = 0
        while i < nombre_etudiants:
            etudiant_courant = base_etudiants[i]
            if etudiant_courant["Nom"].lower() == nom_recherche.lower():
                etudiant_trouve = etudiant_courant
                break
            i += 1
            
        if etudiant_trouve:
            notes = etudiant_trouve["Notes"]
            
            # Compter le nombre de notes
            nombre_de_notes = 0
            for note in notes:
                nombre_de_notes += 1
            
            if nombre_de_notes > 0:
                somme_notes = 0.0
                j = 0
                while j < nombre_de_notes: 
                    somme_notes += notes[j]
                    j += 1
                
                # Calcul de la moyenne
                moyenne = somme_notes / nombre_de_notes
                print(f"Moyenne de {etudiant_trouve['Nom']} : {moyenne:.2f}")
            else:
                print(f"L'étudiant {etudiant_trouve['Nom']} n'a pas de notes enregistrées.")
        else:
            print(f"Erreur : L'étudiant '{nom_recherche}' n'a pas été trouvé.")

    # 4. Afficher l'étudiant ayant la meilleure moyenne
    elif choix == "4":
        print("\n--- Meilleure moyenne ---")
        
        # Compter le nombre d'étudiants 
        nombre_etudiants = 0
        for etu in base_etudiants:
            nombre_etudiants += 1
        
        if nombre_etudiants == 0:
            print("Aucun étudiant dans la base pour calculer la meilleure moyenne.")
        else:
            meilleure_moyenne = -1.0
            meilleur_etudiant = None
            
            i = 0
            while i < nombre_etudiants: 
                etudiant = base_etudiants[i]
                notes = etudiant["Notes"]
                
                # Compter le nombre de notes 
                nombre_de_notes = 0
                for note in notes:
                    nombre_de_notes += 1
                
                if nombre_de_notes > 0:
                    # Calcul de la moyenne de l'étudiant courant
                    somme_notes = 0.0
                    j = 0
                    while j < nombre_de_notes: 
                        somme_notes += notes[j]
                        j += 1
                        
                    moyenne_courante = somme_notes / nombre_de_notes
                    
                    # Vérification si c'est la meilleure moyenne jusqu'à présent
                    if moyenne_courante > meilleure_moyenne:
                        meilleure_moyenne = moyenne_courante
                        meilleur_etudiant = etudiant
                
                i += 1
            
            if meilleur_etudiant:
                print(f"Étudiant ayant la meilleure moyenne : {meilleur_etudiant['Nom']} ({meilleure_moyenne:.2f})")
            else:
                print("Aucun étudiant avec des notes enregistrées pour déterminer le meilleur.")

    # 5. Quitter
    elif choix == "5":
        print("\nAu revoir !")
    
    # Gestion des choix invalides
    else:
        print("\nChoix invalide. Veuillez sélectionner une option entre 1 et 5.")