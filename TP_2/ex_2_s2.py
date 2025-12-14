votes = ["Yasmine","Amine","Yasmine","Omar","Yasmine","Amine","Omar","Amine","Yasmine","Sara","Omar","Yasmine","Sara"]
resultats ={}
for nom in votes :
    if nom in resultats :
        resultats[nom] += 1
    else :
       resultats[nom] = 1
print ('Résultats des votes :', resultats)
max = 0
for nom in votes :
    if resultats[nom] > max :
        candidat_max = nom
        max = resultats[nom]
print(f"Le candidat le plus de votes est : {candidat_max} avec {resultats[candidat_max]} votes")