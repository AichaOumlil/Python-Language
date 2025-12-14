votes = ["Yasmine","Amine","Yasmine","Omar","Yasmine","Amine","Omar","Amine","Yasmine","Sara","Omar","Yasmine","Sara"]
votes_dictio={}
vot_yasmine = 0
vot_sara = 0
vot_omar = 0
vot_amine = 0
for tmp in votes :
    if tmp == "Yasmine" :
       vot_yasmine +=1
    elif tmp == "Amine" :
        vot_amine += 1
    elif tmp == "Omar" :
        vot_omar +=1
    elif tmp == "Sara" :
        vot_sara +=1
votes_dictio ={
    "Yasmine":vot_yasmine ,
    "Amine":vot_amine ,
    "Omar":vot_omar ,
    "Sara":vot_sara,
    } 
print(f'Résultat des votes :{votes_dictio}')
for candidat , nbr_vot in votes_dictio.items :
    if nbr_vot > vot_max :
        vot_max = nbr_vot 
        meuilleur_candidat = candidat
print(f"Le candidat avec le plus de votes est :{meuilleur_candidat} avec {vot_max} votes")