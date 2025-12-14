#----------1----------
phrase_saisie = input("Entrez un phrase ou un paragraphe : ")


#----------2----------

#methode 1
#nb = len(phrase_saisie)
#print(f"Nombre total de caractéres : {nb}")

#meyhode 2
nbr_caractere = 0
for i in phrase_saisie :
    nbr_caractere +=1
print(f"Nombre total de caractéres : {nbr_caractere}")


#----------3----------

#methode 1
#mots = phrase_saisie.split ()
#nbrr_mot =len(mots)
#print(f"Nombre total de mots : {nbrr_mot}")

#methode 2
nbr_mot = 1
for i in phrase_saisie :
    if i == " " :
        nbr_mot +=1
    else :
        nbr_mot += 0
print(f"Nombre total de mots : {nbr_mot}")

#methode 3
# nb_mot = 0
# mot_en_cours = False
# for char in phrase_saisie :
#   if char != " " :
#       if not mot_en_cours :
#           nb_mot += 1
#           mot_en_cours = True
#   else :
#       mot_en_cours = False
#  print(f"Nombre total de mots : {nbr_mot}")


#----------4----------

#methode 1
#print("Texte en majuscule :" ,phrase_saisie.upper )

#methode 2
texte_maj = ""
for i in phrase_saisie :
    if 'a'<= i <= 'z' :
        texte_maj +=chr(ord(i)-32)
    else :
        texte_maj += i
print(f"Texte en majuscule : {texte_maj}")


#----------5----------

#methode 1
#print("Texte en minuscule :" ,phrase_saisie.lower )

#methode 2
texte_min = ""
for i in phrase_saisie :
    if 'A' <= i <= 'Z' :
        texte_min += chr(ord(i)+32)
    else :
        texte_min += i
print(f"Texte en minuscule : {texte_min}")


#----------6----------

#methode 1
#recherche=input("Entrer un caractére à rechercher : ")
#count= texte.count(recherche)
#if count > 0 :
#   print(f"Le caractére '{recherche}' apparaît {count} fois dans le texte. ")
#else : 
#   print(f"Le caractére '{recherche}' n'apparaît pas {count} fois dans le texte. ")


#methode 2
nb_caractére_cherché = 0
caractére_cherché = input("Entrer un caractére à rechercher : ")
for i in phrase_saisie :
    if caractére_cherché == i :
        nb_caractére_cherché += 1
if nb_caractére_cherché > 0 :
    print(f"Le caractére '{caractére_cherché}' apparaît {nb_caractére_cherché} fois dans le texte. ")
else : 
     print(f"Le caractére '{caractére_cherché}' n'apparaît pas {nb_caractére_cherché} fois dans le texte. ")


#----------7----------

#methode 1
#if phrase_saisie == phrase_saisie[::-1] :
#   print("La phrase est un palindorme") #
#else :
#   print("La phrase n'est pas un palindorme  ")

#methode 2
inverse= ""
for i in range (len(texte_min)-1,-1,-1):
    inverse += texte_min[i]

if texte_min == inverse :
    print("La phrase est un palindorme")
else :
    print("La phrase n'est pas un palindorme  ")